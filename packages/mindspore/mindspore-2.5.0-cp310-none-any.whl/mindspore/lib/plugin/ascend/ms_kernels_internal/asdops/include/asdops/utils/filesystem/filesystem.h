/*
 * Copyright (c) 2024 Huawei Technologies Co., Ltd.
 * AscendOpCommonLib is licensed under Mulan PSL v2.
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *          http://license.coscl.org.cn/MulanPSL2
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
 */
#ifndef COMMON_FILESYSTEM_FILESYSTEM_H
#define COMMON_FILESYSTEM_FILESYSTEM_H
#include <string>
#include <vector>
#include <sys/stat.h>
namespace AsdOps {
constexpr int64_t MAX_FILE_SIZE = 10737418240;   // 10737418240 即10GB
constexpr int64_t MAX_FILE_NUM = 100;
constexpr mode_t FILE_MODE = S_IRUSR | S_IWUSR | S_IRGRP;
class FileSystem {
public:
    static void GetDirChildItems(const std::string &dirPath, std::vector<std::string> &itemPaths);
    static void GetDirChildFiles(const std::string &dirPath, std::vector<std::string> &filePaths);
    static void GetDirChildDirs(const std::string &dirPath, std::vector<std::string> &dirPaths);
    static bool Exists(const std::string &path);
    static bool IsDir(const std::string &path);
    static std::string Join(const std::vector<std::string> &paths);
    static int64_t FileSize(const std::string &filePath);
    static std::string BaseName(const std::string &filePath);
    static std::string DirName(const std::string &path);
    static bool ReadFile(const std::string &filePath, char *buffer, uint64_t bufferSize);
    static bool WriteFile(const void *codeBuf, uint64_t codeLen, const std::string &filePath,
                          const mode_t mode = FILE_MODE);
    static void DeleteFile(const std::string &filePath);
    static bool Rename(const std::string &filePath, const std::string &newFilePath);
    static bool MakeDir(const std::string &dirPath, int mode);
    static bool Makedirs(const std::string &dirPath, const mode_t mode);
    static std::string PathCheckAndRegular(const std::string &path, bool symlinkCheck = true);

private:
    static bool IsSymLink(const std::string& filePath);
    static void GetDirChildItemsImpl(const std::string &dirPath, bool matchFile, bool matchDir,
                                     std::vector<std::string> &itemPaths);
};
} // namespace AsdOps
#endif