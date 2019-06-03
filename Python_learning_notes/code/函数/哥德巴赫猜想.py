# 大于等于6
# 两个质数  和

def qzs(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def gdbh(n):
    for i in range(2,n//2+1):
        # 判断i  和n-i 是否都是质数
        if qzs(i) and qzs(n-i):
            print('%s=%s+%s'%(n,i,n-i))


gdbh(int(input('请输入一个大于等于6的偶数：')))