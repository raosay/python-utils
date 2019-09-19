# -*- coding:utf-8 -*-

import os
import re
import sys, getopt


def rename(source, target, path):
    if not os.path.exists(path):
        print('请输入文件路径')
    for dirMap in os.walk(path):
        for dirName in dirMap[1]:
            dirPath = dirMap[0] + "/" + dirName
            if source == dirName:
                replacePath = dirMap[0] + "/" + target
                # print('dir' + replacePath)
                os.replace(dirPath, replacePath)
        # 文件的话 只需要确认java文件，打开修改里面的package路径即可
        for fileName in dirMap[2]:
            filePath = dirMap[0] + "/" + fileName
            if '.java' in fileName:
                fileData = ""
                with open(filePath, 'r', encoding='utf-8') as f:
                    for line in f:
                        print(line)
                        if 'package com.bench.app.kk.platform.worker.web.base' in line:
                            line = line.replace('package com.bench.app.kk.platform.worker.web.base',
                                                'package com.bench.app.kk.platform.partner.web.base')
                        fileData += line
                with open(filePath, 'w', encoding='utf-8') as w:
                    w.write(fileData)





if __name__ == '__main__':
    rename('worker', 'partner', '/program/bench_source/kk.platform.worker.web.base/test')
