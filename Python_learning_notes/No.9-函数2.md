# 函数和过程

~~~markdown
函数：声明和过程是分开的
函数的执行不一定需要过程

函数的结构：
1. 函数的声明+返回值
2. 函数的过程
~~~

* 返回值

~~~markdown
return

1. 任何函数必然有返回值
		如果没有书写任何return，自动添加一个return None
		如果书写了return 没有书写返回值，自动添加一个 None
2. return的作用：将函数执行的流程返回
		返回的过程中可以携带一个值
3. return 后
		1. 跟任何值（具体的值）
		2. 跟一个表达式
		3. 跟一个函数的调用
				最终返回的返回值，是调用的别的函数的返回值
4. return可以返回且只能返回一个对象
		def fun():
    		return 1,2,3   # 本质上是将1,2,3封装成了一个元组，依然是一个值
		print(fun())
5. 同一个代码块中return 后的代码不执行
		因为return的作用是返回流程，刚好跳过了后面的代码
~~~

---

* 函数变量的作用域

~~~markdown
变量：
1. 全局变量：Global Variable
		1. 位置：必须没有缩进（写在行首）
		2. 先赋值后使用
		3. 作用范围（作用域）：从定义开始到文件结束
2. 局部变量：Local Variable
		1. 位置：在函数的内部（有缩进的变量）
		2. 先赋值后使用
		3. 范围：从定义开始到包含它的代码块结束

注意：
1. 如果局部变量和全局变量发生了命名冲突，以局部变量优先，但是局部变量并不会覆盖掉全局变量
		本质上函数内部创建了一个同名的局部变量，遮蔽了全局变量
2. 在函数内部不能书写类似于 a+=1 a=a+1 增强赋值运算（a是全局变量）
		等号左右两边的a不是同一种a
~~~

~~~python
a=10
def fun():
    a+=1# 报错
fun()

a=10
def fun():
    b=a+1
    a=b # 报错 
fun()
~~~



* global  关键字

~~~markdown
可以在局部访问全局变量
		可以在函数中修改同名全局变量
global关键字可以直接影响全局变量，和声明的位置无关
~~~

~~~python
a=10
def fun():
    global a
    a=20
    print(a)

fun()
print(a)
~~~

* nonlocal关键字

~~~Markdown
可以在内部函数中，修改外部函数的局部变量
注意：nonlocal只会影响一层，只影响向外的一层（拥有同名变量的一层）
~~~

~~~python
a=10
def fun1():
    a=20 
    def fun2():
        nonlocal a
        a=30  # 外面的局部 
        print(a)
    fun2()
    print(a)
fun1()
print(a)

========================
a=10
def fun1():
    a=20
    def fun2():
        nonlocal a
        a=30
        def fun3():
            a=40
            print(a)
        fun3()
        print(a)
    fun2()
    print(a)
fun1()
print(a)

~~~

---

### 内嵌函数和闭包

* 内嵌函数

~~~markdown
内部函数（内嵌函数）：函数的内部又定义了一个函数

内嵌函数的作用域：
1. 外部函数：从定义开始到文件结束（全局变量）
2. 内部函数：从定义开始到包含它的代码块（局部变量）

注意：
1. 内部函数不能进行a+=1的操作  （a:具有全局性质的变量---可以是全局变量，也可以是外部函数的局部变量）
		1. a+=1
		2. a=a+1
		3. b=a+1   a=b
		4. print(a)  a=20
		总结：先使用a，后给a赋值，这样会导致使用的a和赋值的a不是同一个变量---导致编译器编译失败（自相矛盾）
~~~

~~~python
def outer():
    def inner():
        print('hello world')
    inner()
outer()
~~~

### 闭包

~~~markdown
闭包：closure   全称：词法闭包（Lexical closure）
~~~

~~~python
def outer(x):
    def inner(y):
        print('hehe')
        return x+y
    return inner

print(outer(10)(20))
~~~

* 闭包的条件

~~~markdown
1. 必须是一个内嵌函数
2. 闭包必须返回内部函数的函数对象（函数名）
3. 内部函数必须引用外部函数的局部变量
~~~

* 闭包的作用

~~~markdown
1. 闭包可以在声明较少的参数的情况下，传递更多的参数
2. 可以在外部使用内部函数
3. 多应用于集群环境
~~~

* 闭包的优点

~~~markdown
1. 避免使用全局变量：
		全局变量是公共的资源，不安全，容易出现数据的脏读（污染）
2. 可以提供部分的数据隐藏
		数据隐藏---封装
3. 可以提供更优雅的面向对象的实现
~~~

---

* 匿名函数

~~~markdown
没有函数名的函数

~~~

- lambda表达式

```markdown
lambda：关键  主要用于创建匿名函数
语法：
lambda 参数：返回值  

1. lambda表达式会返回一个函数对象
		***不是函数的调用
作用：
2. lambda表达式多应用于函数式编程
		函数式编程：泛函编程
		将一个函数对象作为参数，传递给另一个函数
3. 临时使用一个函数，或只使用一次函数，应该使用匿名函数（lambda）
4. 简化代码，提高可读性
5. Lambda的优先级最低
```

~~~python
# 判断a是否是偶数
a=int(input('请输入一个整数：'))

print((lambda n:('偶数' if n%2==0 else '奇数') )(a))
~~~

---

### 高级函数

* 函数式 编程

~~~markdown
1. 也称之为泛函编程，是一种编程范式
		可以实现将函数对象作为参数传递给另个一函数
2. lambda是泛函编程的重要基础 
		Python的重要高级‘函数’：
		filter（）
		map（）
		reduce（）
~~~

* filter（）

~~~markdown
Python2：是函数
Python3：是类

1. filter(function or None, iterable)----过滤
		function or None :传一个函数对象或None
		iterable：可迭代对象
		返回一个filter对象---迭代器（可迭代对象）
		1. 如果第一个参数为None，则留下iterable中为真的元素
		2. 如果第一个参数为函数对象，则将iterable中的元素逐个传给函数对象（参数），并保留函数执行结果为真的元素
~~~

~~~python
# filter

print(filter(None,[0,1,2,3,4,5]))
print(list(filter(None,[0,1,2,3,4,5,True,False,[],(),'',' '])))


def fun(n):
    print('this is fun')
    if n%2==0:
        return True
    else:
        return False

print(list(filter(fun,[0,1,2,3,4,5,6,7,8,9])))

##lambda版本
print(list(filter(lambda n:n%2==0 ,[0,1,2,3,4,5,6,7,8,9])))
print(list(filter(lambda n:n%2!=0 ,[0,1,2,3,4,5,6,7,8,9])))
print(list(filter(lambda n:n%2 ,[0,1,2,3,4,5,6,7,8,9])))
~~~

* map()

~~~Markdown
map: 映射   
python2：函数
python3：类

1. map(func, * iterables)   
		1. 将每一个可迭代对象的每一个元素作为参数，进行计算，直到每个元素都运算完毕，返回运算之后新对象
		返回map对象  
		2. 函数func的参数的个数必须和可迭代对象的匹配
		3. 如果最短的可迭代对象执行完毕，则整个map执行完毕
~~~

~~~python
def fun(a,b,c,d):
    return a+b+c+d

print(list(map(fun,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))


def fun2(*a):
    sums=0
    for i in a:
        sums+=i
    return sums
print(list(map(fun2,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))

##lambda
print(list(map(lambda a,b,c,d:a+b+c+d,[1,2,3],[1,2,3],[1,2,3],[1,2,3,4,5])))
~~~

* reduce（）

~~~Markdown
reduce:折叠
python2：可以直接使用
python3：functools.reduce()
依旧是函数
1. reduce(function, sequence[, initial])
		function：函数对象
		sequence：序列
		initial：初始化值
		返回一个值
		将序列中的前两元素传递给function进行计算，计算结果将会和下一个序列中的元素作为下一次运算的参数，最终只得到一个值
		如果initial给出，则先计算initial和第一个元素的计算结果，后面一次类推
~~~

~~~python
import functools

def func(a,b):
    return a+b

print(functools.reduce(func,[1,2,3,4,5]))
print(functools.reduce(lambda a,b:a+b,[1,2,3,4,5],100))
print(functools.reduce(lambda a,b:a+b,['a','b','c'],'hehe'))
~~~

---

