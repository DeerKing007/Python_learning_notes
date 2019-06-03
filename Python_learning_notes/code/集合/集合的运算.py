s1={1,2,3}
s2={3,4,5}
s3={7,8,9}
s4={1}

# print(s1 & s2)
# print(s1.intersection(s2))
# print(s1,s2)
# s2.intersection_update(s1)
# print(s1,s2)

# print(s1-s4)
# print(s1,s4)
# s1.difference_update(s4)
# print(s1,s4)

# print(s1 | s2)
# print(s1.union(s2))

# print(s1-s2)
# print(s2-s1)
# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

print(s1.isdisjoint(s3))
print(s4.issubset(s1))
print(s1.issuperset(s4))
# print(s1.issubset(s2))




