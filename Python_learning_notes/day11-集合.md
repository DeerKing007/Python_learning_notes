# 集合

~~~markdown
set：集合
{}：可以应用于集合
{1,2,3} --- 集合
~~~

* 集合的特点

~~~markdown
1. 集合是无序的
		顺序是由哈希值决定
2. 集合是可迭代对象
3. 不支持索引操作和切片操作
		不是一个序列
4. 集合的元素不重复
5. 集合的元素必须是可哈希值
		不可变类型
		字典的键就是由集合实现
6. 集合是可变类型
~~~

* 集合的创建

~~~markdown
1. 手工创建：
		变量名={元素1，元素2...}
2. set（）：
		创建空集合对象
		{}：表示空字典
		set():表示空集合---集合对象
3. set(可迭代对象):
		将可迭代对象的每个元素，作为集合的元素
~~~

* 集合的访问

~~~markdown
1. 遍历---访问所有元素
		集合中的所有的元素被访问一遍，不重复，不遗漏
~~~

* 集合的修改

~~~Markdown
1. 存储的一定是不可变类型的元素，不涉及修改问题
~~~

* 集合的删除

~~~markdown
1. clear（）：
		清空集合
2. pop():
		删除并返回一个元素，如果集合为空则报错
3. remove（value）
		从集合中删除value元素，如果value不存在则报错
4. discard(value)
		从集合中删除value元素，如果value不存在什么都不做
~~~

* 集合的添加元素

~~~markdown
1. add（元素）
		向集合中添加一个元素
		只能添加可哈希值（不可变类型）
		如果用元组作为元素，注意：元组中不能有可变类型
~~~

---

* 集合相关的操作符

~~~markdown
1. 支持成员关系操作符
		in  not in
2. 支持增强赋值
		数学相关方法
		-=
		-
3. 支持比较运算符
		< > <= >= != ==
		数学相关比较
~~~

---

* 集合其他的方法：

~~~markdown
1. copy（）：
		浅拷贝
~~~

* 交集，并集，差集

~~~markdown
1. 交集：
		&  intersection()   insersection_update() 两集合相交并修改调用者
2. 差集/补集
		-  difference()  difference_update() 两集合做差并修改调用者
3. 并集：
		|  union（）	update() 两集合求并集，并修改调用者
4. 对称差集：
		symmetric_difference() symmetric_difference_update() 
		求两个集合的对称差集，并修改调用者
5. 判断是否相交：
		isdisjoint()
6. issubset():
		判断是否是子集
7. issuperset():
		判断是否是父集
~~~

~~~python
s1={1,2,3}
s2={3,4,5}
s3={7,8,9}
s4={1}

print(s1 & s2)
print(s1.intersection(s2))
print(s1,s2)
s2.intersection_update(s1)
print(s1,s2)


print(s1-s4)
print(s1,s4)
s1.difference_update(s4)
print(s1,s4)


print(s1 | s2)
print(s1.union(s2))

print(s1-s2)
print(s2-s1)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

print(s1.isdisjoint(s3))
print(s4.issubset(s1))
print(s1.issuperset(s4))
# print(s1.issubset(s2))
~~~

---

* 不可变集合

~~~markdown
frozenset:不可变集合
        l=[1,2,3,4]
        f=frozenset(l)
        print(f)
        
1. frozenset():
		返回一个空不可变集合对象
2. frozenset():
		返回一个新的frozenset对象
		
特点：
1. 是一个可迭代对象
		可以遍历
2. 元素是无序的
3. 是一个不可变类型
~~~

---

