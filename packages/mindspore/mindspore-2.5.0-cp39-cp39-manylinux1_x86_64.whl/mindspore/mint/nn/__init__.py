# Copyright 2024 Huawei Technologies Co., Ltd
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
"""
Neural Networks Cells.

Predefined building blocks or computing units to construct neural networks.
"""
from __future__ import absolute_import
import mindspore.ops as ops
from mindspore.mint.nn import functional as F
from mindspore.nn.cell import Cell
from mindspore.nn import EmbeddingExt as Embedding, MaxPool2dExt as MaxPool2d, LayerNormExt as LayerNorm, Linear
import mindspore.nn as nn

# 1

# 2

# 3
from mindspore.nn.layer.basic import Identity
# 4

# 5
from mindspore.mint.nn.layer.padding import (
    ConstantPad1d, ConstantPad2d, ConstantPad3d,
    ZeroPad1d, ZeroPad2d, ZeroPad3d,
    ReflectionPad1d, ReflectionPad2d, ReflectionPad3d,
    ReplicationPad1d, ReplicationPad2d, ReplicationPad3d
)

# 6
from mindspore.nn.layer.basic import UnfoldExt as Unfold
# 7
from mindspore.nn.layer.basic import Fold
# 8
from mindspore.nn.layer.activation import SoftmaxExt as Softmax
# 9
from mindspore.nn.layer.basic import UpsampleExt as Upsample
# 10

# 11
from mindspore.nn.layer import ReLU

# 12

# 13

# 14
from mindspore.nn.layer.basic import DropoutExt as Dropout
# 15
from mindspore.mint.nn.layer.conv import Conv2d, ConvTranspose2d
from mindspore.mint.nn.layer.conv import Conv3d
# 16
from mindspore.nn.layer import LogSoftmaxExt as LogSoftmax
# 17

# 18
from mindspore.nn.layer import PReLUExt as PReLU
# 19

# 20

# 21

# 22

# 23

# 24

# 25

# 26

# 27

# 28

# 29

# 30

# 31

# 32

# 33

# 34

# 35

# 36

# 37

# 38

# 39

# 40
from mindspore.mint.nn.layer.normalization import GroupNorm
from mindspore.mint.nn.layer.normalization import LayerNorm
from mindspore.mint.nn.layer.normalization import SyncBatchNorm
# 41

# 42

# 43

# 44

# 45

# 46
from mindspore.mint.nn.layer.activation import SiLU, LogSigmoid

# 47

# 48

# 49

# 50

# 51

# 52

# 53

# 54

# 55

# 56

# 57

# 58

# 59

# 60

# 61

# 62

# 63

# 64

# 65

# 66

# 67

# 68

# 69

# 70

# 71

# 72

# 73

# 74

# 75

# 76

# 77

# 78

# 79

# 80

# 81

# 82

# 83

# 84

# 85

# 86

# 87

# 88

# 89

# 90

# 91

# 92

# 93

# 94

# 95

# 96

# 97

# 98
from mindspore.nn.layer import AvgPool1dExt as AvgPool1d
# 99
from mindspore.nn.layer import AvgPool2dExt as AvgPool2d
# 100
from mindspore.nn.layer import SoftShrink as Softshrink
# 152
from mindspore.mint.nn.layer.pooling import AdaptiveAvgPool3d
# 159

# 220
from mindspore.nn.layer import HShrink as Hardshrink
# 221
from mindspore.nn.layer import HSigmoid as Hardsigmoid
# 222
from mindspore.nn.layer import HSwish as Hardswish
# 238
from mindspore.nn.loss import L1LossExt as L1Loss

# 254
from mindspore.mint.nn.layer.pooling import MaxUnpool2d

# 257

# 258
from mindspore.ops.function.nn_func import mse_loss_ext

# 393
from mindspore.mint.nn.layer.basic import Dropout2d

# 406
from mindspore.mint.nn.layer.activation import ELU

# 407
from mindspore.mint.nn.layer.basic import Flatten

# 421
from mindspore.mint.nn.layer.activation import Tanh

# 536
from mindspore.mint.nn.layer.activation import GLU

# 674
from mindspore.mint.nn.layer.normalization import BatchNorm1d

# 675
from mindspore.mint.nn.layer.normalization import BatchNorm2d

# 676
from mindspore.mint.nn.layer.normalization import BatchNorm3d

from mindspore.mint.nn.layer.pooling import AdaptiveAvgPool1d

from mindspore.mint.nn.layer.pooling import AdaptiveAvgPool2d

from mindspore.ops.function.nn_func import cross_entropy_ext as cross_entropy

from mindspore.ops.function.nn_func import _nllloss_nd as nllloss


class NLLLoss(Cell):
    r"""
    Gets the negative log likelihood loss between inputs and target.

    The nll loss with reduction=none can be described as:

    .. math::

        \ell(x, t)=L=\left\{l_{1}, \ldots, l_{N}\right\}^{\top},
        \quad l_{n}=-w_{t_{n}} x_{n, t_{n}},
        \quad w_{c}=\text { weight }[c] \cdot \mathbb{1}
        \{c \not= \text{ignore_index}\},

    where :math:`x` is the inputs, :math:`t` is the target, :math:`w` is the weight,
    :math:`N` is the batch size, :math:`c` belonging to :math:`[0, C-1]` is class index,
    where :math:`C` is the number of classes.

    If `reduction` is not ``None`` (default ``'mean'``), then

    .. math::

        \ell(x, t)=\left\{\begin{array}{ll}
        \sum_{n=1}^{N} \frac{1}{\sum_{n=1}^{N} w_{t n}} l_{n}, & \text { if reduction }=\text { 'mean', } \\
        \sum_{n=1}^{N} l_{n}, & \text { if reduction }=\text { 'sum' }
        \end{array}\right.

    .. warning::
        This is an experimental API that is subject to change or deletion.

    Args:
        weight (Tensor, optional): A rescaling weight applied to the loss of each batch element.
            If not None, the shape is :math:`(C,)`, data type must be float16 or float32 or bfloat16(only supported by
            Atlas A2 training series products). It should have the same data type as `input` . Default: ``None`` .
        ignore_index (int, optional): Specifies a target value that is ignored and does not contribute to the input
            gradient. Only valid in class indices, please set it to a negative number in probabilities.
            Default: ``-100`` .
        reduction (str, optional): Apply specific reduction method to the output: ``'none'`` , ``'mean'`` ,
            ``'sum'`` . Default: ``'mean'`` .

            - ``'none'``: no reduction will be applied.
            - ``'mean'``: compute and return the weighted mean of elements in the output.
            - ``'sum'``: the output elements will be summed.

    Inputs:
        - **input** (Tensor) - :math:`(N)` or :math:`(N, C)` where `C = number of classes` , `N = batch size` ,
          or :math:`(N, C, d_1, d_2, ..., d_K)` (for high-dimensional data).
          `input` is expected to be log-probabilities, data type must be float16 or float32 or bfloat16(only supported
          by Atlas A2 training series products).
        - **target** (Tensor) - :math:`()` or :math:`(N)` ,
          where the value range is :math:`[0, C-1]`, or :math:`(N, d_1, d_2, ..., d_K)` for
          high-dimensional loss, data type must be int32 or int64 or uint8.

    Outputs:
        Tensor, the data type is the same as `input` .

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> import numpy as np
        >>> from mindspore import Tensor, ops
        >>> inputs = mindspore.Tensor(np.random.randn(3, 5), mindspore.float32)
        >>> target = mindspore.Tensor(np.array([1, 0, 4]), mindspore.int32)
        >>> op = mindspore.mint.nn.NLLLoss()
        >>> output = op(inputs, target)

    """

    def __init__(self, weight=None, ignore_index=-100, reduction='mean'):
        super(NLLLoss, self).__init__()
        self.weight = weight
        self.ignore_index = ignore_index
        self.reduction = reduction

    def construct(self, input, target):
        out = nllloss(input, target, self.weight, self.ignore_index, self.reduction)
        return out


class CrossEntropyLoss(Cell):
    r"""
    The cross entropy loss between input and target.

    The cross entropy supports two kind of targets:

    - Class indices (int) in the range :math:`[0, C)` where :math:`C` is the number of classes,
      the loss with reduction=none can be described as:

      .. math::

          \ell(x, y) = L = \{l_1,\dots,l_N\}^\top, \quad
          l_n = - w_{y_n} \log \frac{\exp(x_{n,y_n})}{\sum_{c=1}^C \exp(x_{n,c})}
          \cdot \mathbb{1}\{y_n \not= \text{ignore_index}\}

      where :math:`x` is the inputs, :math:`y` is the target, :math:`w` is the weight, :math:`N` is the batch size,
      :math:`c` belonging to :math:`[0, C-1]` is class index, where :math:`C` is the number of classes.

      If `reduction` is not ``None`` (default ``'mean'`` ), then

      .. math::

          \ell(x, y) = \begin{cases}
              \sum_{n=1}^N \frac{1}{\sum_{n=1}^N w_{y_n} \cdot \mathbb{1}\{y_n \not= \text{ignore_index}\}} l_n, &
              \text{if reduction} = \text{'mean',}\\
              \sum_{n=1}^N l_n,  &
              \text{if reduction} = \text{'sum'.}
              \end{cases}

    - Probabilities (float) for each class, useful when labels beyond a single class per minibatch item
      are required, the loss with reduction=none can be described as:

      .. math::

          \ell(x, y) = L = \{l_1,\dots,l_N\}^\top, \quad
          l_n = - \sum_{c=1}^C w_c \log \frac{\exp(x_{n,c})}{\sum_{i=1}^C \exp(x_{n,i})} y_{n,c}

      where :math:`x` is the inputs, :math:`y` is the target, :math:`w` is the weight, N is the batch size,
      :math:`c` belonging to :math:`[0, C-1]` is class index, where :math:`C` is the number of classes.

      If `reduction` is not ``None`` (default ``'mean'`` ), then

      .. math::

          \ell(x, y) = \begin{cases}
              \frac{\sum_{n=1}^N l_n}{N}, &
              \text{if reduction} = \text{'mean',}\\
              \sum_{n=1}^N l_n,  &
              \text{if reduction} = \text{'sum'.}
              \end{cases}

    .. warning::
            This is an experimental API that is subject to change or deletion.

    Note:
        Dynamic shape, dynamic rank and variable constant input are not supported in `strict graph mode
        (jit_syntax_level=mindspore.STRICT)
        <https://www.mindspore.cn/docs/en/master/model_train/program_form/static_graph.html>`_.

    Args:
        weight (Tensor, optional): A rescaling weight applied to the loss of each batch element.
            If not None, the shape is :math:`(C,)`, data type must be float16 or float32 or bfloat16(only supported by
            Atlas A2 training series products). Default: ``None`` .
        ignore_index (int, optional): Specifies a target value that is ignored and does not contribute to the input
            gradient. Only valid in class indices, please set it to a negative number in probabilities.
            Default: ``-100`` .
        reduction (str, optional): Apply specific reduction method to the output: ``'none'`` , ``'mean'`` ,
            ``'sum'`` . Default: ``'mean'`` .

            - ``'none'``: no reduction will be applied.
            - ``'mean'``: compute and return the weighted mean of elements in the output.
            - ``'sum'``: the output elements will be summed.

        label_smoothing (float, optional): Label smoothing values, a regularization tool used to prevent the model
            from overfitting when calculating Loss. The value range is [0.0, 1.0]. Default: ``0.0`` .

    Inputs:
        - **input** (Tensor) - :math:`(N)` or :math:`(N, C)` where `C = number of classes` or :math:`(N, C, H, W)`
          in case of 2D Loss, or :math:`(N, C, d_1, d_2, ..., d_K)`.
          `input` is expected to be log-probabilities, data type must be float16 or float32 or bfloat16(only supported
          by Atlas A2 training series products).
        - **target** (Tensor) - For class indices, tensor of shape :math:`()`, :math:`(N)` or
          :math:`(N, d_1, d_2, ..., d_K)` , data type must be int32 or int64. For probabilities, tensor of shape
          :math:`(N,)` , :math:`(N, C)` or :math:`(N, C, d_1, d_2, ..., d_K)` , data type must be float16 or float32
          or bfloat16(only supported by Atlas A2 training series products).

    Outputs:
        Tensor, the data type is the same as `input` .

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore as ms
        >>> import numpy as np
        >>> # Case 1: Indices labels
        >>> inputs = ms.Tensor(np.random.randn(3, 5), ms.float32)
        >>> target = ms.Tensor(np.array([1, 0, 4]), ms.int32)
        >>> op = ms.mint.nn.CrossEntropyLoss()
        >>> output = op(inputs, target)
        >>> # Case 2: Probability labels
        >>> inputs = ms.Tensor(np.random.randn(3, 5), ms.float32)
        >>> target = ms.Tensor(np.random.randn(3, 5), ms.float32)
        >>> op = ms.mint.nn.CrossEntropyLoss()
        >>> output = op(inputs, target)
    """

    def __init__(self, weight=None, ignore_index=-100, reduction='mean', label_smoothing=0.0):
        super(CrossEntropyLoss, self).__init__()
        self.weight = weight
        self.ignore_index = ignore_index
        self.reduction = reduction
        self.label_smoothing = label_smoothing

    def construct(self, input, target):
        out = cross_entropy(input, target, self.weight, self.ignore_index, self.reduction, self.label_smoothing)
        return out


class BCEWithLogitsLoss(Cell):
    r"""
    Adds sigmoid activation function to `input` as logits, and uses this logits to compute binary cross entropy
    between the logits and the target.

    Sets input `input` as :math:`X`, input `target` as :math:`Y`, output as :math:`L`. Then,

    .. math::
        p_{ij} = sigmoid(X_{ij}) = \frac{1}{1 + e^{-X_{ij}}}

    .. math::
        L_{ij} = -[Y_{ij} \cdot \log(p_{ij}) + (1 - Y_{ij}) \cdot \log(1 - p_{ij})]

    Then,

    .. math::
        \ell(x, y) = \begin{cases}
        L, & \text{if reduction} = \text{'none';}\\
        \operatorname{mean}(L), & \text{if reduction} = \text{'mean';}\\
        \operatorname{sum}(L),  & \text{if reduction} = \text{'sum'.}
        \end{cases}

    Args:
        weight (Tensor, optional): A rescaling weight applied to the loss of each batch element.
            If not None, it can be broadcast to a tensor with shape of `target`, data type must be float16, float32 or
            bfloat16(only Atlas A2 series products are supported). Default: ``None`` .
        reduction (str, optional): Apply specific reduction method to the output: ``'none'`` , ``'mean'`` ,
            ``'sum'`` . Default: ``'mean'`` .

            - ``'none'``: no reduction will be applied.
            - ``'mean'``: compute and return the weighted mean of elements in the output.
            - ``'sum'``: the output elements will be summed.

        pos_weight (Tensor, optional): A weight of positive examples. Must be a vector with length equal to the
            number of classes. If not None, it must be broadcast to a tensor with shape of `input`, data type
            must be float16, float32 or bfloat16(only Atlas A2 series products are supported). Default: ``None`` .

    Inputs:
        - **input** (Tensor) - Input `input` with shape :math:`(N, *)` where :math:`*` means, any number
          of additional dimensions. The data type must be float16, float32 or bfloat16(only Atlas A2 series products
          are supported).
        - **target** (Tensor) - Ground truth label with shape :math:`(N, *)` where :math:`*` means, any number
          of additional dimensions. The same shape and data type as `input`.

    Outputs:
        Tensor or Scalar, if `reduction` is ``'none'``, its shape is the same as `input`.
        Otherwise, a scalar value will be returned.

    Raises:
        TypeError: If input `input` or `target` is not Tensor.
        TypeError: If `weight` or `pos_weight` is a parameter.
        TypeError: If data type of `reduction` is not string.
        ValueError: If `weight` or `pos_weight` can not be broadcast to a tensor with shape of `input`.
        ValueError: If `reduction` is not one of ``'none'``, ``'mean'``, ``'sum'``.

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore as ms
        >>> from mindspore import mint
        >>> import numpy as np
        >>> input = ms.Tensor(np.array([[-0.8, 1.2, 0.7], [-0.1, -0.4, 0.7]]).astype(np.float32))
        >>> target = ms.Tensor(np.array([[0.3, 0.8, 1.2], [-0.6, 0.1, 2.2]]).astype(np.float32))
        >>> loss = mint.nn.BCEWithLogitsLoss()
        >>> output = loss(input, target)
        >>> print(output)
        0.3463612
    """

    def __init__(self, weight=None, reduction='mean', pos_weight=None):
        super(BCEWithLogitsLoss, self).__init__()
        self.bce_with_logits = ops.auto_generate.BCEWithLogitsLoss(reduction)
        self.weight = weight
        self.pos_weight = pos_weight

    def construct(self, input, target):
        out = self.bce_with_logits(input, target, self.weight, self.pos_weight)
        return out


class SELU(Cell):
    r"""
    Activation function SELU (Scaled exponential Linear Unit).

    Refer to :func:`mindspore.mint.nn.functional.selu` for more details.

    SELU Activation Function Graph:

    .. image:: ../images/SeLU.png
        :align: center

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, mint
        >>> import numpy as np
        >>> input = Tensor(np.array([[-1.0, 4.0, -8.0], [2.0, -5.0, 9.0]]), mindspore.float32)
        >>> selu = mint.nn.SELU()
        >>> output = selu(input)
        >>> print(output)
        [[-1.1113307 4.202804 -1.7575096]
        [ 2.101402 -1.7462534 9.456309 ]]
    """

    def __init__(self):
        """Initialize SELU"""
        super(SELU, self).__init__()

    def construct(self, input):
        return F.selu(input)


class GELU(Cell):
    r"""
    Activation function GELU (Gaussian Error Linear Unit).

    Refer to :func:`mindspore.mint.nn.functional.gelu` for more details.

    GELU Activation Function Graph:

    .. image:: ../images/GELU.png
        :align: center

    Supported Platforms:
        ``Ascend`` ``GPU`` ``CPU``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, mint
        >>> import numpy as np
        >>> input = Tensor(np.array([[-1.0, 4.0, -8.0], [2.0, -5.0, 9.0]]), mindspore.float32)
        >>> gelu = mint.nn.GELU()
        >>> output = gelu(input)
        >>> print(output)
        [[-1.5880802e-01  3.9999299e+00 -3.1077917e-21]
         [ 1.9545976e+00 -2.2918017e-07  9.0000000e+00]]
    """

    def __init__(self):
        """Initialize GELU"""
        super(GELU, self).__init__()

    def construct(self, input):
        return F.gelu(input)


class Hardtanh(Cell):
    r"""
    Activation function Hardtanh.

    Refer to :func:`mindspore.mint.nn.functional.hardtanh` for more details.

    Hardtanh Activation Function Graph:

    .. image:: ../images/Hardtanh.png
        :align: center

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, mint
        >>> import numpy as np
        >>> input = Tensor(np.array([-1, -2, 0, 2, 1]), mindspore.float32)
        >>> hardtanh = mint.nn.Hardtanh(min_val=-1.0, max_val=1.0)
        >>> output = hardtanh(x)
        >>> print(output)
        [-1. -1.  0.  1.  1.]
    """

    def __init__(self, min_val=-1.0, max_val=1.0, inplace=False):
        """Initialize ReLU6"""
        super(Hardtanh, self).__init__()
        self.min_val = min_val
        self.max_val = max_val
        self.inplace = inplace

    def construct(self, input):
        if self.inplace:
            return F.hardtanh_(input, self.min_val, self.max_val)
        return F.hardtanh_op(input, self.min_val, self.max_val)


class ReLU6(Cell):
    r"""
    Activation function ReLU6.

    .. warning::
        This is an experimental API that is subject to change or deletion.

    Refer to :func:`mindspore.mint.nn.functional.relu6` for more details.

    ReLU6 Activation Function Graph:

    .. image:: ../images/ReLU6.png
        :align: center

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, mint
        >>> import numpy as np
        >>> input = Tensor(np.array([[-1.0, 4.0, -8.0], [2.0, -5.0, 9.0]]), mindspore.float32)
        >>> relu6 = mint.nn.ReLU6()
        >>> output = relu6(input)
        >>> print(output)
        [[0. 4. 0.]
        [2. 0. 6.]]
    """

    def __init__(self, inplace=False):
        """Initialize ReLU6"""
        super(ReLU6, self).__init__()
        self.inplace = inplace

    def construct(self, input):
        return F.relu6(input, self.inplace)


class Mish(Cell):
    r"""
    Computes MISH (A Self Regularized Non-Monotonic Neural Activation Function)
    of input tensors element-wise.

    Refer to :func:`mindspore.mint.nn.functional.mish` for more details.

    Mish Activation Function Graph:

    .. image:: ../images/Mish.png
        :align: center

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, mint
        >>> import numpy as np
        >>> x = Tensor(np.array([[-1.1, 4.0, -8.0], [2.0, -5.0, 9.0]]), mindspore.float32)
        >>> mish = mint.nn.Mish()
        >>> output = mish(x)
        >>> print(output)
        [[-3.0764845e-01 3.9974124e+00 -2.6832507e-03]
         [ 1.9439589e+00 -3.3576239e-02 8.9999990e+00]]
    """

    def __init__(self):
        """Initialize Mish."""
        super(Mish, self).__init__()

    def construct(self, input):
        return F.mish(input)


class MSELoss(Cell):
    r"""
    Calculates the mean squared error between the predicted value and the label value.

    For simplicity, let :math:`x` and :math:`y` be 1-dimensional Tensor with length :math:`N`,
    the unreduced loss (i.e. with argument reduction set to 'none') of :math:`x` and :math:`y` is given as:

    .. math::
        \ell(x, y) = L = \{l_1,\dots,l_N\}^\top, \quad \text{with} \quad l_n = (x_n - y_n)^2.

    where :math:`N` is the batch size. If `reduction` is not ``'none'``, then:

    .. math::
        \ell(x, y) =
        \begin{cases}
            \operatorname{mean}(L), & \text{if reduction} = \text{'mean';}\\
            \operatorname{sum}(L),  & \text{if reduction} = \text{'sum'.}
        \end{cases}

    Args:
        reduction (str, optional): Apply specific reduction method to the output: ``'none'`` , ``'mean'`` ,
            ``'sum'`` . Default: ``'mean'`` .

            - ``'none'``: no reduction will be applied.
            - ``'mean'``: compute and return the mean of elements in the output.
            - ``'sum'``: the output elements will be summed.

    Inputs:
        - **logits** (Tensor) - The predicted value of the input. Tensor of any dimension.
          The data type needs to be consistent with the `labels`. It should also be broadcastable with the `labels`.
        - **labels** (Tensor) - The input label. Tensor of any dimension.
          The data type needs to be consistent with the `logits`. It should also be broadcastable with the `logits`.

    Outputs:
        - Tensor. If `reduction` is ``'mean'`` or ``'sum'``, the shape of output is `Tensor Scalar`.
        - If reduction is ``'none'``, the shape of output is the broadcasted shape of `logits` and `labels` .

    Raises:
        ValueError: If `reduction` is not one of ``'mean'``, ``'sum'`` or ``'none'``.
        ValueError: If `logits` and `labels` are not broadcastable.
        TypeError: If `logits` and `labels` are in different data type.

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> from mindspore import Tensor, nn
        >>> import numpy as np
        >>> # Case 1: logits.shape = labels.shape = (3,)
        >>> loss = nn.MSELoss()
        >>> logits = Tensor(np.array([1, 2, 3]), mindspore.float32)
        >>> labels = Tensor(np.array([1, 1, 1]), mindspore.float32)
        >>> output = loss(logits, labels)
        >>> print(output)
        1.6666667
        >>> # Case 2: logits.shape = (3,), labels.shape = (2, 3)
        >>> loss = nn.MSELoss(reduction='none')
        >>> logits = Tensor(np.array([1, 2, 3]), mindspore.float32)
        >>> labels = Tensor(np.array([[1, 1, 1], [1, 2, 2]]), mindspore.float32)
        >>> output = loss(logits, labels)
        >>> print(output)
        [[0. 1. 4.]
         [0. 0. 1.]]
    """

    def __init__(self, reduction='mean'):
        super(MSELoss, self).__init__()
        self.mse_loss = mse_loss_ext
        self.reduction = reduction

    def construct(self, input, target):
        out = self.mse_loss(input, target, self.reduction)
        return out


class SmoothL1Loss(Cell):
    r"""
    Computes smooth L1 loss, a robust L1 loss.

    Refer to :func:`mindspore.mint.nn.functional.smooth_l1_loss` for more details.

    .. warning::
        This is an experimental API that is subject to change or deletion.

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore
        >>> import numpy as np
        >>> from mindspore import Tensor, mint
        >>> input = Tensor(np.array([2, 2, 3]), mindspore.float32)
        >>> target = Tensor(np.array([2, 2, 2]), mindspore.float32)
        >>> beta = 1.0
        >>> reduction_1 = 'none'
        >>> loss1 = mint.nn.SmoothL1Loss(reduction=reduction_1, beta=beta)
        >>> output = loss1(input, target)
        >>> print(output)
        [0.  0.  0.5]
        >>> reduction_2 = 'mean'
        >>> loss2 = mint.nn.SmoothL1Loss(reduction=reduction_2, beta=beta)
        >>> output = loss2(input, target)
        >>> print(output)
        0.16666667
        >>> reduction_3 = 'sum'
        >>> loss3 = mint.nn.SmoothL1Loss(reduction=reduction_3, beta=beta)
        >>> output = loss2(loss3, target)
        >>> print(output)
        0.5
    """

    def __init__(self, reduction='mean', beta=1.0):
        super(SmoothL1Loss, self).__init__()
        self.smooth_l1_loss = ops.function.smooth_l1_loss
        self.reduction = reduction
        self.beta = beta

    def construct(self, input, target):
        out = self.smooth_l1_loss(input, target, self.beta, self.reduction)
        return out


class BCELoss(Cell):
    r"""
    Compute the binary cross entropy between the true labels and predicted labels.

    Set the predicted labels as :math:`x`, true labels as :math:`y`, the output loss as :math:`\ell(x, y)`.
    The formula is as follow:

    .. math::
        L = \{l_1,\dots,l_n,\dots,l_N\}^\top, \quad
        l_n = - w_n \left[ y_n \cdot \log x_n + (1 - y_n) \cdot \log (1 - x_n) \right]

    where N is the batch size. Then,

    .. math::
        \ell(x, y) = \begin{cases}
        L, & \text{if reduction} = \text{'none';}\\
        \operatorname{mean}(L), & \text{if reduction} = \text{'mean';}\\
        \operatorname{sum}(L),  & \text{if reduction} = \text{'sum'.}
        \end{cases}

    .. note::
        Note that the predicted labels should always be the output of sigmoid. Because it is a two-class
        classification, the true labels should be numbers between 0 and 1.
        And if :math:`x_n` is either 0 or 1, one of the log terms would be mathematically undefined in the above loss
        equation.

    .. warning::
        This is an experimental API that is subject to change or deletion.

    Args:
        weight (Tensor, optional): A rescaling weight applied to the loss of each batch element.
            And it must have the same shape and data type as `inputs`. Default: ``None`` .
        reduction (str, optional): Apply specific reduction method to the output: ``'none'`` , ``'mean'`` ,
            ``'sum'`` . Default: ``'mean'`` .

            - ``'none'``: no reduction will be applied.
            - ``'mean'``: compute and return the weighted mean of elements in the output.
            - ``'sum'``: the output elements will be summed.

    Inputs:
        - **input** (Tensor) - The input tensor with shape :math:`(N, *)` where :math:`*` means, any number
          of additional dimensions. The data type must be float16 or float32 or bfloat16(only supported
          by Atlas A2 training series products).
        - **target** (Tensor) - The label tensor with shape :math:`(N, *)` where :math:`*` means, any number
          of additional dimensions. The same shape and data type as `input`.

    Outputs:
        Tensor, has the same dtype as `input`. if `reduction` is ``'none'``, then it has the same shape as `input`.
        Otherwise, it is a scalar Tensor.

    Raises:
        TypeError: If dtype of `input`, `target` or `weight` (if given) is not float16, float32 or bfloat16.
        ValueError: If `reduction` is not one of ``'none'``, ``'mean'``, ``'sum'``.
        ValueError: If shape of `input` is not the same as `target` or `weight` (if given).

    Supported Platforms:
        ``Ascend``

    Examples:
        >>> import mindspore as ms
        >>> from mindspore import nn
        >>> import numpy as np
        >>> weight = ms.Tensor(np.array([[1.0, 2.0, 3.0], [4.0, 3.3, 2.2]]), ms.float32)
        >>> loss = nn.BCELoss(weight=weight, reduction='mean')
        >>> input = ms.Tensor(np.array([[0.1, 0.2, 0.3], [0.5, 0.7, 0.9]]), ms.float32)
        >>> target = ms.Tensor(np.array([[0, 1, 0], [0, 0, 1]]), ms.float32)
        >>> output = loss(input, target)
        >>> print(output)
        1.8952923
    """

    def __init__(self, weight=None, reduction='mean'):
        super(BCELoss, self).__init__()
        self.bce_loss = nn.loss.BCELoss(weight, reduction)

    def construct(self, input, target):
        return self.bce_loss(input, target)


__all__ = [
    # 1
    'BCEWithLogitsLoss',
    # 2

    # 3
    'Identity',
    # 4

    # 5
    'ConstantPad1d',
    'ConstantPad2d',
    'ConstantPad3d',
    'ZeroPad1d',
    'ZeroPad2d',
    'ZeroPad3d',
    'ReflectionPad1d',
    'ReflectionPad2d',
    'ReflectionPad3d',
    'ReplicationPad1d',
    'ReplicationPad2d',
    'ReplicationPad3d',

    # 6
    'Fold',
    # 7
    'Unfold',
    # 8
    'Softmax',
    # 9
    'Upsample',
    # 10

    # 11
    'ReLU',

    # 12

    # 13

    # 14

    # 15
    'Conv2d',
    # 16
    'LogSoftmax',
    # 17
    'ConvTranspose2d',
    # 18
    'PReLU',
    # 19
    'Conv3d',
    # 20

    # 21

    # 22

    # 23

    # 24

    # 25

    # 26

    # 27

    # 28

    # 29

    # 30

    # 31

    # 32

    # 33

    # 34

    # 35

    # 36

    # 37

    # 38
    'Linear',
    # 39

    # 40
    'GroupNorm',

    # 41

    # 42

    # 43

    # 44

    # 45

    # 46
    'SiLU',

    # 47

    # 48

    # 49

    # 50

    # 51

    # 52

    # 53

    # 54

    # 55

    # 56

    # 57

    # 58

    # 59

    # 60

    # 61

    # 62

    # 63

    # 64
    'SyncBatchNorm',
    # 65

    # 66

    # 67

    # 68

    # 69

    # 70

    # 71

    # 72

    # 73

    # 74

    # 75

    # 76

    # 77

    # 78

    # 79

    # 80

    # 81

    # 82

    # 83

    # 84

    # 85

    # 86

    # 87

    # 88

    # 89

    # 90

    # 91

    # 92

    # 93

    # 94

    # 95

    # 96
    'AdaptiveAvgPool1d',

    # 97
    'AdaptiveAvgPool2d',

    # 98
    'AvgPool1d',
    # 99
    'AvgPool2d',
    # 100
    'SELU',
    # 152
    'AdaptiveAvgPool3d',
    # 159
    'GELU',
    # 220
    'Hardshrink',
    # 221
    'Hardsigmoid',
    # 222
    'Hardswish',
    # 238
    'L1Loss',
    # 254
    'MaxUnpool2d',
    # 267
    'Mish',
    # 258
    'MSELoss',
    # 259

    # 294
    'SmoothL1Loss',

    # 393
    'Dropout2d',
    # 406
    'ELU',
    # 407
    'Flatten',
    # 412
    'Hardtanh',
    'ReLU6',
    # 413
    'BCELoss',
    # 421
    'Tanh',

    # 556
    'LogSigmoid',
    # 674
    'BatchNorm1d',
    # 675
    'BatchNorm2d',
    # 676
    'BatchNorm3d',
]
