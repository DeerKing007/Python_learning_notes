# l=[i for i in range(1,30+1) if i%2==0]
# print(l)
#
# s='hello world'
# l2=[i for i in s]
# print(l2)
#
# print([i+1 for i in range(10)])
#
# print([9 for i in range(10)])
#
# print([i**2 for i in range(10)])
#
# def fun(x):
#     return x**2
# print([fun(i) for i in range(10)])
#
# print([(lambda x:x**2)(i) for i in range(10)])
#
# print([(lambda x:x**2) for i in range(10)])

# 请输入一个值n，打印一个从1到n的列表，用lambda实现
a=lambda n:[i+1 for i in range(n)]

print(a(int(input('请输入一个整数：'))))

def fun(n):
    temp=[]
    for i in range(n):
        temp.append(i+1)
    return temp
print(a(int(input('请输入一个整数：'))))

