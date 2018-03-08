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
