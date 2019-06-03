# 字符串

~~~markdown
Python---对象   字符串对象
特点：
1. 天生具有快平台性质
2. 是可迭代对象
3. 支持下标操作
4. 支持切片操作
5. 支持成员操作符
6. 拥有人为含义
		变相的存储任何数据
7. 是不可变类型
~~~

~~~markdown
1. 单引号引起来的内容,双引号引起来的内容，三引号引起来的内容
2. 原始字符串：
		r'abc'
3. bytes---二进制字符串
		b'abc'
		str---bytes  endcode()
		bytes---str  decode()
4. 转义字符
		\t:横向制表符
		\n:换行符
~~~

* 常用的方法

~~~markdown
‘’：空串  
1. capitalize()
		将首字母大写
2. casefold()
		将字符串转小写
3. center(width[, fillchar])
		居中
4. count(sub[, start[, end]])
		返回字符出现的个数
5. encode(encoding='utf-8', errors='strict')
		编码，返回一个bytes二进制字符串
6. endswith(suffix[, start[, end]])
		判断结尾的字符串是否是suffix
7. expandtabs(tabsize=8)
		给横向制表符，设置长度，默认长度为8个空格
8. find(sub[, start[, end]])
		从字符串中找sub字符串的最小下标，如果没找到则返回-1
9. index(sub[, start[, end]])
		返回sub的下标
10. isalnum()
		判断字符串是否都是字母或数字
11. isalpha()
		判断是否是字母
12. isdecimal()
		判断是否都是数字：十进制
13. isdigit()：
		判断是否都是数字
14. isnumeric()：
		判断是否都是数字：中文，大写，罗马
15. islower()：
		判断是否都是小写
16. isspace()：
		判断是否是空格
17. isupper():
		判断是否都是大写
18. join(iterable)
		利用字符串将可迭代对象的每个元素分割开
19. ljust(width[, fillchar])
		左对齐
20. rjust(width[, fillchar])
		右对齐
21. split(sep=None, maxsplit=-1)
		分割字符串，返回一个列表（字符串列表）
22. upper()/lower()
		全大写/全小写
~~~

----

* 格式化

~~~markdown
1. format(* args ， * kwargs)
		*args:可变长参数---封装成元组使用
		**kwargs：可变长参数---封装成字典使用
		格式化输出字符串
		
2. 利用位置参数传值---  ‘{0}{1}...’.format('a','b'...)
		字符串中的数字和format参数的下标有关
		字符串中的数字之间和书序无关
		
		如果花括号内不写任何参数，默认从0开始逐个递增
3. 利用关键字参数传值---'{a} love {b}'.format(a='I',b='python')
		字符串中的字母，和format中的关键字参数有关
		
4. 如果想要打印花括号：
		花括号可以转义花括号
		print('{{{0}}}'.format(1))
~~~

~~~python
# print('{0} love {1}'.format('I','Python'))
# print('{1} love {2}  {2}'.format('I','Python','hehe'))

# print('{} love {}'.format('I'))

print('{a} love {b}'.format(a='I',b='python'))
print('{a} love {c}'.format(a='I',b='python',c='hehe'))
~~~

* 字符串的操作

~~~markdown
通过%将不同类型的数据格式化成字符串

1. %c---格式化字符ASCII码
		print('%c'%97)  # a
2. %s：格式化字符串
		相当于str（）
		如果字符串中需要多个参数，用都好隔开
		print('%s love %s'%('I','Python'))
3. %d：格式化整数
		print('%d'%100)
4. %o:格式化八进制数（无符号）
		print('%o'%10)
5. %x:格式化十六进制数（无符号）
		print('%x'%12)
6. %X：同上  大写
		print('%X'%10)
7. %f：格式化定点数（小数）
		print('%f'%100)
		默认取小数点后6位
		四舍五入
8. %e:格式化科学计数法
		print('%e'%12345.679)
		默认取小数点后6位
		四舍五入
9. %E:格式化科学计数法 大写
10. %g:自动选择使用%f或%e
		print('%g'%12345.6789)
		print('%g'%12345108709837498273492834.6789)
11. %G:自动选择使用%f或%E
~~~

---

* 格式化操作辅助命令

~~~Markdown
辅助命令书写在%和特殊字符中间
1. m.n  
		m:显示的最小宽度
		n:小数点后的位数-四舍五入
2. -：用于左对齐
		print('%-10d'%5)
3. #：八进制或十六进制显示符号
		print('%#x'%10)
		print('%#o'%10)
4. 0： 在数字前填充0
		print('%10d'%5)# 0000000005
		print('%-010d'%5)  # 5        
~~~

---

* 转义字符

~~~markdown
转义字符拥有特殊的功能
斜杠可以让转义字符消失含义

1. \':单引号
2. \":双引号
3. \a:发出系统铃声
4. \b:退格符
5. \n:换行符  在win：\r
6. \t:横向制表符
7. \v:纵向制表符
8. \f:换页符
9. \o:代表八进制字符串
10. \x:十六进制字符串
11. \0:空字符串
12. \\:反斜杠

代码换行：  \
表示可以将一个完整的表达式分割成两行，不会影响操作
本质还是一行数据
~~~

---

