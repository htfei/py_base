import time

# 获取当前的timestamp
timenow = int(round(time.time())) #round四舍五入
print(timenow)  #1520235837


# http://www.runoob.com/python/python-date-time.html
#
localtime = time.localtime(time.time())
print "本地时间为 :", localtime
# 本地时间为 : time.struct_time(tm_year=2018, tm_mon=12, tm_mday=21, tm_hour=18, tm_min=57, tm_sec=28, tm_wday=4, tm_yday=355, tm_isdst=0)
# 
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime
# 本地时间为 : Fri Dec 21 18:58:52 2018


>>> # 格式化成2016-03-20 11:45:39形式
... print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
2018-12-21 18:59:40
>>>
... # 格式化成Sat Mar 28 22:24:24 2016形式
... print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
Fri Dec 21 18:59:40 2018
>>>
... # 将格式字符串转换为时间戳
... a = "Sat Mar 28 22:24:24 2016"
>>> print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
1459175064.0





>>> import datetime
>>> i = datetime.datetime.now()
>>> print ("当前的日期和时间是 %s" % i)
当前的日期和时间是 2018-12-21 19:00:37.836000
>>> print ("ISO格式的日期和时间是 %s" % i.isoformat() )
ISO格式的日期和时间是 2018-12-21T19:00:37.836000
>>> print ("当前的年份是 %s" %i.year)
当前的年份是 2018
>>> print ("当前的月份是 %s" %i.month)
当前的月份是 12
>>> print ("当前的日期是  %s" %i.day)
当前的日期是  21
>>> print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
dd/mm/yyyy 格式是  21/12/2018
>>> print ("当前小时是 %s" %i.hour)
当前小时是 19
>>> print ("当前分钟是 %s" %i.minute)
当前分钟是 0
>>> print ("当前秒是  %s" %i.second)
当前秒是  37



