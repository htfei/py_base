__author__ = 'Terry'



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
    pass
    #myslot = CurrentSlotState()
    #myslot.getlastslottime()

    #mydev = CurrentDeviceStatus()
    #mydev.getlastdevtime()

            # 执行实时车位状态查询策略
        #myslot.slot_strategies()

        # 执行实时硬件设备状态查询策略
        #mydev.dev_strategies()
