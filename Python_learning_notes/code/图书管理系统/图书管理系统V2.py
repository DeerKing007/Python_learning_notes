# # 需求
# 用户
    #登录
        # 账号，密码
    #注册
        # 账号，密码+密码确认
# 书籍
    # 查询所有书籍
    # 根据类别查询书籍
    # 根据价格查询书籍
    # 根据书名查询一本书
    # 修改一本书的信息
        # 获取书名信息
        # 修改书籍的内容
    # 删除一本书
        # 获取书籍信息
        # 确认
    # 添加一本书
        # 输入书籍信息

###################################################
userDB=None
bookDB=None
def initDB():
    global userDB
    userDB = [['admin', '123'], ['zhang3', '123'], ['li4', '123']]
    global bookDB
    bookDB = [['《Python丛书》', '计算机', 'guido', 9.99, '看不懂'],
              ['《天龙八部》', '武侠小说', '金庸', 19.99, '很好看'],
              ['《西游记》', '古典小说', '吴承恩', 99.99, '很好看'],
              ['《三少爷的剑》', '武侠小说', '古龙', 9.99, '很好看'],
              ['《鬼吹灯》', '悬疑小说', '不详', 19.99, '看不懂'],
              ['《高等数学(上)》', '大学教材', '贾鹂', 49.99, '完全看不懂'],
              ['《风云》', '漫画', '马荣成', 9.99, '看不懂'],
              ['《盗墓笔记》', '悬疑小说', '南派三叔', 9.99, '看不懂'],
              ['《儒林外史》', '纪录历史', '司马光', 9.99, '看不懂'],
              ['《史记》', '纪录历史', '司马迁', 9.99, '看不懂']]
def librarySystem():
    pass


def login():
    while 1:
        name = input('请输入用户名：\n')
        pwd = input('请输入密码：\n')
        flag = 0
        for i in userDB:
            if i[0] == name and i[1] == pwd:
                # 登录成功，允许进入图书管理系统
                flag = 1
        if flag == 1:
        # 成功
            librarySystem()
            print('登录成功')
        else:
            print('账号或密码错误，请重新输入：')
def regist():
    while 1:
        name = input('请输入账号：\n')
        flag = 0
        # 判断是否已经被注册
        for i in userDB:
            if i[0] == name:
                flag == 1
        if flag == 1:
            print('该账号已经被注册，请更换用户名')
        else:
            break
    while 1:
        pwd1 = input('请输入密码：\n')
        pwd2 = input('请输入确认密码：\n')
        if pwd1 == pwd2:
        # 信息入库
            userDB.append([name,pwd1])
            print('注册成功')
            login()
        else:
            print('两次密码不一致，请重新输入密码')


def manager():
    print('================欢迎使用图书管理系统===================')
    while 1:
        result = input('1.登录  2.注册 \n')
        if result == '1':
            login()
        elif result == '2':
            regist()
        else:
            print('输入有误请重新输入')

# 核心主程序---任务调度，程序运行的接口
def run():
    # 初始化数据库
    initDB()
    # 启用管家，管理其他操作
    manager()

run()
















