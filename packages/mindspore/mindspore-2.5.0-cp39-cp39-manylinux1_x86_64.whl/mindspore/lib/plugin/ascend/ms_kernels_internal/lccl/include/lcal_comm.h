/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2023. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#ifndef LCAL_COMM_H
#define LCAL_COMM_H

#include <vector>
#include <string>
#include <unordered_map>

#include <lcal_types.h>
#include <hccl.h>

namespace Lcal {
constexpr int IPC_NAME_SIZE = 65;
class LcalSockExchange;
class LcalComm {
public:
    LcalComm(int rank, int rankSize);
    LcalComm(int rank, int rankSize, std::vector<int> &rankList);
    ~LcalComm();
    LcalComm(const LcalComm &) = delete;
    LcalComm &operator=(const LcalComm &) = delete;
    int Init(const std::string &uid = "", int maxBuffSize = LCAL_BUFF_BYTES);
    int InitThread();
    int GetRank() const;
    int GetRankSize() const;
    const PhysicalInfo &GetPhysicalInfo() const;
    friend class Lccl;
    friend class Lcoc;

private:
    int SetIpcPid(const char *name, const uint32_t *pids) const;
    int OpenIpcMem(const char names[LCAL_MAX_RANK_SIZE][IPC_NAME_SIZE]);
    int GetDev();
    int GetDevThread();
    int EnablePeerAccess();
    int InitCommMem(int maxBuffSize);
    int InitCommon();
    void FreePeerMem(int8_t *&mem);
    int InitMem(int maxBuffSize);
    int GetPid(uint32_t *pids);
    int GetName(const char *name, char names[LCAL_MAX_RANK_SIZE][IPC_NAME_SIZE]);

private:
    std::string shmName_ = "lccl";
    int rank_ = 0;
    int rankSize_ = 0;
    int devId_ = 0;
    int64_t magic_ = 1;
    bool inited_ = false;
    std::vector<int> devList_ = {};
    std::vector<int> rankList_ = {};
    int8_t *peerMem_[LCAL_MAX_RANK_SIZE] = {}; // shared ping pong buff
    std::unordered_map<std::string, const char *> kernelNameMap_;
    PhysicalInfo physicalInfo_ = {};
    bool deterministic_ = false;
    LcalSockExchange *socketExchange_ = nullptr;
};
} // Lcal

#endif // LCAL_COMM_H
