# 正则表达式

~~~markdown
不是Python独有的，是一套搜索引擎，用于做字符串的检索
起源于Unix---检索工具：awk，grep，egrep
~~~

* 正则表达式的基本概念

~~~markdown
正则表达式是一种小型的，高度专业化的编程语言
1. 正则表达式被集成在了re模块中
2. 正则可以指定查找规则

运行原理：
先将正则字符串编译成字节码，然后由C编写的引擎进行执行

注意：
正则表达式不是万能的，是相对较小的，功能有限（不是任何字符串都可以用正则表达式处理）
~~~

* re模块

~~~markdown
集成了正则表达式的相关方法
1. findall（正则表达式，目标字符串）
		从目标字符串中以正则表达式为要求，筛选出指定字符串
		并打包成列表进行返回
2. finditer,match,search
3. sub(正则表达式，替换的字符串，目标字符串)
		返回一个替换之后的字符串
4. subn(正则表达式，替换的字符串，目标字符串)
		返回一个元组：（替换之后的字符串，替换的个数）
5. split(正则表达式，目标字符串)
		通过正则进行切分，并把切分后的子串打包成列表进行返回
~~~

* 字符串的匹配

~~~markdown
1. 普通字符串：
		大多数数字和字母和字符都可以和自身匹配
		
2. 元字符串：
		在正则表达式中具有特殊含义的字符串
~~~

* 元字符串

~~~markdown
1. [] ：
		1. 用于指定一个字符集
			一个方括号只能代表一个字符串
			例:
			print(re.findall('a[bdc]c','abcadcacc'))
		2. 元字符串在字符集中不起作用
		3. 可以表示一个范围
2. ^ :
		通常用于匹配行首
		尖叫号如果在字符集中的第一位，表示取反
		尖叫号如果在字符集中的其他位置，表示普通字符串’^‘
3. $ :
		通常用于匹配行位
4. \：反斜杠
		1. 转义元字符串，为普通字符串
		2. 和特殊字符匹配，拥有特殊功能
			\d:匹配任何十进制字符串：[0-9]
			\D:匹配任何非数字字符串：[^0-9]
			\s;匹配任何空白字符串：[\t \n]
			\S:同上取反
			\w:匹配任何字母数字字符：[a-zA-Z0-9]
			\W:同上取反
5. {n}：重复
		n：重复的次数
6. * ：重复
		没有设置次数
		表示星号之前的一个字符重复0到n次、
		正则中默认匹配模式：贪婪匹配（尽可能多的匹配）
7. + ：重复
		表示+号之前的字符重复1次到n次
8. ？ ：重复
		1. 表示？号之前的字符重复1次或0次
		2. 如果？号在重复之后，表示启用非贪婪模式
9.  . : 
		匹配除了换行符以外的任何字符
10. {m，n}: 重复
		范围重复
		m：重复下限
		n：重复上限
		
		{,}:*
		{1,}:+
		{,1}:?
11. （）：分组
		只显示括号内的字符串
12. | :或
		同时用两个正则表达式进行匹配
~~~

~~~python
import re

# s='abc'
# rule='a'
# result=re.findall(rule,s)
# print(result)

# print(re.findall('a','abc'))
# print(re.findall('a','abcabb'))
# print(re.findall('a[bd]c','abcadcacc'))

# print(re.findall('^abc','abcadbacc'))
# print(re.findall('a\^','a^bcadbacc'))
# print(re.findall('a[bd^]c','abcadcba^c'))
# print(re.findall('a[^bd]c','abcadcba^c'))
# print(re.findall('a[b][d][a]c','abcadc'))
# print(re.findall('a[a-zA-Z0-9]c','abcadcaccaAca7c'))

# print(re.findall('acc$','abcadbacc'))

# print(re.findall('010-\d\d\d\d\d\d\d\d','010-12345678'))
# print(re.findall('010-\w\w\w\w\w\w\w\w','010-12345678'))
# print(re.findall('010-\d{8}','010-12345678'))
# print(re.findall('010-\d{8}','010-123456789'))
# print(re.findall('010-\d*','010-'))
# print(re.findall('010-\d*','010-123'))
# print(re.findall('010-\w*','010-12345678'))

# print(re.findall('010-\d+','010-'))
# print(re.findall('010-\d+','010-12345678'))
# print(re.findall('010-\d?','010-12345678'))
# print(re.findall('010-\d?','010-'))
# print(re.findall('010-\d*?','010-12345678'))
# print(re.findall('010-\d{3}?','010-12345678'))
# print(re.findall('010-\d+?','010-12345678'))
# print(re.findall('010-\d??','010-12345678'))

# print(re.findall('.','abc\nabd#A\t'))
# print(re.findall('010-\d{2,5}?','010-12345678'))
# print(re.findall('010-\d{2,5}?','010-123'))
# print(re.findall('010-\d{2,5}','010-1'))
# print(re.findall('010-\d{,}','010-12345678'))
# print(re.findall('010-\d{,}','010-'))
~~~

---

* 正则表达式的使用

~~~markdown
1. re模块提供一个正则表达式引擎的接口
2. 正则表达式有两种运行机制：
		1. 直接解释运行：练习，极少量的匹配需求
		2. 编译正则表达式：提高匹配效率
			使用 re.compile方法,编译之后会生成一个正则对象
~~~

~~~python
import re

target='010-123456789 010-12345678 010-123456'
rule='010-\d*'
# result=re.findall(rule,target)
# print(result)
rule_re=re.compile(rule) # 编译正则表达式
result=rule_re.findall(target)
print(result)
~~~

* 正则对象的方法

~~~markdown
1. match（target）：
		决定RE是否在字符串刚开始的位置匹配（匹配行首）
		如果匹配到对应字符串，则返回一个Match对象
		如果没有匹配到则返回None
2. search（target）：
		返回匹配字符串的位置
		如果匹配到对应字符串，则返回一个Match对象
		如果没有匹配到则返回None
3. findall（target）：
		返回一个列表，匹配到正则对应的字符串
4. finditer(target):
		找到RE匹配的所有字符串，并打包成一个迭代器返回
		每一个元素都是一个Mach对象
~~~

* MatchObject 实例

~~~markdown
1. group()
		返回RE匹配的字符串
2. start() 
		返回RE匹配的字符串的开始位置
3. end()
		返回RE匹配的字符串的结束位置
4. span()
		返回一个元组：（开始，结束）
		
~~~

~~~python
target='010-123456789 010-123456789 010-123456789 '

re_obj=re.compile('010-\d*')
# print(re_obj.match(target))
# print(re_obj.search(target))
# print(re_obj.findall(target))
for i in re_obj.finditer(target): # i: 每一个Match
    print(i.group(),i.start(),i.end(),i.span())
~~~

---

* 编译标志

~~~markdown
正则表达式在执行的过程中，可以接收额外的参数：编译标志
~~~

| 标志          | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| DOTALL，S     | 使 ‘.’ 匹配包括换行符在内的所有字符串                        |
| IGNORECASE，I | 是匹配对大小写不敏感                                         |
| MULTILINE，M  | 多行匹配(目标字符串)，影响^和$                               |
| VERBOSE，     | 启用正则表达式的verbose状态，使正则表达式更加清晰易懂（对正则表达式启用多行模式） |

~~~python
import re

# print(re.findall('.*','abc123\n123\tabc',re.S))
# print(re.findall('.*','abc123\n123\tabc',re.DOTALL))

# print(re.findall('abc','abc ABC Abc aBc',re.IGNORECASE))
# print(re.findall('abc','abc ABC Abc aBc',re.I))

# s='''
# abc
# acc
# adc
# aqc
# '''
# print(re.findall('^a.c',s,re.MULTILINE))


rule='''
010
-
\d*
'''
print(re.findall(rule,'010-123456789',re.VERBOSE))
print(re.findall(rule,'010-123456789',re.X))
~~~

---

### 爬虫练习

~~~markdown
网络爬虫：
		网络蜘蛛，网络机器人
		蚂蚁，自动索引，虚拟程序，蠕虫
		web crawler

从百度贴吧爬取图片
1. 访问百度贴吧
2. 分析网页结构
3. 下载网络源码
4. 将源码转换成字符串
5. 利用正则筛选有用数据（图片路径）
6. 再次向百度服务器请求图片
7. 保存图片
~~~

