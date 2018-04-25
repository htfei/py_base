# 5.编程用sort进行排序，然后从最后一个元素开始判断

a=[1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
print(a)

a.sort()
print(a)

## 什么用？
last=a[-1]
for i in range(len(a)-2,-1,-1): # 倒数第二个，到倒数第一个，往前遍历步长为1
    if last==a[i]:
        del a[i]
    else:last=a[i]
print(a)
 