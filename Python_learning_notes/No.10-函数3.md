# 函数嵌套调用和递归

* 函数的嵌套调用

~~~Markdown
在一个函数中调用其他函数（最一般的函数使用方法）
~~~

~~~python
def fun3():
    print('thisis fun3')
    print('thisis fun3')

def fun2():
    print('this is fun2')
    fun3()
    print('this is fun2')

def fun1():
    print('this is fun1')
    fun2()
    print('this is fun1')

fun1()
~~~

* 解一元二次方程

$ax^2+bx+c=0$

$x=\frac{-b\pm{\sqrt{b^2-4ac}}}{2a}$

~~~python
def shiFouYouJie(a,b,c):
    delta = b ** 2 - (4 * a * c)
    if delta>=0:
        return True
    else:
        return False

def jieFangCheng(a,b,c):
    # 判断x是否有解
    delta=b**2-(4*a*c)
    if shiFouYouJie(a,b,c):
        x1=((-b)+(delta)**0.5)/(2*a)
        x2=((-b)-(delta)**0.5)/(2*a)
        print(x1,x2)
    else:
        print('无解')

jieFangCheng(1,1,1)
jieFangCheng(1,1,-1)
~~~

* 哥德巴赫猜想

~~~Markdown
任何一个大于6的偶数，都能拆分成两个质数的和
~~~

~~~python
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

~~~

---

* 递归

~~~markdown
递归是一种特殊的嵌套调用
		自己调用自己
无限递归：
	无限的自己调用自己，永远不会退出
	尽量避免无限递归
	无限递归会大量消耗内存（1. 执行效率低 2.内存累加）
	递归深度：python允许递归的层数（python预设，1000层---保护系统）
	
	解决方案：设置递归的收敛条件
	
递归思想：
	1. 对问题尽心拆分，大问题的解决方案和小问题的解决方案一样（一致）
	2. 递归一般用于解决难题（简化的是流程）
~~~

~~~python
# 利用递归求n的阶乘
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

print(jc(int(input('请输入一个整数：'))))
~~~

* 斐波那契数列

~~~python
n=int(input('请输入要查看的前n项：'))
def fun(n):
    count = 0
    a, b = 0, 1
    while count < n:
        a, b = b, a + b
        print(a,end=' ')
        count += 1
fun(n)
=================
def fun(n):
    if n<3:
        return 1
    else:
        return fun(n-1)+fun(n-2)

n=int(input('请输入要查看的前n项：'))
for i in range(1,n+1):
    print(fun(i),end=' ')
~~~

* 汉诺塔问题

![汉诺塔](E:\AI145\笔记\md笔记\picture\汉诺塔.png)

~~~python
def hnt(froms,to,temp,n):# 从froms柱子  到to柱子，中间利用temp柱子 n盘子的个数
    # 首先要设置收敛条件
    if n==1:
        print('%s--->%s'%(froms,to))
        return None
    else:
        # 1. n-1个盘子从froms--temp 借助to
            hnt(froms,temp,to,n-1)
        # 2. 一个盘子从froms--to
            print('%s--->%s'%(froms,to))
        # 3. n-1个盘子从temp--to 借助froms
            hnt(temp,to,froms,n-1)

hnt('A','B','C',3)
~~~

* 注意

~~~markdown
1. 不是所有的题都适合用递归
2. 递归占资源，运行效率比较慢
3. 能用递归写的题，一定能用循环写
~~~

---

