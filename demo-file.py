__author__ = 'Terry'
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# atom中运行 python 目录有问题，提示打不开，pycharm中正常。

import io
import sys
import importlib
importlib.reload(sys)

# 打开一个文件
fo = open("foo.txt", "r+")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

#read()方法
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
print("当前文件位置 : ", position)
str = fo.read()
print("重新读取字符串 : ", str)

# 关闭打开的文件
fo.close()


# 目录操作
import os

# 创建目录
# os.mkdir("testdir")
# 创建多级目录
os.makedirs(r"python\test2")  # 左右斜杠均可， os.makedirs(r"python/test3")
os.makedirs(r"C:/python/test3")  # 盘符默认当前盘， os.makedirs(r"/python/test3")

# 打开一个文件
fo = open("testdir/foo.txt", "w+")

