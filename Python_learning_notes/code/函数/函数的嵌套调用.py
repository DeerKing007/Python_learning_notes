

def fun3():
    print('thisis fun3')
    print('thisis fun3')

def fun2():
    print('this is fun2')
    fun3()
    print('this is fun2')

def fun1():
    print('this is fun1')
    fun2()
    print('this is fun1')

fun1()
