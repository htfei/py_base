__author__ = 'Terry'


'''
函数原型：range（start， end， scan):

参数含义:start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
        end:技术到end结束，但（不包括end）.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        scan：每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''

a = range(5)  # 相当于 range(0,5,1)
print(list(a))  # 代表从0到5(不包含5) :[0, 1, 2, 3, 4]


# list[start:end]  列出 下标 在start和end之间的 列表数据 （不包括end）
array = [1, 2, 5, 3, 6, 8, 4]
print(array)  # 打印列表 , print(array[:])
# 下标1=  0, 1, 2, 3, 4, 5, 6
# 下标2= -7,-6,-5,-4,-3,-2,-1
print(array[0:6])  # 代表 第1到第5个：[1, 2, 5, 3, 6, 8]
print(array[-7:3])  # [1, 2, 5]
# list[::scan] 列出
print(array[::2])  # [1, 5, 6, 4]

dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
s = '1'
print(dic[s])





