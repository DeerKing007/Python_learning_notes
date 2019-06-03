# a=10
# if 1>0:
#     b=10

# print(a)
# a=10

# def fun():
#
#     print(a)
#     a = 10
# fun()

# a=10
# def fun():
#
#     b=20
#     print(b)
# fun()
# print(b)

# a=10
# def fun():
#     global a
#     a=20
#     print(a)
#
# fun()
# print(a)


# a=10
# def fun1():
#     global a
#     a=20  # a---全局
#     def fun2():
#         nonlocal a
#         a=30  # 外面的局部
#         print(a)
#     fun2()
#     print(a)
# fun1()
# print(a)



# a=10
# def fun1():
#     a=20
#     def fun2():
#         # nonlocal a
#         # a=30
#         def fun3():
#             nonlocal a
#             a=40
#             print(a)
#         fun3()
#         print(a)
#     fun2()
#     print(a)
# fun1()
# print(a)


# def fun():
#     global a
#     a=20
#     print(a)
# fun()
# print(a)

# a=10
# def fun():
#     # a+=1  # a=a+1   a+1  a=？？
#     # b=a+1  # 全局
#     # print(b)
#     a=20
#     print(a)  # 局部
#
#     a+=1# a=a+1
# fun()

# a=10
# def fun():
#     # b=10
#     # b+=1
#     # a=20
#     # a+=1
#     # b=a+1
#     # a=b






