# coding:utf-8
import threading
import time
import random
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    t = random.randint(0,5)
    time.sleep(t)
    print('thread %s ,sleep %d s \r' %(arg,t))

for i in range(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print('main thread end!')