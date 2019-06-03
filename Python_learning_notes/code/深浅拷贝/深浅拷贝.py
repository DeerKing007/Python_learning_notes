# l1=[1,2,3]
# l2=l1  # 浅拷贝
# l3=l1.copy() # 浅拷贝
#
# print(l1,l2,l3)
# print(id(l1),id(l2),id(l3))
# print(id(l1[0]),id(l2[0]),id(l3[0]))

# a=257
# b=257
# print(id(a),id(b))


l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=l1.copy() # 外--拷贝  内层不拷贝
# print(l1)
# print(l2)
# print(id(l1),id(l2))
# print(id(l1[0]),id(l2[0]))
# l1[0][0]=99
# print(l1)
# print(l2)


import copy
l3=copy.deepcopy(l1)

print(l1)
print(l2)
print(l3)
print(id(l1),id(l2),id(l3))
print(id(l1[0]),id(l2[0]),id(l3[0]))

l1[0][0]=99
print(l1)
print(l2)
print(l3)