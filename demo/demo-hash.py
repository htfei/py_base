__author__ = 'Terry'
# -*- coding:utf-8 -*-
import hashlib

# 注意：需要以二进制方式打开，否则可能报错TypeError: Unicode-objects must be encoded before hashing
# 字符串前面加b,若为文件，则 open(myfile, "rb")
a = b"I am huoty"
print(hashlib.md5(a).hexdigest())
print(hashlib.sha1(a).hexdigest())
print(hashlib.sha224(a).hexdigest())
print(hashlib.sha256(a).hexdigest())
print(hashlib.sha384(a).hexdigest())
print(hashlib.sha512(a).hexdigest())

print(hashlib.algorithms)
