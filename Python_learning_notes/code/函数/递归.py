# def fun():
#     print('hello world')
#     fun()
#
# fun()

# 求一个数的阶乘：
# n!=?  n*(n-1)*(n-2)...* 1
#
# def jc(n):
#     mul=1
#     for i in range(1,n+1):
#         mul*=i
#     print(mul)
#
#

# 求一个数的阶乘：
# n!=?  n*(n-1)!  (n-1)(n-2)!  (n-*)1!
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

print(jc(int(input('请输入一个整数：'))))