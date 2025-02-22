# Copyright 2023 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Cell of auto parallel"""
from __future__ import absolute_import
from __future__ import division

import numpy as np

from mindspore import context
from mindspore.nn.cell import Cell
from mindspore.ops import operations as P
from mindspore.ops.operations.comm_ops import AllGather
from mindspore.communication import GlobalComm
from mindspore.common import jit
from mindspore.communication import create_group, destroy_group
from mindspore.communication._comm_helper import _get_group_map
from mindspore.train._utils import get_parameter_redundancy, remove_param_redundancy

_ALLGATHER_CELL = None


class AllGatherCell(Cell):
    """
    Allgather cell, used in model parallel scenario.
    To allgather the selected parameter slice from each device.
    """

    def __init__(self, group, do_reshape, after_reshape_slice_shape):
        super(AllGatherCell, self).__init__(auto_prefix=False)
        self.allgather = AllGather(group)
        self.do_reshape = do_reshape
        self.after_reshape_slice_shape = tuple(after_reshape_slice_shape)
        self.add_flags(skip_auto_parallel_compile=True)

    @jit()
    def construct(self, x):
        if self.do_reshape:
            x = P.Reshape()(x, self.after_reshape_slice_shape)
        x = self.allgather(x)
        return x


class SaveOptShardCkptCell(Cell):
    """
    Allgather cell, used in optimizer parallel scenario.
    Firstly gather the tensor to original layout in the specified device group.
    Then gather the whole parameter slices from all devices.

    Note:
        This could be optimized later with less communication consumption.
    """

    def __init__(self, group, do_reshape, after_reshape_slice_shape):
        super(SaveOptShardCkptCell, self).__init__(auto_prefix=False)
        self.allgather1 = AllGather(group)
        self.allgather2 = AllGather()
        self.do_reshape = do_reshape
        self.after_reshape_slice_shape = tuple(after_reshape_slice_shape)
        self.add_flags(skip_auto_parallel_compile=True)

    def construct(self, x):
        x = self.allgather1(x)
        if self.do_reshape:
            x = P.Reshape()(x, self.after_reshape_slice_shape)
        x = self.allgather2(x)

        return x


class SingleCommunicator(Cell):
    """
    Used to broadcast single parameter.
    """

    def __init__(self, group_name):
        super(SingleCommunicator, self).__init__()
        self.allreduce = P.AllReduce(group=group_name)
        self.add_flags(skip_auto_parallel_compile=True)

    def construct(self, loaded_param):
        result = self.allreduce(loaded_param)
        return result


def get_allgather_cell(group, need_merge_twice=False, do_reshape=False, after_reshape_slice_shape=()):
    """Get AllGatherCell object."""
    global _ALLGATHER_CELL
    if need_merge_twice:
        _ALLGATHER_CELL = SaveOptShardCkptCell(group, do_reshape, after_reshape_slice_shape)
    else:
        if group:
            _ALLGATHER_CELL = AllGatherCell(group, do_reshape, after_reshape_slice_shape)
        else:
            _ALLGATHER_CELL = AllGatherCell(GlobalComm.WORLD_COMM_GROUP, do_reshape, after_reshape_slice_shape)
    return _ALLGATHER_CELL


def destroy_allgather_cell():
    """Destroy AllGatherCell object."""
    global _ALLGATHER_CELL
    if _ALLGATHER_CELL:
        _ALLGATHER_CELL = None


def _chang_parallel_context(origin_dataset_strategy):
    """Change the original parallel state."""
    if context.get_context("mode") == context.GRAPH_MODE:
        context.set_auto_parallel_context(parallel_mode="hybrid_parallel")
        if origin_dataset_strategy != "data_parallel":
            context.set_auto_parallel_context(dataset_strategy="data_parallel")


def _restore_parallel_context(origin_parallel_mode, origin_dataset_strategy):
    """Restore the original parallel state."""
    if context.get_context("mode") == context.GRAPH_MODE:
        context.set_auto_parallel_context(parallel_mode=origin_parallel_mode)
        if origin_dataset_strategy != "data_parallel":
            if origin_dataset_strategy is not None and isinstance(origin_dataset_strategy, list):
                origin_dataset_strategy = tuple(tuple(ds_item) for ds_item in origin_dataset_strategy)
            context.set_auto_parallel_context(dataset_strategy=origin_dataset_strategy)


def _get_group_name(group_map, group):
    """get group name"""
    group_name = str(group)
    is_manual_communication_group = True
    if group_map:
        for name, rank_list in group_map.items():
            if list(group) == rank_list:
                group_name = name
                is_manual_communication_group = False
                break
    if is_manual_communication_group:
        create_group(str(group), list(group))
    return group_name, is_manual_communication_group


def _single_parameter_broadcast(net, layout, cur_rank=0, initial_rank=0):
    """
    Broadcast single parameter to other rank in data parallel dimension.
    """
    from mindspore import Tensor
    origin_parallel_mode = context.get_auto_parallel_context("parallel_mode")
    origin_dataset_strategy = context.get_auto_parallel_context("dataset_strategy")
    if layout:
        param_redundancy = get_parameter_redundancy(layout, initial_rank)
    else:
        param_redundancy = get_parameter_redundancy(net)
    if not param_redundancy:
        return
    single_params = remove_param_redundancy(param_redundancy)
    if not single_params:
        return
    param_redundancy_reversed = {}
    for key, redundancy in param_redundancy.items():
        for item in redundancy:
            if len(item) == 1:
                continue
            if cur_rank in item:
                param_redundancy_reversed.setdefault(item, []).append(key)
    if not param_redundancy_reversed or cur_rank not in single_params:
        return
    net_param_dict = net.parameters_dict()
    _chang_parallel_context(origin_dataset_strategy)
    group_map = _get_group_map()
    for group, params in param_redundancy_reversed.items():
        group_name, is_manual_communication_group = _get_group_name(group_map, group)
        allreduce_input = []
        for param in params:
            if param not in net_param_dict:
                continue
            real_param = net_param_dict[param]
            if param not in single_params[cur_rank]:
                real_param.set_data(Tensor(np.zeros(real_param.shape), dtype=real_param.dtype), real_param.sliced)
            allreduce_input.append(real_param)
        if not allreduce_input:
            continue
        communicator = SingleCommunicator(group_name)
        for real_param in allreduce_input:
            real_param.set_data(communicator(real_param), real_param.sliced)
        if is_manual_communication_group:
            destroy_group(group_name)
    _restore_parallel_context(origin_parallel_mode, origin_dataset_strategy)
