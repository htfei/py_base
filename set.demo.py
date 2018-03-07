# set即集合，set可以看成数学意义上的无序和无重复元素的集合
s = {1,2,3} #set([1, 2, 3]) #两种定义方法都可以
print(s)  # 
s = set([1, 1, 2, 2, 3, 3])
print(s)

#增加，删除元素
s.add(4)
print(s)
s.remove(4)
print(s)

# 交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}
