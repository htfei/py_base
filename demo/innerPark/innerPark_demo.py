
# !/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Terry'

import requests
import json
import time
import configparser
import msgpack
import zmq
import sys
import importlib
importlib.reload(sys)

# 配置文件目录

innerPark_ini_path = './innerPark.ini'




# 从配置文件读取服务器的IP和端口
cf = configparser.ConfigParser()
cf.read(innerPark_ini_path)
ip = cf.get("innerPark", "ip")
last_park_time_s = cf.getint("innerPark", "last_park_time_s")
gateway_ip = cf.get("gateway", "ip")
gateway_data_port = cf.getint("gateway", "data_port")


# Socket to send messages to
context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.connect("tcp://" + gateway_ip + ":5558")  # read gateway ip and port form innerPark.ini


# 停车记录查询 类
class ParkingRecord(object):

    # 停车记录查询 时间间隔（s）
    time_interval_s = 60   # todo : 测试时暂定为60s同步一次,实际运行时改为5分钟 or 1小时，待测试后决定
    # 停车记录查询 上次查询时间（s）
    last_park_time_s = 1483954939

    # 停车记录查询url
    park_url = 'http://xx.xx.xx.xx:8000/innerParkMaintanceService/queryParkingTradingRecord'
    # 停车记录查询 post的 字典数据
    post_dict = {
        "invokeSerial": 1,
        "pageInfo": {"recordsPerPage": 10, "currentPage": 0},
        "condition": {
            "fuzzyMatchingPlateNo": False,
            "tradeType": None,
            "exitTimeStart": 1483954939000,
            "recordType": None,
            "exitId": None,
            "plateNo": None,
            "exitTimeEnd": 1483954939000,
            "entryId": None,
            "enterTimeStart": 1483954939000,
            "enterTimeEnd": 1483954939000
        },
        "terminalId": "\u4e3b\u7ec8\u7aef"
    }

    # the common log  will be packed
    # encode_point_data = [] # todo: 暂时无法确定点位，故采用common_log. 以后有需求再考虑添加or修改
    encode_common_log = []

    # 初始化ip和[上次同步时间]
    def __init__(self, ip, time_s):
        print(u'声明一个停车记录查询类...')
        self.park_url = 'http://' + ip + ':8000/innerParkMaintanceService/queryParkingTradingRecord'
        print(u'POST_URL:' + self.park_url)
        self.last_park_time_s = time_s
        print('从ini读取[上次同步时间]:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_s)))
        return

    # 读取'上次同步时间'
    def get_last_park_time(self):
        print('读取[上次同步时间]:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.last_park_time_s)))
        return self.last_park_time_s

    # 更新'上次同步时间'到配置文件
    def set_last_park_time(self, time_s):
        self.last_park_time_s = time_s
        print(u'[上次同步时间]更新为:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_s)))
        return

    # 发送数据到gateway
    def send_log_to_gateway(self):
        pack = msgpack.packb(self.encode_common_log)
        sender.send_string(pack)
        self.encode_common_log = []
        print(u'发送' + str(len(self.encode_common_log)) + '条log到gateway.')
        return

    # back list data解析处理
    def data_parse(self, post_dict):
        # 保存返回的数据到内存字典对象中。
        data = post_dict["data"]
        for each in data:
            print('list :' + each)
            # eg: [783, 'None', 1483005421000, '未知', 203, '京A12345', 1483005470948, 'ETC出口', 49948, 0.0, 'PESUDO', 'TRUSTED', 'FRONT_ETC']
            # [入场记录ID，入口识别车牌号,入场时间戳,入口,出场记录ID,出场识别车牌号,出场时间,出口,停车时间（毫秒）,交易金额,入口记录类型,出口记录类型,交易类型]

            # encode common log
            log_id = each[4]
            chepai = each[5]
            log_timestamp = int(each[6]/1000)
            log_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(log_timestamp)) #时间
            didian = each[7]
            log_context = log_time_str + ' ' + didian + ' ' + chepai + '离开停车场'

            common_log = [3, each[4], log_context, log_timestamp]  # log type,log id,log context,log timestamp
            self.encode_common_log.append(common_log)
            if len(self.encode_common_log) > 100:
                # send data to gateway.
                self.send_log_to_gateway()

        # 判断是否还有数据需要post
        current_page = post_dict["pageInfo"]["currentPage"]
        total_page = post_dict["pageInfo"]["totalPage"]
        if current_page < total_page:
            # 继续post获取下一页
            # 修改请求的页码+1
            self.post_dict["pageInfo"]["currentPage"] +=1
            # 修改请求序列号+1 #todo :暂时未确定翻页查询时此字段是否需要更新，待现场测试
            self.post_dict["invokeSerial"] +=1

            # 递归调用
            self.park_post()

        elif current_page >= total_page:
            print('this post is over.')
            # send data to gateway.
            if len(self.encode_common_log) > 0:
                self.send_log_to_gateway()
        return

    # post查询停车记录
    def park_post(self):
        r = requests.post(self.park_url,data=json.dumps(self.post_dict))
        # print(r.json())
        # data解析处理
        self.data_parse(r.json())
        return

    # 查询停车记录 策略
    def park_strategies(self):
        # print(u'执行停车记录查询策略...')

        # 读取当前时间
        now_s = int(time.time())
        # print('当前系统时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_s)))
        now_ms = now_s*1000

        if now_s >= self.last_park_time_s + self.time_interval_s:
            # 设置查询的时间段(上次出库到现在的所有出库记录)
            self.post_dict["condition"]["enterTimeStart"] = now_ms-24*3600*1000  # 24小时内进入的车辆
            self.post_dict["condition"]["enterTimeEnd"] = now_ms
            self.post_dict["condition"]["exitTimeStart"] = self.last_park_time_s # 60分钟内出去的车辆
            self.post_dict["condition"]["exitTimeEnd"] = now_ms

            # 查询停车记录
            # self.park_post()

            # 修改请求序列号+1 #temp:暂时未确定翻页查询时此字段是否需要更新，待测试
            self.post_dict["invokeSerial"] += 1

            # 更新上次同步时间
            self.set_last_park_time(now_s)

            # 同时更新时间到 配置文件 中去
            cf = configparser.ConfigParser()
            cf.read(innerPark_ini_path)
            cf.set("innerPark", "last_park_time_s", str(now_s))
            cf.write(open(innerPark_ini_path, "w"))
        else:
            time.sleep(1)
            now_s = int(time.time())
            print('距离下次查询还剩' + str(int(self.last_park_time_s + self.time_interval_s - now_s)) + 's',end='\r',flush=True)
        return

# 实时车位状态查询 类
class CurrentSlotState(object):

    # 实时车位状态 时间间隔（ms）
    slot_timeinterval = 10000
    # 实时车位状态 上次查询时间（ms）
    lastslottime = 1483954939000

    # 实时车位状态url  #temp：注意需要修改IP
    slot_url = 'http://xx.xx.xx.xx:8000/innerParkMaintanceService/getCurrentSlotState'
    # 实时车位状态 post的 字典数据
    solt_postdict = {
        "invokeSerial": 1,
        "terminalId": "\u4e3b\u7ec8\u7aef"
    }
    # 实时车位状态 post返回的 字典数据
    solt_back = {
        "slotsState":[
            {
            "areaId":"B区",
            "occupiedSlots":0,
            "totalSlots":25
            },
            {
                "areaId":"D区",
                "occupiedSlots":12,
                "totalSlots":16
            }
        ],
        "parkWhollySlotState":{
            "occupiedSlots":33,
            "totalSlots":120
        },
        "recordTime":1483958325825
    }

    def __init__(self):
        print(u'开始查询实时车位状态...')
        return

    # back list data解析处理
    def data_parse(self,list):
        print('now data:' + list)
        print('使用这个函数来解析data[]列表数据，并保存到sql or 发送给getway.')
        # ...
        return

    # post查询实时车位状态
    def slot_post(self):
        r = requests.post(self.slot_url,data=json.dumps(self.slot_postdict))
        # print(r.json())
        # 保存返回的数据到内存字典对象中。
        data = r.json()["slotsState"]
        for each in data:
            # data解析处理
            self.data_parse(each)
        return

    # 从配置文件中读取'上次同步时间'
    def getlastslottime(self):
        cf = configparser.ConfigParser()
        cf.read(innerPark_ini_path)
        self.lastslottime = cf.getint("innerPark", "lastslottime")
        print("上次同步时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.lastslottime/1000)))
        return self.lastslottime

    # 更新'上次同步时间'到配置文件
    def setlastslottime(self,timesp):
        self.lastslottime = timesp
        # 同时更新时间到 配置文件 中去
        cf = configparser.ConfigParser()
        cf.set("innerPark", "lastslottime", self.lastslottime)
        cf.write(open(innerPark_ini_path, "w"))
        return

    # 查询实时车位状态 策略
    def slot_strategies(self):
        # 读取当前时间
        now_time = time.time()*1000
        # print('当前系统时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time/1000)))
        if now_time >= self.lastslottime + self.slot_timeinterval:
            # 查询实时车位状态
            self.slot_post()
            # 修改请求序列号+1 #temp:暂时未确定翻页查询时此字段是否需要更新，待测试
            self.slot_postdict["invokeSerial"] +=1
            # 更新上次同步时间
            self.setlastslottime(now_time)
        else:
            time.sleep(1)
            now_time = time.time()*1000
            print('距离下次查询还剩' + str(int(self.lastslottime + self.slot_timeinterval - now_time)) + 'ms',end='\r',flush=True)
        return

# 实时硬件设备状态查询 类
class CurrentDeviceStatus(object):

    # 实时硬件设备状态查询 时间间隔（ms）
    dev_timeinterval = 10000
    # 实时硬件设备状态查询 上次查询时间（ms）
    lastdevtime = 1483954939000

    # 实时硬件设备状态查询url  #temp：注意需要修改IP
    dev_url = 'http://xx.xx.xx.xx:8000/innerParkMaintanceService/getCurrentDeviceStatus'
    # 实时硬件设备状态查询 post的 字典数据
    dev_postdict = {
        "invokeSerial": 1,
        "terminalId": "\u4e3b\u7ec8\u7aef"
    }
    # 实时硬件设备状态查询 post返回的 字典数据
    dev_back = {
        "deviceGroup":[
            {
                "deviceStatus":[
                    {
                        "status":"正常",
                        "deviceId":"出口摄像机",
                        "online":True
                    }
                ],
                "infrasGroupId":"出口"
            }
        ],
        "recordTime":1483958379681
    }

    def __init__(self):
        print(u'开始实时硬件设备状态查询...')
        return

    # back list data解析处理
    def data_parse(self,list):
        print('now data:' + list)
        print('使用这个函数来解析data[]列表数据，并保存到sql or 发送给getway.')
        # ...
        return

    # post 实时硬件设备状态查询
    def dev_post(self):
        r = requests.post(self.dev_url,data=json.dumps(self.dev_postdict))
        # print(r.json())
        # 保存返回的数据到内存字典对象中。
        data = r.json()["slotsState"]
        for each in data:
            # data解析处理
            self.data_parse(each)
        return

    # 从配置文件中读取'上次同步时间'
    def getlastdevtime(self):
        cf = configparser.ConfigParser()
        cf.read(innerPark_ini_path)
        self.lastdevtime = cf.getint("innerPark", "lastdevtime")
        print("上次同步时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.lastdevtime/1000)))
        return self.lastdevtime

    # 更新'上次同步时间'到配置文件
    def setlastdevtime(self,timesp):
        self.lastdevtime = timesp
        # 同时更新时间到 配置文件 中去
        cf = configparser.ConfigParser()
        cf.set("innerPark", "lastdevtime", self.lastdevtime)
        cf.write(open(innerPark_ini_path, "w"))
        return

    # 实时硬件设备状态查询 策略
    def dev_strategies(self):
        # 读取当前时间
        now_time = time.time()*1000
        # print('当前系统时间:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time/1000)))
        if now_time >= self.lastdevtime + self.dev_timeinterval:
            # 实时硬件设备状态查询
            self.dev_post()
            # 修改请求序列号+1 #temp:暂时未确定翻页查询时此字段是否需要更新，待测试
            self.dev_postdict["invokeSerial"] +=1
            # 更新上次同步时间
            self.setlastdevtime(now_time)
        else:
            time.sleep(1)
            now_time = time.time()*1000
            print('距离下次查询还剩' + str(int(self.lastdevtime + self.dev_timeinterval - now_time)) + 'ms',end='\r',flush=True)
        return


if __name__ == '__main__':

    # 声明一个 停车记录查询类
    park = ParkingRecord(ip, last_park_time_s)

    while 1:
        # break
        # 执行停车记录查询策略
        park.park_strategies()

