# n=int(input('请输入要查看的前n项：'))
# def fun(n):
#     count = 0
#     a, b = 0, 1
#     while count < n:
#         a, b = b, a + b
#         print(a,end=' ')
#         count += 1
# fun(n)

def fun(n):
    if n<3:
        return 1
    else:
        return fun(n-1)+fun(n-2)

n=int(input('请输入要查看的前n项：'))
for i in range(1,n+1):
    print(fun(i),end=' ')
