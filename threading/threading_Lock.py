# coding:utf-8
import threading
import time

lock = threading.RLock()
gl_num = 0
def show(arg):
    lock.acquire()

    global gl_num   
    gl_num +=1
    lock.release()

    print('threading',arg+1,'-->',gl_num) 
    time.sleep(1)

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')