# 类和对象

~~~markdown
万物皆对象
Python： 函数，数据，文件，包，range对象，set-like对象，set对象，frozenset对象。。。
~~~

### 面向对象的思想

~~~markdown
1. 第一个面向对象的语言：small talk
2. C++ ---拥有面向对象的思想（C）
		面向过程：
		面向对象：
3. Java: 是由C++实现的---纯面向对象的语言---革命--1995
4. Python：更加纯粹的面向对象的语言
~~~

### 对象

~~~markdown
万物皆对象
1. 对象： 
		一切客观存在的事物
		
对象的构成：
1. 有什么：属性
2. 能做什么：方法

对象=属性+方法

客观世界是由对象构成
1. 属性
		由小对象组成大对象
2. 方法
		对象和对象之间相互调用方法
~~~

* 对象的属性

~~~markdown
1. 可以是另一个对象
~~~

* 对象的方法

~~~markdown
1. 对象和对象之间彼此方法调用
		一个对象调用另一个对象的方法
		一个对象调用自己的方法
		一个对象可以被自己调用同时也可以被其他对象调用
~~~

* 建立解题思路（现实世界）

~~~markdown
从 沙河 到 天安门 
找对象
找方法

1. 把解决问题需要的对象准备好
2. 对象和对象之间合理的调用方法

1.  面向过程的思想：---把每一个步骤都考虑清楚
		地铁/小黄车/公交车/步行（人）/打车---从哪上车-从沙河-出昌平-朝阳-西城-在哪下车-宣武门
2.  面向对象的思想： ---找对象+找方法
		地铁
		调用地铁的交通运输方法
		
1. 面向对象的思想：
		1. 可以简化流程
		2. 只需要找到对象，调用方法即可
		3. 第一步找到合适的对象，调用合适的方法，其次再考虑过程
	
2. 面向过程的思想：
		要把每一步都细化到十分精细，只考虑过程
~~~

---

### 在编程中的面向对象思想

~~~markdown
计算的的需求：来源于客观世界
1. 面向对象思想的核心：
		模拟现实世界，从而解决现实世界的问题
~~~

~~~markdown
需求：聊天  订饭    购物   租房子  找工作  相亲  。。。 
实现：QQ   饿了么   淘宝   58      智联   百合 。。。

计算机中的对象
在内存中一块连续的存储空间（属性+方法：计算机中的数据）

图书管理系统：
	现实：书+书架+房子+管理员---管理员管理图书
	计算机：书对象+书架对象+数据库（房子）+管理员---系统（管理图书）
	
	书：
	书名：name='三国演义'
	价格：price=99.9
	作者：author=‘罗贯中’
	
	def looked():
		print('this book is looked')
~~~

* 总结

~~~markdown
存在即合理

面向对象的特点：
1. 各司其职：
		对象应该保持简单性
2. 弱耦合性：
		对象和对象之间的关系尽量弱化
3. 可重用性：
		创建一个对象可以多次使用
4. 可扩展性：
		在原有的功能基础上增加新的功能
		
OOP：面向对象的编程   Object Oriented Programming
~~~

---

### 类

~~~markdown
1. 类是对象共性的抽象
2. 类是对象的模板
3. 类是人脑对客观事物的一种主观反应

类是主观的认知，对象向是客观的存在
~~~

* 如何编写一个类

~~~markdown
类=属性+方法

语法结构：
	class  类名：
		属性名=属性值
		。。。
		
		def 方法名（self）：
			方法的实现
		。。。
~~~

~~~python
# 创建学生类
class Student:
    # 属性
    name='ming'
    age=18
    sex=True

    #方法
    def learn(self):
        print('student can learn')
~~~

---

* 属性

~~~markdown
1. 属性的分类：
		类属性
		实例属性
2. 类属性：
		1. 属于类的属性
        2. 直接写在类中的属性
        3. 通过类名直接调用，不用创建任何对象
        4. 可以通过对象进行调用
		5. 类属性一旦修改影响所有的对象
				牵一发而动全局
		6. 如果通过实例修改了类属性，类属性不会被修改，而是创建了一个同名的实例属性，从而遮蔽了类属性
		7. 对象默认引用类属性，类属性有且只有一个，所有对象共用
		8. 类的外部也可以创建类属性：
				类名.新属性名=属性值 
3. 实例属性：
		1. 实例属性属于实例
				实例：对象
		2. 在方法内部创建的属性
		3. 必须先创建实例对象
		4. 实例属性的创建和修改不会影响类的
				因为该属性是属于实例的，不属于类
		5. 对象之间实例属性各自拥有相互不会影响
		6. 如果通过实例修改了类属性值，不会影响其他实例，也不会影响类
		7. 如果在方法内部创建一个同名的实例属性，会遮蔽掉类属性，不会影响类属性
		8. 类的外部也可以创建实例属性：
				对象名.新属性名=属性值 
~~~

~~~python
# 创建学生类
class Student:
    # 属性
    name='ming'
    # age=18
    sex=True

    #方法
    def learn(self):
        self.score=100
        print('student can learn')

    def showName(self,name):
        self.name=name

    def addClassAttribute(self):
        Student.age=18


# print(Student.score)# 学生类还没有创建score属性，所报错
# s1=Student()
# s1.learn()  # 创建score
# # print(s1.score)
# # print(Student.score)
# s2=Student()
# s3=Student()
# print(s2.score)  # 没有score属性


# s1=Student()  # 创建对象  s1是变量 存储Student()对象的地址  s1可以代表对象，不是学生对象
# # print(s1)
# s2=Student()
# s3=Student()   # 创建了3个学生对象  相互之间不影响
#
# print(Student.name)  #ming
# # print(id(s1),id(s2),id(s3))
# print(s1.name,s2.name,s3.name)
# Student.name='jian guo'
# print(Student.name)
# print(s1.name,s2.name,s3.name)
~~~

* 方法

~~~markdown
1. 方法的结构：
		方法的声明+返回值
		方法的实现
2. 方法和函数的区别：
		self
3. self:
		1. 是一个位置参数
		2. self指代当前对象---
		3. self在方法调用时，会自动传入，不用手工传入
		4. self是绑定方法的组成元素
		5. self不是关键字，不是保留字，是普通的参数，系统会自动传入当前对象，只会给第一个参数传当前对象，和是否是self名字无关
4. 方法的使用必须先创建对象
		1. 先创建实例对象，利用实例对象调用方法，自动传递self
		2. 通过类调用方法，不会自动传递self，需要手工传递self，需要额外创建一个实例对象
5. 方法可以定义多个参数，除了self以外其他参数的使用形式和函数类似
6. 参数的传递，归根结底都是地址的传递（引用）
~~~

~~~python
class Student:
    name='ming'
    def learn(self):
        self.age=18
        age=20
        print(age,self.age,self.name)

s1=Student()
# print(s1.name)
s1.learn()
# print(s1.age)
# s1.sex=True
# Student.name
# s1.name
~~~

---

###  构造方法

~~~markdown
1. __init__(self):
		初始化方法 
		构造方法：3.5以前
		构造方法的作用：应该是创建实例对象---但是__init__()不会创建对象（不能算是真正意义上的构造方法）
		可以接收多个参数，多个参数用逗号隔开
2. 创建对象时自动调用一次，不需要手工调用
3. 创建对象时类名后的括号内构传递造参数
		参数会传递给构造方法：init方法（初始化方法）
4. 一个类中如果定义多个构造方法，后者会覆盖掉前者
5. 构造方法的返回值，只能是None值
6. 一个类可以没有构造方法，会向该类的父类调用构造方法
~~~

~~~python
class Student(object):  # object:对象---是所有实例对象的父类，根类
    # def __init__(self,a,b,c):
    #     print('this is init method',a,b,c)
    # def __init__(self):
    #     print('hehe')
        # return [1,2,3]
    pass

s1=Student()


# s1.__init__()

# class List:
#     def __init__(self,iterable=[]):
#         print(iterable)
#
# l1=List()
# l2=List([1,2,3])

~~~

* 补充：

~~~Markdown
__init__（）的应用：一般初始化实例属性
~~~

~~~python
class Student:
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex


s1=Student('小明',True,18)
s2=Student('建国',False,18)
print(s1.name,s2.name)
~~~

---

* 创建一个对象

~~~markdown
1. 变量名=类名（构造参数）
2. 类名（构造参数）
3. 创建的对象：实例对象（instance）
		实例对象：手工创建
		类对象：class 创建 
~~~

* 组合

~~~markdown
一个类的属性是另一个对象，称该形式为组合
~~~

~~~python
# 类属性
class Student:
    name='ming'

class Teacher:
    name='jian guo'

class School:
    teacher=Teacher()
    student=Student()

s=School()

print(s.student.name)
print(s.teacher.name)

================================
# 实例属性
class Student:
    name='ming'

class Teacher:
    name='jian guo'

class School:
    def getClass(self):
        self.student=Student()
        self.teacher=Teacher()


s=School()
s.getClass()
print(s.student.name)

=================================
# 配合构造方法使用
class Student:
    name='ming'

class Teacher:
    name='jian guo'

class School:
    def __init__(self):
        self.student=Student()
        self.teacher=Teacher()

s=School()
print(s.student.name)
print(s.teacher.name)

==============================
# 定制版组合1
class Student:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name

class School:
    def __init__(self,teacher,student):
        self.teacher=teacher
        self.student=student

s=School(Teacher('建国'),Student('小明'))
print(s.student.name)
print(s.teacher.name)

==================================
#定制版组合2
class Student:
    def __init__(self,name):
        self.name=name

class Teacher:
    def __init__(self,name):
        self.name=name

class School:
    def __init__(self,t_name,s_name):
        self.teacher=Teacher(t_name)
        self.student=Student(s_name)

s=School('建国','小明')
print(s.student.name)
print(s.teacher.name)

~~~

---

* 访问范围

~~~markdown
公有私有
1. 私有化：在属性钱加入两条下划线
		在类外部不能进行访问，但是类内部可以进行访问
2. 私有化过程：
		1. 给想要私有化的属性或方法加下划线
		2. 提供对应的get/set方法
3. Python的私有化，不是真正的私有化
		伪私有化
		name mangling 名字重构
		修改形式： _类名__属性名
~~~

~~~python
class Student:
    __score=85
    def getScore(self):
        return self.__score
    def setScore(self,newScore):
        self.__score=newScore

s1=Student()
print(s1.getScore())
print(s1._Student__score)


class A:
    def __init__(self):
        self.__age=18
    def __methodb(self):
        print('this is methodb')
a=A()
# print(a._A__age)
a._A__methodb()
~~~

----



