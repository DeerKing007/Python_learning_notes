# # filter
#
# print(filter(None,[0,1,2,3,4,5]))
# print(list(filter(None,[0,1,2,3,4,5,True,False,[],(),'',' '])))
#
#
# def fun(n):
#     # print('this is fun')
#     # if n%2==0:
#     #     return True
#     # else:
#     #     return False
#     return n%2==0
#
# print(list(filter(fun,[0,1,2,3,4,5,6,7,8,9])))
#
# print(list(filter(lambda n:n%2==0 ,[0,1,2,3,4,5,6,7,8,9])))
# print(list(filter(lambda n:n%2!=0 ,[0,1,2,3,4,5,6,7,8,9])))
# print(list(filter(lambda n:n%2 ,[0,1,2,3,4,5,6,7,8,9])))

# map
# def fun(a,b,c,d):
#     return a+b+c+d
#
# print(list(map(fun,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))
#
#
# def fun2(*a):
#     sums=0
#     for i in a:
#         sums+=i
#     return sums
# print(list(map(fun2,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))
# print(list(map(lambda a,b,c,d:a+b+c+d,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))
# print(list(map(lambda *a:a,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))

# reduce
# import functools
#
# def func(a,b):
#     return a+b
#
# print(functools.reduce(func,[1,2,3,4,5]))
# print(functools.reduce(lambda a,b:a+b,[1,2,3,4,5],100))
# print(functools.reduce(lambda a,b:a+b,['a','b','c'],'hehe'))


# print(list(map(lambda a,b,*c:a+b+c,[1,2,3],[1,2,3],[1,2,3])))












