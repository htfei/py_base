#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

# 打开文件
path = "D:/projects/"
dirs = os.listdir(path) # 1
dirs = os.listdir() # 2
# 输出所有文件和文件夹
for file in dirs:
    print(file)
