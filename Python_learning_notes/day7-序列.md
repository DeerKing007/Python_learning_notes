# 序列

* 常见的序列

~~~markdown
list,tuple,str
1. 可迭代对象
2. 支持索引操作
3. 支持切片操作
4. 支持拼接，重复


序列的特点：
* 支持切片操作
* 支持索引操作
~~~

* 序列相关的函数

~~~markdown
1. list()  str()  tuple() 
		构造方法
2. range() 
3. 获取序列的长度：len（）
4. max（）
		1. 如果只有一个参数（可迭代对象）返回可迭代对象中最大的元素
		2. 如果有多个可迭代对象作为参数，则返回比较之后最大的参数
		max(iterable, *[, default=obj, key=func])
    	max(arg1, arg2, *args, *[, key=func])
    	注意：混合可迭代对象可能会出错
5. min()
		1. 如果只有一个参数（可迭代对象）返回可迭代对象中最小的元素
		2. 如果有多个可迭代对象作为参数，则返回比较之后最小的参数
6. sum()
		sum(iterable, start=0)
		求和，注意不能传入字符串序列（无法和整数相加的元素都不能传递）
7. sorted()
		排序（默认升序排序）
		sorted(iterable, key=None, reverse=False)
		key:排序规则	
		reverse：是否翻转
8. reversed（）
		原地翻转
		返回列表翻转迭代器对象（利用了工厂模式）
9. enumerate（）---构造方法
		枚举
		enumerate(iterable[, start])
		返回一个枚举对象（迭代器-可迭代对象）
		将下标和下标对应的元素打包成元组作为一个完整的大元素
		
		l=['a','b','c']
		a=enumerate(l)
		list(a)
		[(0, 'a'), (1, 'b'), (2, 'c')]
10. zip()---构造方法
		 压缩
		 zip(iter1 [,iter2 [...]])
		 返回一个zip对象
		 将每个可迭代对象对应下标的元素打包成元组
		 当最短的可迭代对象压缩完毕则停止压缩
~~~

---

