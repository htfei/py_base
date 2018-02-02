# coding=utf8
#!/usr/bin/python

'''
python3 安装scapy-python3
注：linux，可能需要以root登陆，避免出现permission error
Scapy还包含内建函数arping(),该函数实现的功能和以上的两个命令类似：
arping("192.168.1.*")
'''
from scapy.all import srp, Ether, ARP
#import scapy
IpScan = '192.168.114.1/24'
try:
    ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
except Exception as e:
    print(e)
else:
    for send, rcv in ans:
        ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")
        print(ListMACAddr)
