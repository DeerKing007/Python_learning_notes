#

def shiFouYouJie(a,b,c):
    delta = b ** 2 - (4 * a * c)
    if delta>=0:
        return True
    else:
        return False

def jieFangCheng(a,b,c):
    # 判断x是否有解
    delta=b**2-(4*a*c)
    if shiFouYouJie(a,b,c):
        x1=((-b)+(delta)**0.5)/(2*a)
        x2=((-b)-(delta)**0.5)/(2*a)
        print(x1,x2)
    else:
        print('无解')

jieFangCheng(1,1,1)
jieFangCheng(1,1,-1)



