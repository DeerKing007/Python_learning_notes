# 文件

~~~markdown
存储：1. 运行内存  2. 永久存储（硬盘）
硬盘：机械硬盘（5400r  7200r 固态硬盘---sata3：6GB/s  m.2:32GB/s）
		存储内容多，内容不丢失---读写速度低
运行内存： DDR3 DDR4  
		存储内容相对较少，一旦重启，或断电，所有数据全部丢失，读写速度高
		
保存：ctrl+s  
~~~

* 常见的文件形式

~~~markdown
.exe .txt .py .pdf .avi .mp4  .rmvb  .rm .ppt  .excl  .jpg .png
后缀的作用：仅用于识别该文件的打开方式
~~~

* 打开文件

~~~Markdown
1. open(file, mode='r', buffering=-1, encoding=None)函数
		作用：打开一个（I/O流），并返回一个文件对象
		流：stream，数据传输资源
		file：文件的路径+文件名---str
		mode：打开文件的模式，默认是只读
		encoding:设置编码---只用于文本文件
		buffering:设置缓冲区
			缓冲区会在IO操作结束强制flush（清空缓存）
			0：关闭缓冲区
			1：打开缓冲区
			大于1的整数：设置缓冲区大小为该数---1024上下
			小于0：缓冲区大小交给系统负责
~~~

| 模式 | 描述                        |
| ---- | --------------------------- |
| r    | 只读                        |
| rb   | 以二进制形式只读            |
| r+   | 读写 如果文件不存在，则报错 |
| w    | 只写 覆盖写                 |
| wb   | 以二进制形式只写            |
| w+   | 读写 如果文件不存在，则创建 |
| a    | 追加写                      |
| a+   | 读写                        |
| ab   | 以二进制形式追加写          |

~~~python
file=open(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件\hehe.txt','w')

file.write('白日依山尽\n黄河入海流\n欲穷千里目\n更上一层楼')

file.close()
~~~

---

* 文件对象的属性

~~~markdown
1. closed：
		判断流是否是关闭状态
2. mode：
		查看当前文件打开的模式
3. name：
		查看文件的名字
		
文件的全路径：
		全路径=绝对路径
		win：挂载点+文件目录+文件名+后缀
		mac/linux:文件目录+文件名+后缀
~~~

* 文件对象的方法

~~~markdown
1. close():
		关闭流，关闭资源，关闭文件
		1. 任何资源都要及时关闭，释放资源
		2. close（）之后不能进行I/O操作
2. read([size=-1])
		按字符读取，size不做设置时，表示全部读出，如果设置具体的值，则按照该值的字符数进行读取
		1. 换行符也占用一个字符
		2. 文件指针：记录文件读取的位置
3. readline（[size=-1]）
		按照字符读取一行（包括换行符）
4. readlines（）
		读取每一行字符串，返回一个列表
5. tell（）
		返回文件指针的位置
		1. 中文和转义字符：占用两个字节（一个字符）
		2. 英文占用1个字节（一个字符）
		3. 一个字节由8位构成
6. seek（offset[,from]）：
		修改文件指针的位置
        从from位置移动offset个字节
        from：0-从起始位置  1-从当前位置  2-从结尾位置
        offset：挪动的字节数
7. write（str）
		将字符串写出到文件中
8. writelines(seq):
		将seq中的字符串元素写出到文件中
9. flush（）
		刷新文件内部缓存（缓冲区），直接将内部缓冲区的数据立刻写入到文件中，并清空该缓冲区---强制flush
		1. 调用close（）时，不仅仅是释放了资源，同时还可以将文件强制保存
		2. flush（）相当于手工保存，但是不会关闭资源
~~~

---

* os模块

~~~Markdown
os：操作系统 Operation System 
os模块的作用：和操作系统打交道
导入os模块： import os
~~~

~~~python
import os
path=r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件'
# print(os.getcwd())# 返回当前工作目录
# os.chdir(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\模块')# 改变工作目录
# print(os.getcwd())

# print(os.listdir(path))# 列举制定目录下的所有文件
# os.mkdir(path+r'\a') # 创建单层目录
# os.makedirs(path+r'\a\b') # 递归的创建多层目录
# os.remove(path+r'\hehe2.txt') # 删除文件
# os.rmdir(path+r'\a\c')  # 删除单层目录--如果目录中有文件，则报错
# os.removedirs(path+r'\a\b') # 递归的删除多层目录--如果目录中有文件，则报错
# os.rename(path+r'\hehe.txt',path+r'\hehe2.txt')
# print(os.getcwd())
# os.chdir(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\模块')
# os.rename(r'hehe2.txt',r'hehe.txt') # 相对路径

# 相对路径： 相对于当前文件的路径（系统会自动的将当前文件的路径填充到相对路径上）---当前文件的路径：工作路径
# 绝对路径：从挂载点开始到文件名+后缀

# os.system('mspaint') # 运行操作系统中的shell命令

# print(os.curdir) # 当前目录---同   .:表示当前目录
# os.rename(r'.\hehe2.txt',r'.\hehe.txt')
# print(os.pardir)  # ..:表示上一级目录
# os.rename(r'..\文件\hehe.txt',r'..\文件\hehe2.txt')

# print(os.sep)# 打印当前操作系统的路径分隔符
# print(os.linesep) # 打印当前操作系统的换行符
# print(os.name) # 打印当前操作系统的名字  nt:windows OS  posix:mac/linux/Ngix
~~~

* os.path模块

~~~markdown
os.path和os 没关系 
和路径相关的操作
~~~

~~~python
import os.path as p,time
path=r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件\hehe2.txt'
# print(p.basename(path))  # 返回文件名+后缀
# print(p.dirname(path)) # 返回文件路径--绝对路径
# print(p.join('C:\\','a','b')) # 动态的将多个路径合成一个路径
# print(p.split(path)) # 返回一个元组：（路径，文件名+后缀）
# print(p.getsize(path)) # 返回一个文件的大小
# print(time.localtime(p.getatime(path)))  # 返回文件的最近访问的时间
# print(time.localtime(p.getctime(path)))  # 返回文件的创建时间
# print(time.localtime(p.getmtime(path)))  # 返回文件的最近修改的时间
# print(p.exists(path)) # 判断文件是否存在
# print(p.isabs(path))  # 判断是否绝对路径
# print(p.isabs(r'hehe2.txt'))
# print(p.isdir(path))  # 判断是否是路径
# print(p.isdir(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件'))
# print(p.isfile(path)) #判断是否是文件

# print(p.ismount('G:\\')) # 判断是否是挂载点

# print(p.samefile(path,r'hehe2.txt')) # 判断两个路径中的文件是否是同一个文件
~~~

---

### 永久存储

~~~markdown
存在硬盘中---永久存储
~~~

* pickle模块

~~~Markdown
pickle：腌菜，酸黄瓜
放入：dump，pickling
取出：unpickling
~~~

* 写文件

~~~python
import pickle
l=[1,2,3] # 对象---不是字符串---字节流

f=open(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件\zhang3.hehe','wb')

pickle.dump(l,f)

f.close()
~~~

* 读文件

~~~Python
import pickle

f=open(r'C:\Users\Administrator\PycharmProjects\AI145\com\baizhi\ai145\文件\zhang3.hehe','rb')

print(pickle.load(f))

f.close()

~~~

* 补充：

~~~markdown
按照功能分：
1. 字节流：
		以二进制形式传输对象---可以传任何对象
		如果要传文本，需要利用桥转换流，或二进制字符串（bytes）
2. 字符流：
		以字符串形式传输文本--只能传文本
		字符流的传输效率高于字节流
		
如果传输的是文本，要使用字符流
如果传输的不是文本（任何不是文本的对象），要用字节流
		如果使用字节流传出，必须使用二进制模式传输---序列化
		pickle是对象序列化之后存储的一种手段
~~~

* 补充

~~~markdown
with-open语句
帮助自动的关闭资源（流）
~~~

~~~python
with open(r'hehe2.txt','r') as f:
    print(f.read())
~~~

---

