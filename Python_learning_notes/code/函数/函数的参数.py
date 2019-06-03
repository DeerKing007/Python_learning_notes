# def fun(param1,param2):
#     print(param1)
#
# fun('hehe')
# fun([1,2,3])

# def fun(a,b,c):
#     # a和b应该是个字符串， c是个列表
#     print(a+b)
#     print(c)
#
# fun([1,2,3],'b','a')


# def fun(a,b,c):
#     print(a,b,c)
# fun(c=3,b=2,a=1)

# def fun(a=10,b=20,c=30):
#     print(a,b,c)
# fun(1,2,c=3)
# fun()

# def fun(a,b):
#     pass
# fun(1,a=2)

# l=[1,2,3]
# def fun(a):  # a=l
#     print(a)
#     a[0]=99
# fun(l)
# print(l)

# def fun(a,b):
#     pass
# fun(a=1,a=2)
#
# def fun(*a):
#     print(a) # 元组
#     for i in a:
#         print(i)
#
# fun(1,2,3,4,5)

# print('{1},{0}'.format('hehe','python'))
#
# def format(*a):
#     print(a[1],a[0])
#
# format('hehe','python')

# def fun(**kwargs):
#     print(kwargs)
#
# fun(a=1,b=2,c=3)

# def fun(**a):
#     print(a)
#
# fun(a=10)

# def fun(*a,b):
#     print(a,b)
# fun(1,2,3,4,b=5)
#
# def fun(a=10,*b):
#     print(a,b)
#
# fun(1,2,3,4,5)

# def fun(a,a):
#     pass

def fun(*a,b,**c):
    print(a,b,c)

fun(1,2,3,4,5,b=6,d=10,e=20)







