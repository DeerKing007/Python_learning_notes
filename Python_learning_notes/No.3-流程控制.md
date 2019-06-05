# 流程控制

### 条件分支流程

* if-else结构

~~~markdown
1. 语法：
		1. if 布尔表达式：
				代码
		2. if 布尔表达式：
				代码
		   else:
		   		代码
		3. if 布尔表达式：
				代码
		   elif 布尔表达式：
		   		代码
		   ...
		   else:
		   		代码

补充：代码块：
1. Python中有代码块，可以用一对花括号表示，代码块中一定书写逻辑代码
2. Python主导优雅的代码风格，一般不书写代码块（花括号）
		Python利用缩进表示代码块（tab）
		每一层缩进表示该代码属于上一层代码的内容
3. 利用缩进控制代码块，避免else悬挂问题
		C语言中：根据就近原则匹配else，导致else的执行发生错误
		
补充
1. else和if中的代码绝不可能同时出现
2. 不同的if-else结构之间不会发生干扰
3. if-else的嵌套
		if结构，else结构，elif结构可以任意嵌套
~~~

~~~python
money=int(input('请输入您充值的钱数：'))

if 100>=money>50:
    print('赠送果盘')
elif 500>=money>100:
    print('赠送精品烤鸭一只')
elif 2000>=money>500:
    print('当天免单')
elif 10000>=money>2000:
    print('您是普通VIP')
elif 50000>=money>10000:
    print('您是高级VIP','附赠洗浴一次')
elif 100000>=money>50000:
    print('您是顶级VIP','泰国-芭堤雅圣地一月游')
else:
    print('欢迎消费')
    
~~~

---

### 断言

~~~markdown
assert  语句
assert 布尔表达式
如果布尔表达式为真：流程正常执行
如果布尔表达式为假：程序终止，并抛出异常：AssertionError
~~~

### 循环流程

* while



~~~markdown
重复的执行某代码集
1. 语法
		while 布尔表达式：
			代码：循环体
2. 注意：
		1. 循环的条件
		2. 死循环（# 硬件设施 服务器 操作系统）
		
3. 练习：请输入一个整数，计算各个位数之和？
	
4. 补充
		while 1 和while True 的效率问题
		Python2：
				while 1 的效率更高
					1：不可变的---
				while True 的效率较低
				
		python3：
				都一样
~~~

~~~python
#请输入一个整数，计算各个位数之和

n=int(input('请输入一个整数：')) # 12345

# 创建累加器
sums=0

while n!=0:
    ge=n%10
    n//=10
    sums+=ge

print(sums)
~~~

---

* for

~~~markdown
称之为计数循环  
1. Python中的for循环：
		1. 可以调用函数
		2. 可以处理异常
2. 语法
		for 变量名 in 可迭代对象：
			循环体
		
		1. 变量名：任意变量（符合标识符命名规范）
		2. 可迭代对象：
		

注意：
知道循环次数：for循环
不知道循环次数：while循环
~~~

* range

~~~markdown
range()---构造方法
range是一个类，可以返回一个range对象

1. range(stop):
		start默认取0
		step默认取1
2. range(start,stop[,step]):
		[]:表示可选参数（可以给，也可以不给）
		start：从某个数开始
		stop：到某个数结束（取不到）
		step: 步长从start开始每次增加或减少的数量
		取值范围：[start,stop)
		
3. 补充
		序列是可迭代对象
		for循环的循环次数由可迭代对象的元素个数决定
~~~

~~~python
for i in range(0,10):
    print(i,end=' ')
print()

for i in range(10):
    print(i,end=' ')
print()

for i in range(1,10):
    print(i,end=' ')
print()

for i in range(1,10,3):
    print(i,end=' ')
print()

for i in range(10,1,-1):
    print(i,end=' ')
print()

for i in range(-5,5,1):
    print(i,end=' ')
~~~

* 练习

~~~python
打印10遍hello world
for i in range(10):
    print('hello world')
~~~

* continue

~~~markdown
跳过本次循环，不影响其他循环
~~~

~~~python
for i in range(10):
    if i==3:
        continue
    else:
        print(i)
~~~

* break

~~~markdown
跳出本次循环，其他循环不再执行
~~~

~~~python
for i in range(10):
    if i==3:
        break
    else:
        print(i)
~~~

---

* 循环嵌套

~~~markdown
循环中可以使用循环
双重循环，内层循环控制列数，外层循环控制行数
~~~

~~~python
# 向控制台打印一个正方形  用*

for i in range(4): # 打印4行
    for i in range(4): # 打印一行星星
        print('*',end=' ')
    print()
~~~

~~~python
for i in range(4):
    for j in range(i+1):
        print('*',end=' ')
    print()
~~~

~~~python
# 九九乘法表
for i in range(1,10): # 1~9
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t\t')
    print()
~~~

---

