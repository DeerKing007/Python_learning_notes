def hnt(froms,to,temp,n):# 从froms柱子  到to柱子，中间利用temp柱子 n盘子的个数
    # 首先要设置收敛条件
    if n==1:
        print('%s--->%s'%(froms,to))
        return None
    else:
        # 1. n-1个盘子从froms--temp 借助to
            hnt(froms,temp,to,n-1)
        # 2. 一个盘子从froms--to
            print('%s--->%s'%(froms,to))
        # 3. n-1个盘子从temp--to 借助froms
            hnt(temp,to,froms,n-1)

hnt('A','B','C',3)