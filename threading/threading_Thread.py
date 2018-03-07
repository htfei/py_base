# coding:utf-8
import threading
import time
import random

#方法一：将要执行的方法作为参数传给Thread的构造方法
    # is/setDaemon(bool):   获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
    # join([timeout]):      阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
def action(arg):
    tm = random.randint(0,3)
    time.sleep(tm)
    print('thread %s ,sleep %d s \r' %(arg,tm)) # 若不对子线程进行管理，将导致共享资源使用混乱（此处为输出混乱）

thread_list = []    #线程存放列表
for i in range(4):
    t =threading.Thread(target=action,args=(i,))
    #t.setDaemon(True)   #设置线程为后台线程，此时主线程执行完毕后，后台线程不论成功与否，程序均停止。
    t.start() 
    #t.join()           #join不妥当的用法,阻挡了下一个线程的start(),使得“多线程”失去了多线程意义。
    thread_list.append(t)

for t in thread_list:
    t.join()
    print(threading.currentThread().getName())

print('main thread end!')
