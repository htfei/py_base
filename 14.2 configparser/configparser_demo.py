# -*- coding:utf-8 -*-
import configparser


config = configparser.ConfigParser()
config.read("./config.ini")
print(config)

mode = config.getint("Pet", "mode")
print(mode)

isThreadPool = config.getboolean("Pet", "isThreadPool")
print(isThreadPool)

