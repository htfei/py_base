# coding=utf-8
#!/usr/bin/python

import hashlib
import hmac
import base64
import urllib.parse
import time

message = "GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Nonce=11886&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&SignatureMethod=HmacSHA256&Timestamp=1465185768".encode('utf-8')
secret = "Gu5t9xGARNpq86cd98joQYCN3Cozk1qA".encode('utf-8')

signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
print(signature)
# b'0EEm/HtGRr/VJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s='
signature2 = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha1).digest())
print(signature2)
# b'RVSD1I6ip2Zo56I2HdqRVrt+1TE='

#URL编码
SignatureURL = urllib.parse.quote(signature)
print(SignatureURL)
# b'0EEm/HtGRr/VJXTAD9tYMth1Bzm3lLHz5RCDv1GdM8s='


timenow = int(round(time.time()))
print(timenow)

#2. 生成签名串signature
SecretId = 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA'
SecretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA'
#2.1. 对参数排序
mydict = {
        'Action' : 'TextKeywords',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : SecretId,
        'Timestamp' : int(round(time.time())),
        'title': 'Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330',
        'content': 'Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330'
    }
#2.2. 拼接请求字符串
# 遍历dict并转化为url参数
def dict2url(mydict):
    s1 =''
    for k,v in mydict.items():
        #print(k,v)
        s1 += '&%s=%s' % (str(k),str(v)) 
    #print(s1)  
    return s1[1:]
#请求方法 + 请求主机 +请求路径 + ? + 请求字符串
str2 = 'GETwenzhi.api.qcloud.com/v2/index.php?'+dict2url(mydict)
print(str2)

#数字签名