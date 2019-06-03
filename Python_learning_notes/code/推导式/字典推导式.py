d={key:value for key,value in [(1,'one'),(2,'two'),(3,'three')]}
print(d)

# 将上面的字典，键和值互换
d={value:key for key,value in [(1,'one'),(2,'two'),(3,'three')]}
print(d)

d={key:None for key,value in [(1,'one'),(2,'two'),(3,'three')]}
print(d)

d={i:None for i in range(10) if i%3==0}
print(d)
