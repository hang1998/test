#include <iostream>
#include <fstream>
#include <curl/curl.h>

// 回调函数，用于写入数据到文件
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    std::ofstream* ofs = static_cast<std::ofstream*>(userp);
    size_t totalSize = size * nmemb;
    ofs->write(static_cast<char*>(contents), totalSize);
    return totalSize;
}

int main() {
    // 下载文件的 URL
    const std::string url = "http://jx3hdv4qq-autoupdate.xoyocdn.com/jx3hd_v4/zhcn_hd/autoupdateentry.txt";
    // 本地文件路径
    const std::string localFilePath = "autoupdateentry.txt";

    // 初始化 libcurl
    CURL* curl;
    CURLcode res;
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if(curl) {
        std::ofstream ofs(localFilePath, std::ios::binary);
        if (!ofs.is_open()) {
            std::cerr << "无法打开文件进行写入: " << localFilePath << std::endl;
            return 1;
        }

        // 设置 URL 和回调函数
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &ofs);

        // 执行请求
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            std::cerr << "curl_easy_perform() 失败: " << curl_easy_strerror(res) << std::endl;
        }

        // 清理
        curl_easy_cleanup(curl);
        ofs.close();
    }

    curl_global_cleanup();

    // 读取文件内容并逐行输出
    std::ifstream ifs(localFilePath);
    if (!ifs.is_open()) {
        std::cerr << "无法打开文件进行读取: " << localFilePath << std::endl;
        return 1;
    }

    std::string link = "http://jx3hdv4qq-autoupdate.xoyocdn.com/jx3hd_v4/zhcn_hd/";
    std::string delimiter = "=";
    std::string startVersion = "jx3hd_v4_c_1.0.0.8778";
    std::string line;
    bool bStart = false;
    while (std::getline(ifs, line)) {
        if (line.rfind("Patch_", 0) == 0) { // 检查行是否以 "Patch_" 开始

            if (!bStart && std::string::npos != line.find(startVersion))
                bStart = true;
            
            if (!bStart)
                continue;
            
            size_t pos = line.find(delimiter);
            if (pos != std::string::npos) {
                std::string key = line.substr(0, pos);
                std::string value = line.substr(pos + 1);

                std::cout << link << value << std::endl;
            }
        }
    }

    ifs.close();
    return 0;
}
