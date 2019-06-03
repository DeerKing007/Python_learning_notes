# 异常

~~~markdown
异常---对象
异常的目的：提高系统的容错性
		制定合适的容错机制
~~~

~~~python
file=open(r'hehe.txt','r')
print(file.read())
file.close()

异常：运行时异常
~~~

* 常见的异常

~~~Markdown
异常类
1. AssertionError:断言异常    
2. AttributeError：属性异常
3. KeyError：键异常
4. IndexError：索引异常（下标越界异常）
5. TypeError：类型异常
6. NameError：变量名异常
7. ValueError：值异常
8. FileNotFoundError：文件未找到异常（是IOError的子类）
9. SyntaxError:语法错误
10. ZeroDivisionError：分母为零异常
11. RecursionError：递归异常（1. 达到了最大递归深度）（2. 内存溢出）
12. KeyboardInterrupt：键盘终止异常
13. ImportError：导入异常
~~~

* 异常处理

~~~Markdown
1. try---except
		try:
			可能出现异常的代码
		except 异常类名 [as 变量]：
			异常处理的代码
			
		try：收集异常（收集代码）
		except:将捕获的异常进行处理（捕获异常）
		1. 要捕获的异常和收集的异常要一一对应
		2. 大类型可以捕获小类型（大类型必须是小类型的父类）
		3. 如果捕获多个异常：
				1. 写多个except结构
				2. 在except后一元组的形式，书写多个异常
						可读性差（建议将as 变量补充上）
		4. 在try中出现任何异常，异常之后的代码，都不执行
				try中不可能同时抛出多个异常
		5. 如果大类型和小类型同时存在，小类型应该在前面
		6. except后如果不写异常类型，表示，捕获任何异常
2. try-except-finally
		try:
			可能出现异常的代码
		except 异常类 as 变量：
			异常处理的代码
		finally：
			无论如何都会执行的代码
		
		finally:无论是否有异常，都会执行
			一般写资源的释放的代码
			
3. 嵌套使用
		try-except-finally
		可以任意嵌套使用
~~~

~~~python
try:
    # 1/0
    # print('****')
    f = open(r'hehe.py', 'r')
    print(f.read())
    f.close()
# except FileNotFoundError as reason:
#     print('客官，文件开小差了~~~')
# except FileNotFoundError:  # FileNotFoundError 是IOError 的子类
#     print('客官，文件开小差了~~~')
# except IOError:  # FileNotFoundError 是IOError 的子类
#     print('客官，文件开小差了~~~')
# except IOError:  # FileNotFoundError 是IOError 的子类
#     print('客官，文件开小差了~~~')
# except ZeroDivisionError:
#     print('亲，分母不能为零哦~')

# except (IOError,ZeroDivisionError) as reason:  # FileNotFoundError 是IOError 的子类
#     print('客官，文件开小差了~~~',reason)

# except ZeroDivisionError:
#     print('分母不能为零哦~')
# except Exception:
#     print('出错了~~~')

except:
    print('出错了，呵呵~')



============================
try:
    f=open(r'__init__.py')
    1/0
    f.read()
except (FileNotFoundError,ZeroDivisionError):
    print('亲，出错了~')
finally:
    f.close()
    print('this is finally')
    
================================
try:
    with open(r'hehe.txt') as f:
        f.read()

except FileNotFoundError:
    try:
        1/0
    except ZeroDivisionError:
        print('分母不能为零')
finally:
    try:
        1 / 0
    except ZeroDivisionError:
        print('分母不能为零-finally')
~~~

---

* raise语句

~~~markdown
1. raise：可以主动抛出一个异常
		1. 如果抛出的是自带的异常，用于流程控制
		2. 如果抛出的自定义异常，用于业务处理
2. 语法：
		raise 异常类(异常提示信息) 
~~~

* 自定义异常

~~~markdown
1. 自己写的异常类---自定义异常

语法：
class 自定义异常类名（BaseException）：
		pass
2. 注意：
		BaseException：是所有异常的父类
		自定义的异常类，必须直接或间接的继承于BaseException
3. 异常的具体信息，应该以异常类的构造参数传入
~~~

~~~python
# 抢票，异常：票卖光了异常
# class TicketSaledOutError(BaseException):
#     pass

class TicketSaledOutError(ZeroDivisionError):
    def __init__(self,str):
        super().__init__(str)

# raise TicketSaledOutError()

# try:
#     raise TicketSaledOutError('亲，车票卖光了~')
#
# except TicketSaledOutError as reason:
#     print(reason)

raise TicketSaledOutError('亲，车票卖光了~')
~~~

---

