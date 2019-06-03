# next() # 从迭代器中获取下一个元素
# iter() # 从可迭代对象中获取它的迭代器
# l=[1,2,3,4]
# a=iter(l) # a是列表的迭代器
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# a=l.__iter__()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# a=iter(l)
# a2=iter(a)
# print(a)
# print(a2)

# for i in a:
#     print(i)


# print(dir(a))
l=[1,2,3,4]
a=iter(l)

for i in a:
    print(i)

print('======================')
for i in a:
    print(i)
