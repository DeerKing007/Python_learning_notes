# a=(i for i in range(10))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print(i)


def fun():
    a=0
    while 1:
        yield  a
        a+=1

        if a==10:
            raise StopIteration()

print(fun)
a=fun()
# print(next(a))

for i in a:
    print(i)