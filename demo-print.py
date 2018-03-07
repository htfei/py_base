__author__ = 'Terry'
# 注意：python3中print需要使用括号!

# 1-2.变量,无论什么类型(数值，字符串，布尔，列表，元组，字典...)都可以直接输出
x = 12
print(x)

s = 'Hello'
print(s)

b = True
print(b)

L = [1, 2, 'a']
print(L)

t = (1, 2, 'a')
print(t)

d = {'a': 1, 'b': 2}
print(d)


# 3.格式化输出,类似于C中的 printf
s = 'Hello'
x = len(s)
print("The length of %s is %d" % (s, x))
pi = 3.141592653
print('%10.3f' % pi)  # 字段宽10，精度3
print("%.*f" % (3, pi))  # 用*从后面的元组中读取字段宽度或精度
print('%010.3f' % pi)  # 用0填充空白
print('%-10.3f' % pi)  # 左对齐
print('%+f' % pi)  # 显示正负号

# 4.如何让print不换行（在Python中总是默认换行的）,2.x 版本可以这样 print x, 在末尾加上,  3.x 中应该写成 print(x，end = '' )
for x in range(0, 10):
    print(x, end='')


# 5. 拼接字符串
s2 = 'World'
print('\n'+s + s2)
