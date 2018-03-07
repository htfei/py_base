# dict字典
# http://www.runoob.com/python/python-dictionary.html
# 使用dict和set --廖雪峰
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868193482529754158abf734c00bba97c87f89a263b000

# 定义
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 取值
print(d['Michael'])  # 95
print(d.get('Bob'))  # 75
print(d.get('Bob', -1))  # 75
print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))  # -1

# 检查
# print(d['Thomas']) #不存在则报错
print('Thomas' in d)  # False
print('Bob' in d)  # True

# 新建键值 or 修改
d['Adam'] = 67
print(d)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}

# 删除
d.pop('Bob')
print(d)
# 清空
#d.clear()
#print(d) #{}

#转str
#print(d+'hello') #error
print(str(d)+'hello')

#遍历
print(len(d))
print(d.items())
print(d.keys())
print(d.values())
print("Value : %s" %  d.values())

# 遍历dict并转化为url参数
def dict2url(mydict):
    s1 =''
    for k,v in mydict.items():
        #print(k,v)
        s1 += '&%s=%s' % (str(k),str(v)) 
    #print(s1)  
    return s1[1:]

print('http://www.baidu.com/v1/hello.php?'+ dict2url(d)); 