def 高效生成list():
    print('1'+str(2)) #12
    a = 1
    b = 3
    c = [9,b,a][a > b]  # 如果a > b返回list[1]，否则返回list[0]
    print(c) #9

    c = a if a>b else b # 如果a > b返回a，否则返回b
    print(c) #3

    c = [ i for i in range(10) if i%2==0 ]  # 遍历list，在i为偶数时返回
    print(c) #[0, 2, 4, 6, 8]

    # 同时嵌套遍历列表a和b，返回i和j同时为偶数时的和。
    # 其中for in a属于外层嵌套，for in b属于内层
    c = [i+j for i in range(5) for j in range(5,10) if i%2==0 and j%2==0]    
    print(c) #[6, 8, 8, 10, 10, 12]
    # 等同于下面的表达式
    c=[]
    for i in range(5):
        for j in range(5,10):
            if i%2==0 and j%2==0:
                c.append(i+j)
    print(c) #[6, 8, 8, 10, 10, 12]

#list相连
a=[1,2,3]
b=[4,5,6]
c= a+b
print(c)
print(b+a)


#元组 范围都是不可变的类型，即不能作为自变量，不能修改

#取下标(第一次出现)
c=[1,2,5,5,6]
print(c.index(5))