__author__ = 'Terry'
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import io
import sys
import importlib
importlib.reload(sys)
import re

str1 = "ACGCY.ME  密码: as5p "
print(re.findall(r"密码: (.+?) ",str1))

str2 = 'ACGCY.ME  密码:as5p'
a = re.findall('密码: *(\w*?)',str2)
print(a)
print(len(a))
print(a[0])
#print(len(a[0]))

b = re.search('密码:(\w+?)',str2,re.S)
print(b.group(1))

c = str2.index(':') + 1
print(c)
print(str2[c:])

c = str2.find('x') + 1
print(c)
print(str2[c:])
