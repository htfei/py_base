# coding=utf-8
#!/usr/bin/python

import hashlib
import hmac
import base64
import urllib.parse
import time
import requests
import random

# http://wiki.open.qq.com/wiki/关键字提取API
# https://github.com/QcloudApi/qcloudapi-sdk-python

SecretId = 'AKID4wa0B7fHWYLtBEhYooX0D9tNaXR9PqoW'
SecretKey = 'av0pOhla9TXQ5UecLo1yf6HCrGPII4bt'

def textkeywords(title,content):
    #2. 生成签名串signature
    #2.1. 对参数排序
    mydict = {
            'Action' : 'TextKeywords',
            'Nonce' : random.randint(100000,999999),
            'Region' : 'ap-guangzhou',
            'SecretId' : SecretId,
            'Timestamp' : int(round(time.time())),
            'content': content,
            'title': title,
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

    str1 = dict2url(mydict)
    str2 = 'GETwenzhi.api.qcloud.com/v2/index.php?'+ str1
    #print(str2)

    #数字签名
    signature = base64.b64encode(hmac.new(SecretKey.encode('utf-8'), str2.encode('utf-8'), digestmod=hashlib.sha1).digest())
    #print('signature=',signature)
    #URL编码
    SigURL = urllib.parse.quote(signature)
    #print(str(SigURL))

    #4.2 API调用
    #构造请求URL
    url = 'https://wenzhi.api.qcloud.com/v2/index.php?' + str1 +  '&Signature=' + SigURL
    #print(url)

    #执行请求
    myPage = requests.get(url).content.decode("gbk")
    print(myPage)

if __name__ == '__main__':
    title = '习近平在参加内蒙古代表团审议时强调 扎实推动经济高质量发展 扎实推进脱贫攻坚'
    content = '''他首先表示完全赞成政府工作报告，强调政府工作报告体现了党的十八大以来党中央的一系列决策部署，体现了党的十九大精神，回顾了过去5年政府工作情况和成就，提出了今年政府工作目标任务。

　　习近平指出，内蒙古是我国最早成立民族自治区、党的民族区域自治制度最早付诸实施的地方，地处祖国北疆，战略地位十分重要。内蒙古改革发展稳定工作做好了，在全国、在国际上都有积极意义。他充分肯定党的十八大以来内蒙古各方面建设取得的新成绩，希望内蒙古的同志们再接再厉，打好三大攻坚战，扎实解决好发展不平衡不充分问题，推动经济发展质量变革、效率变革、动力变革，全面做好稳增长、促改革、调结构、惠民生、防风险各项工作，推动经济社会发展再上新台阶。

　　习近平强调，我国经济已由高速增长阶段转向高质量发展阶段。'''
    textkeywords(title,content);