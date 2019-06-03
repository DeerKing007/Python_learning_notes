# def outer(x):
#     def inner(y):
#         print('hehe')
#         return x+y
#     return inner
#
# print(outer(10)(20))
#
# def outer():
#     def inner():
#         return 100
#     return inner
# outer()()

# def fun1():
#     def fun2():
#         pass
#     return fun2()
# print(fun2())


# def outer():
#     x=10
#     def inner(a,b,c,d):
#         return x+a+b+c+d
#     return inner
# print(outer()(1,2,3,4))
#
# a=10
# def fun1():
#     def fun2():
#         return a


# a=[1,2,3]
#
# def fun1(n):
#     print(n)
#
# def fun2(n):
#     n[0]=99
#
# fun2(a)
# fun1(a)


# def fun1():
#     a=[1,2,3]
#     def fun2():
#         a[0]=99
#         return a
#     return fun2
#
# print(fun1()())
#
# def fun3():
#     a=[1,2,3]
#     def fun4():
#         return a
#     return fun4
#
# print(fun3()())







