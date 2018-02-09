# -*- coding=utf-8 -*-  
import threadpool  
import time  
import requests 
  
urls = [  
    'http://www.163.com',  
    'http://www.sohu.com',  
    'http://www.ebay.com',  
    'http://www.sina.com.cn',  
    'http://www.baidu.com'  
]  
  
def myRequest(url):  
    rsp = requests.get(url)  
    print(url, rsp.status_code)
  
  
def timeCost(request, n):  
    print("Elapsed time: %s" % (time.time()-start)) 
  
start = time.time()  
pool = threadpool.ThreadPool(5)  
reqs = threadpool.makeRequests(myRequest, urls, timeCost)  
[ pool.putRequest(req) for req in reqs ]  
pool.wait()  