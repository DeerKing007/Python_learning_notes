# MixIn编程

~~~markdown
是一种开发模式，是一种将多个类中的功能单元组合的使用的方式

组合：一个类中的属性是另个一实例对象
mixin：一个对象可以使用多个类中的方法---和继承没有必然联系
~~~

* 利用多继承

~~~markdown
Python支持多继承的，继承拥有可扩展性，父类扩展子类，子类利用多个父类继承的形式，获得多种方法
~~~

~~~python
class A:
    def a(self):
        print('a')

class B:
    def b(self):
        print('b')

class C(A,B):
    pass

c=C()
c.a()
c.b()
~~~

* 利用__bases\_\_

~~~markdown
1. __bases__属性直接返回继承关系（直接继承关系）
2. 可以利用修改bases属性达到影响类的继承关系
3. 不使用mro的原因：
		1. 有用不到的类继承关系
		2. 不能直接展示直接父类
~~~

~~~python

class A:
    def a(self):
        print('a')

class B:
    def b(self):
        print('b')

class C(A):
    pass


c=C()
C.__bases__+=(B,)
c.a()
c.b()
~~~

* 利用插件模式

~~~markdown
1. __dict__ 是一个字典，记录了对象（类对象，实例对象）的所有属性和方法
2. 修改dict魔法属性，可以影响对象中成员的变化
~~~

~~~python
lass Plug:
    def __init__(self):
        # self.methods={} # 利用该字典影响被插入的对象
        self.methods=[]  # 收集所有想要插入的方法对象

    def plugIn(self,owner):  # owner:被插入的对象
        for i in self.methods: # i是每一个方法对象
            owner.__dict__[i.__name__]=i

    def plugOut(self,owner): #
        for i in self.methods:
            del owner.__dict__[i.__name__]

class A(Plug):
    def __init__(self):
        super().__init__()
        self.methods.append(self.a) # 给父类中的方法库，append一个方法对象

    def a(self):
        print('a')

class B(Plug):
    def __init__(self):
        super().__init__()
        self.methods.append(self.b) # 给父类中的方法库，append一个方法对象

    def b(self):
        print('b')

class C:pass

c=C()
A().plugIn(c)
B().plugIn(c)

c.a()
c.b()
~~~

* mixin编程的特点

~~~markdown
1. 可以在不修改任何源代码的前提下，对已有的类进行扩展
2. 可以保证组件的划分
3. 可以根据需要使用已有的功能
4. 很好的避免了多继承的局限性
~~~

---

