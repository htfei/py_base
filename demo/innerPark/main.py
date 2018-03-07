# coding=utf-8
'''
# 0、Python语言HelloWorld
print("hello python!")

# 1、定义变量
a = 2
b = 3
c = a+b
print(c)

# 2、判断语句
if c > 6:
    print("你好！")
elif c < 6:
    print("hello python!" )

# 3、循环
for i in range(0, 3):
    print("nihao {0},{1}".format(i,"gepi"))

# 4、定义函数
# 5、面向对象
# 6、引入Python文件1
import mylib
h = mylib.Hello('李四')
h.sayhello()
# h.sayhi()  #error


# 6、引入Python文件2
from mylib import Hello, Hi

h = Hello(10)
h.sayhello()

h1 = Hi("张三")
h1.sayhi()
h1.sayhello()

'''

import time

a = time.time()
print(str(a))
print(str(int(a)))
print(u'当前系统时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a)))
