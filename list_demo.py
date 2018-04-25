A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = [ i for i in range(10)]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(A7)
'''
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
range(0, 10)
[]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
'''

print('###############################')

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2) # l指向内存中存储的一个列表
f(3,[3,2,1]) # l这时指向了新生成的列表
f(3) # l指向之前内存地址中存储的旧列表，而旧列表在f(2)调用时已被添加2个元素了
f(4) # 同f(3)
'''
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 0, 1, 4]
'''

print('###############################')
''''
#lis与set转化
>>> a=[1,2,4,2,4,5,6,5,7,8,9,0]
>>> set(a)
{0, 1, 2, 4, 5, 6, 7, 8, 9}
>>> [set(a)]
[{0, 1, 2, 4, 5, 6, 7, 8, 9}]
>>> [i for i in set(a)]
[0, 1, 2, 4, 5, 6, 7, 8, 9]
>>> list(set(a))
[0, 1, 2, 4, 5, 6, 7, 8, 9]
>>> {}.fromkeys(a)
{1: None, 2: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None, 0: None}
>>> {}.fromkeys(a).keys()
dict_keys([1, 2, 4, 5, 6, 7, 8, 9, 0])
>>> list({}.fromkeys(a).keys())
[1, 2, 4, 5, 6, 7, 8, 9, 0]
>>>
'''