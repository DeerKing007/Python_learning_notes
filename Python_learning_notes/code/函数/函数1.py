# 登鹳雀楼
# 需求：分隔符
# print('白日依山尽')
# print('+++++++++++++++')
# print('黄河入海流')
# print('+++++++++++++++')
# print('欲穷千里目')
# print('+++++++++++++++')
# print('更上一层楼')
# print('+++++++++++++++')    # 60遍  ---维护   将进酒


# 2
#
# print('白日依山尽')
# for i in range(15):
#     print('+',end='')
# print()

# print('黄河入海流')
# for i in range(15):
#     print('+',end='')
# print()
# print('欲穷千里目')
# for i in range(15):
#     print('+',end='')
# print()
# print('更上一层楼')    # 修改了4遍
# for i in range(15):
#     print('+',end='')
# print()




# V3.0
def fgf(a,b):  # a:要打印的符号   b:打印的次数
    for i in range(b):
        print(a, end='')  # 修改了1遍
    print()

print('白日依山尽')
fgf('+',5)
print('黄河入海流')
fgf('-',10)
print('欲穷千里目')
fgf('*',15)
print('更上一层楼')
fgf('/',20)
