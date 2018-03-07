__author__ = 'Terry'

#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求

req = urllib2.Request("http://www.baidu.com/")
res = urllib2.urlopen(req)
html = res.read()
res.close()

html = unicode(html, "gb2312").encode("utf8")
print html