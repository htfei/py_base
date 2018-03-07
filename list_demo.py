for i in range(2,5):
    print(i)

c = [ i for i in range(10) if i%2==0 ]  # 遍历list，在i为偶数时返回
print(c)

# 同时嵌套遍历列表a和b，返回i和j同时为偶数时的和。
# 其中for in a属于外层嵌套，for in b属于内层
c = [i+j for i in range(5) for j in range(5,10) if i%2==0 and j%2==0]    
print(c)

c=[]
for i in range(5):
    for j in range(5,10):
        if i%2==0 and j%2==0:
            c.append(i+j)
print(c)