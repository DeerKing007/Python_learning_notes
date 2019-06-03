# def fun1():
#     x=5
#     def fun2():
#         nonlocal x
#         x+=1
#         return x
#     return fun2
#
# a=fun1()
# print(a(),end='')
# print(a(),end='')
# print(a(),end='   ')
#
#
# a=fun1()
# b=fun1()
# c=fun1()
# print(a(),end='')
# print(b(),end='')
# print(c(),end='')

# def funA(x,y=3):
#     return x*y
#
# lambda x,y=3:x*y

# lambda x:(x if x%2 else None)
#
# def fun(x):
#     if x%2:
#         return x
#     else:
#         return None

# 统计
# def count(*args):
#
#     #args是元组
#     for i in args:  #i是传进来的每个大字符串
#         eng_count = 0
#         num_count = 0
#         spa_count = 0
#         # other_count = 0
#         for j in i:
#             if j.isalpha():
#                 eng_count+=1
#             elif j.isdigit():
#                 num_count+=1
#             elif j.isspace():
#                 spa_count+=1
#         print('第%s个字符串有：%s个英文，%s个数字，%s个空格，%s个字符'\
#               %(args.index(i)+1,eng_count,num_count,spa_count,len(i)-(eng_count+num_count+spa_count)))
# count('hello world!','hello python')

# 24
# print(list(filter(lambda n:n%3==0,range(1,100))))
# print(list(filter(lambda n:not n%3,range(1,100))))

# 25
# def fun(a,b): # a,b 分别是两个点 可以元组代替（两个元素）
#     x1=a[0]
#     y1=a[1]
#     x2=b[0]
#     y2=b[1]
#     delta_x_pow=(x1-x2)**2
#     delta_y_pow=(y1-y2)**2
#     return (delta_x_pow+delta_y_pow)**0.5
#
# print(fun((0,0),(3,4)))

# def fun(x1,y1,x2,y2):
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
# print(fun(0,0,3,4))

# print((lambda x1,y1,x2,y2:((x1-x2)**2+(y1-y2)**2)**0.5)(0,0,3,4) )


# 27
# def jche2(n):
#     mul=1
#     for i in range(1,n+1):
#         mul*=i
#     return mul
#
# def jche(n):
#     han=n//100
#     ten=n//10%10
#     ge=n%10
#     return jche2(han)+jche2(ten)+jche2(ge)
#
#
# def fun():
#     for i in range(100,1000):
#         if i==jche(i):
#             print(i)
#
# fun()

# 28
# def fun(n):
#     while n!=1:
#         if n % 2 == 0:
#             n //= 2
#             print('是偶数除以2')
#         else:
#             n = n * 3 + 1
#             print('是奇数乘以3加1')
#     print('最终结果为：%s'%(n))

# 29
# def wqpf(n):
#     if int(n**0.5)**2==n:
#         return True
#     return False
#
# def fun():
#     for i in range(100,1000):
#         if wqpf(i):
#             a, b, c = i // 100, i // 10 % 10, i % 10
#             for j in range(100,1000):
#                 if wqpf(j):
#                     x,y,z=j//100,j//10%10,j%10
#                     if wqpf(a*10+x) and wqpf(b*10+y) and wqpf(c*10+z):
#                         print(i,j)
#
# fun()

# fun(int(input('请输入一个自然数：')))

# 30
# import functools
# def sums(n):
#     sums=0
#     for i in range(1,n):
#         if n%i==0:
#             sums+=i
#     return sums
#
#
#
# def fun():
#     for A in range(1,3000):
#         if sums(sums(A))==A and sums(A)<=A:
#             print('%s/%s是一对亲密数'%(A,sums(A)))
#
# fun()