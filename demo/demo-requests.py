
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码


import chardet
import urllib.request
res = urllib.request.urlopen('http://dict.baidu.com/s?wd=python')
htmlBytes = res.read()
# print(htmlBytes.decode('utf-8'))  # 中文乱码
typeEncode = sys.getfilesystemencoding()  ##系统默认编码
infoencode = chardet.detect(htmlBytes)  ##通过第3方模块来自动提取网页的编码
html = htmlBytes.decode(infoencode).encode(typeEncode)  ##先转换成unicode编码，然后转换系统编码输出
print(html)


'''
import requests
r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
print(r.encoding)
print('==========')
print(r.content)
print('==========')
print(r.text) #打印解码后的返回数据
'''