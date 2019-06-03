# 面向对象特性

~~~markdown
面向对象特性也称之为：三大基石
~~~

* 封装

~~~markdown
1. 对象都有明确的边界，把属性保护在边界之内
		将内部和外部进行了隔离，外部不能直接访问内部属性或方法，内部不能直接访问外部的属性或方法
		封装也称之为：数据隐藏
2. 封装的粒度：
		控制一个对象的范围---边界，封装的目标：属性和方法
		封装的粒度过大：导致封装的目标过于复杂，不利于各司其职
		封装的粒度过小：导致封装的目标过于简单，让过程过于复杂
~~~

~~~python
# class A:
#     age=18
#
# class B:
#     name='建国'
#     def hehe(self):
#         print(age)
#
# b=B()
# b.hehe()
# print(age)




class School:
    class Teacher:
        pass

    class Student:
        pass

    teacher=Teacher()
    student=Student()

    def getClass(self):
        print('上课')

s=School()
print(s.student)
~~~

* 继承

~~~markdown
物质---生物---动物---哺乳动物---狗类---哈士奇，泰日天，中华田园犬
继承关系
更抽象：父类：是子类的抽象
更具体：子类：是父类的具象（特殊）

汽车---货车+轿车+卡车+客车   

定义形式：
class 子类类名（父类类名）：

父类：也称之为基类，超类  BaseClass
object:是Python中的一个类：根类，是所有类的父类
~~~

~~~python
class Parent(object):
    pass

class Children(Parent):
    pass
~~~

* 继承的特点

~~~markdown
1. 子类可以继承父类中的成员
		属性+方法 统称为成员
2. 子类不能继承父类中的私有成员
3. 可扩展性：
		父类扩展了子类
4. 多继承
5. init方法的调用：(子类可以调用父类的成员)
		1. 当子类拥有__init__()方法时，只会调用子类的方法
		2. 当子类没有__init__()方法时，会调用父类中的init
6. 访问父类的init方法：（子类调用父类成员的方法）
		1. 父类类名.父类方法（self）
        2. super().父类方法（）
        3. 父类类名（）.父类方法（）
~~~

* 方法覆盖

~~~markdown
方法覆盖：子类用特殊的方法实现，替换掉父类继承下来的一般的方法实现

语法要求：子类和父类中的方法名完全一致
注意：父类中的方法名不能省略，因为方法名相当于接口，无论子类是否实现了接口，子类都会拥有父类中的方法（接口）

接口：
接口就是标准
~~~

~~~python
class Animal:
    def eat(self):
        print('Animal can eat')

class Dog(Animal):
    def eat(self):
        print('dog can eat')

class Cat(Animal):
    def eat(self):
        print('cat can eat')

class Fish(Animal):
    def eat(self):
        print('fish can eat')

d=Dog()
c=Cat()
f=Fish()

d.eat()
c.eat()
f.eat()

~~~

* 多继承

~~~markdown
一个类可以同时继承多个父类
		语法：
		class  子类名（父类1，父类2...）
		
1. 尽量避免多继承，可能会导致混乱
2. 多继承中父类的属性和方法有先后继承关系
3. 钻石继承问题（菱形继承）
		多个子类共同继承了一个父类，可能会导致资源浪费（创建多次父类）
		解决方案：使用super（）
		原因：super的底层实现是按照mro实现的
			mro：继承链式关系
			mro中的链式关系中，所有的类只会出现一次
4. 循环继承问题
		一个类可以有多个子类，也可以有多个父类，其中任何一个父类不能是自己的子类
		多继承中，子类的子类不能直接继承object
~~~

~~~python
class  A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('B')

class C(A):
    def __init__(self):
        A.__init__(self)
        print('C')

class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('D')


d=D()  # A B A C D  A出现了两次，A多占用了一个内存


============================================
#解决？？？

class  A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(A):
    def __init__(self):
        super().__init__()
        print('C')

class D(B,C):
    def __init__(self):
        super().__init__()
        print('D')


d=D()
~~~

~~~python
class A:
    def __init__(self):
        print('A')

class B:
    def __init__(self):
        print('B')

class C(A,object):
    def __init__(self):
        print('C')

class F(C,object):
    def __init__(self):
        print('F')

class D(A,B):
    def __init__(self):
        print('D')

print(C.mro())
print(D.mro())
print(F.mro())
~~~

* 补充：

~~~Markdown
Python 2.2版本引入super
Python2：没有super()用法
Python3：有super()用法

1. super():
		无参的形式相当于调用super(type,obj):
2. super(type,obj):
		type:类
		obj：实例
		super（type，obj）：选取mro中type类右边的第一个类作为返回对象
~~~

---

### 多态+多态性

* 多态

~~~markdown
1. 一种类事物拥有多种形态

动物-猫，狗，人，鱼  序列-列表，字符串，元组
2. 多态和继承息息相关
		没有继承，就没有多态
~~~

~~~python
def fun(animal):  # animal [1,2,3]
    animal.eat()  # 正常执行的原因：animal变量中代表的对象，一定会有eat方法---eat方法时父类继承下来的


class Animal:
    def eat(self):
        print('animal eat')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

class Monkey(Animal):
    pass

class Snake(Animal):
    pass

class Panda(Animal):
    pass



fun(Snake())
fun(Animal())
~~~

* 多态性

~~~markdown
1. 向不同的对象发送同一条信息，不同的对象在接收时，会产生不同的行为
2. 和继承没有必然联系
~~~

~~~python
class Dog:
    def run(self):
        print('Dog run')


class Car:
    def run(self):
        print('Car run')

class Hourse:
    def run(self):
        print('Hourse run')

def fun(obj):
    obj.run()

fun(Dog())
fun(Car())
~~~

* 多态和多态性的好处

~~~markdown
1. 增加程序的灵活性
2. 增加了程序的可扩展性
~~~

---

#  内置函数或类

* issubclass()

~~~markdown
1. issubclass(cls, class_or_tuple)--函数
		cls:类
		class_or_tuple:另一个类或其他类的元组
		cls 是否是第二个参数的子类（不严谨---一个类是自己的子类）
		如果第二个参数是元组（多个类），只要有任意一个类是其父类，则返回True，否则返回False	
~~~

~~~python
class A:pass
class B:pass
class D:pass
class C(A):pass

print(issubclass(C,A))
print(issubclass(C,D))
print(issubclass(C,C))
print(issubclass(C,(A,B,D)))
print(issubclass(C,(B,D)))
~~~

* isinstance()

~~~markdown
1. isinstance(obj, class_or_tuple)---函数
			判断obj是否是第二个参数的子类实例对象
			如果第二个参数是元组（多个类），只要有任意一个类是实例对象的父类（包含父类的父类），则返回True，否则返回False	

~~~

~~~python
class A:pass
class B:pass
class D:pass
class C(A):pass

a=A()
c=C()
print(isinstance(a,A))
print(isinstance(a,B))
print(isinstance(c,C))
print(isinstance(c,A))
print(isinstance(c,(A,B,D)))
print(isinstance(c,(B,D)))
~~~

* hasattr

~~~markdown
1. hasattr(obj, name)--函数
		判断obj中是否有name的属性
		name:是str
		
~~~

~~~python
class A:
    age=18
    __sex=True

a=A()
print(hasattr(a,'age'))
print(hasattr(a,'hehe'))
print(hasattr(a,'_A__sex'))
~~~

* getattr

~~~markdown
1. getattr(object, name[, default])
		从object中获得name属性，如果属性不存在，则返回default值，如果default值没有给出，则直接报错
		name是str
~~~

~~~python
class A:
    age=18
    __sex=True

a=A()
print(getattr(a,'age'))
print(getattr(a,'hehe','属性不存在'))
print(getattr(a,'hehe'))
~~~

* setattr

~~~markdown
1. setattr(obj, name, value)
		在obj对象中设置name属性，值为value
~~~

~~~python
class A:
    age=18
    __sex=True

a=A()
setattr(a,'hehe',100)
setattr(a,'hehe',200)
print(getattr(a,'hehe'))
~~~

* delattr

~~~markdown
1. delattr(obj, name)
		从obj中删除name属性
~~~

~~~python
class A:
    def __init__(self):
        self.age=18

a=A()
delattr(a,'age')
print(hasattr(a,'age'))
~~~

* property

~~~markdown
1. property是一个类，返回一个property对象
2. property(fget=None, fset=None, fdel=None, doc=None)
		fget:被关联的属性的get方法
		fset:被关联的属性的set方法
		fdel:被关联的属性的del方法
		doc:文档说明
3. 作用：
		将一个属性和另一个属性进行关联

~~~

~~~python
class Student:
    def __init__(self):
        self.__socre=90
    def getScore(self):
        return self.__socre
    def setScore(self,newScore):
        self.__socre=newScore
    def delScore(self):
        del self.__socre
    score=property(getScore,setScore,delScore,'hehe')

s=Student()
print(s.score)
print(s.getScore())
s.score=100
print(s.getScore())
del s.score
print(s.getScore())
~~~

* 补充

~~~markdown
1. 如果类属性和方法名发生命名冲突：
		出现在后面的对象会覆盖掉前面的对象
2. 如果实例属性和方法名发生命名冲突：
		实例属性会覆盖掉方法对象
~~~

---

