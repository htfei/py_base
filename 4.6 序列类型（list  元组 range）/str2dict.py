# -*- coding:utf-8 -*-
import ast

user = '{"name" : "john", "gender" : "male", "age": 28}'
user_dict = ast.literal_eval(user)
print user_dict
print user_dict['age']
# {'gender': 'male', 'age': 28, 'name': 'john'}

user_info = "{'name' : 'john', 'gender' : 'male', 'age': 28}"
user_dict = ast.literal_eval(user)
print user_dict
print user_dict['name']
# {'gender': 'male', 'age': 28, 'name': 'john'}


# unicode暂时无法正确解析
DEV_FMT = "{'IPMI':u'物理机','server':u'服务器','os':u'操作系统'}"
user_dict = ast.literal_eval(DEV_FMT)
print user_dict
# {'IPMI': u'\xe7\x89\xa9\xe7\x90\x86\xe6\x9c\xba', 'os': u'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f', 'server': u'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8'}
# print user_dict['IPMI'].decode('unicode-escape')