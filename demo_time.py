__author__ = 'Terry'
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# atom中运行 python 目录有问题，提示打不开，pycharm中正常。

import io
import sys
import importlib
importlib.reload(sys)
import time

a = time.time()
print(str(a))
print(str(int(a)))
print('当前系统时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)))
print('now date:' + time.strftime("%Y%m%d", time.localtime(time.time())))
