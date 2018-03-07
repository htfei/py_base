__author__ = 'Terry'
# -*- coding:utf-8 -*-
import requests

'''
#带参数的请求实例：
r = requests.post('http://www.itwhy.org/wp-comments-post.php', data={'comment': '测试POST'})    #POST参数实例
print(r.text)
'''


#POST发送JSON数据：
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.json())
r = requests.post(url, json=payload)
print(r.json())
print(r.json()["documentation_url"])
data = r.json()
print(data["documentation_url"])

'''
#定制header：
import json

data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)
'''

'''
#可以修改其编码让 r.text 使用自定义的编码进行解码
r = requests.get('http://www.itwhy.org')
print(r.text, '\n{}\n'.format('*'*79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)
'''


'''
URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
try:
    r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
    r.raise_for_status()    # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)
else:
    result = r.json()
    print(type(result), result, sep='\n')
'''

#上传文件
#把字符串当着文件进行上传
'''
r = requests.get('https://github.com/timeline.json')
print(r.json())

'''

