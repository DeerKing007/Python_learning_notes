# else 语句

~~~markdown
1. if-else
2. if-elif-else
3. for-else
		当循环正常结束时，else才会执行
		如果循环过程中，强制终止了循环，else不会执行
4. while-else
		当循环正常结束时，else才会执行
		如果循环过程中，强制终止了循环，else不会执行
5. try-except-else
		当try结构中没有任何异常，则会执行else结构
		如果try中有异常，则不会执行
6. try-except-else-finally
		当try结构中没有任何异常，则会执行else结构
		如果try中有异常，则不会执行
		finally一定出现在else之后
~~~

~~~python
# for - else

# for i in range(10):
#     if i==3:
#         # print('hehe')
#         break
# else:
#     print('循环结束')

count=0
while count<=10:
    count+=1
    if count==3:
        # break
        continue
else:
    print('循环结束')
====================================

# try:
#     print('程序开始')
#     raise Exception()
# except Exception:
#     print('出错了~~~')
# else:
#     print('程序结束')

try:
    print('程序开始')
    # raise Exception()
except Exception:
    print('出错了~~~')
else:
    print('程序结束')
finally:
    print('this is finally')
~~~

