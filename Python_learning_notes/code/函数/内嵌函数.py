def outer():
    a=10
    def inner():
        a+=1
        print('hello world')
    inner()

outer()

