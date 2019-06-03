# if 1>0:
#     i=1
#
# print(i)

# 临时变量不销毁现象---作用域泄露问题
#
# count=0
# for i in range(10):  #JS---Java Script  脚本   脚本
#     # print('hehe')
#     count+=1
#     if i ==3:
#         break
#
# # print(i)
#
# print(i)  # 漏洞  危险，使用方便，


# def fun():
#     a=10
#     def fun2():
#         nonlocal a
#         a=a+1
#         return a
#     return fun2
# b=fun()
# print(b())
# print(b())
# print(b())


# Python 的闭包延时绑定问题
# def fun():
#     l=[]
#     for i in range(4):
#         def fun2(a,c=i):
#             return a*c
#         l.append(fun2)
#     return l
#
# b=fun()  # 列表l
# for j in b:
#     print(j(2))

# def fun():
#     return [lambda x,c=i:c*x for i in range(4)]
#
# print([i(2) for i in fun()])






