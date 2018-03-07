from math import sqrt
a = range(1, 11)
print(a)
b = range(1, 10)
c = sum([item for item in a if item in b])
print(c)
# "item for item in a if item in b" 叫作列表推导式，是在一组字符串或者一组对象上执行一条相同操作的简洁写法！
# 最后的最后：人生苦短，我用Python.
