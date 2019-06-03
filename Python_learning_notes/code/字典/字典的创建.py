# print(dict())
#
# d={1:'one',2:'two',3:'three'}
#
# print(dict(d))
#
# d1=[(1,'one'),(2,'two'),(3,'three')]
# d2=[(1,'one'),(2,'two'),(3,'three')]
# print(dict(d1))
# print(dict(d2))
#
# print(dict(one=1,two=2,three=3))

# d={}.fromkeys([1,2,3],99)
# print({}.fromkeys([1,2,3],99))
# print({}.fromkeys([1,2,3],['a','b','c']))
# print(d)
# print(d[1])

d={'one':1,'two':2,'three':3}
# print(d)
# print(d['two'])
# print(list(d.keys()))
#
# for i in d: # 键值对  键  值
#     print(i)
#
# print(list(d.values()))
# print(d.items())
#
# for i in d.items():  #i:元组
#     print(i)

# print(d)
# # print(d.get('three'))
# # print(d.get('four'))
# d['one']=99
# print(d)
# # print(d['four'])
# d['four']=4
# print(d)

# print(d.pop('four','error'))
# print(d.pop('three'))
print(d)
# print(d.popitem())
# print(d)

# print(d.setdefault('four',4))
# print(d.setdefault('three',4))
# print(d)

print(d.update({'four':4}))
print(d.update([('five',5),('six',6)]))
print(d.update(a=10,b=20))
print(d)

