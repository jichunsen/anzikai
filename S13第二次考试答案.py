# 1 D
# 2 C
# 3 D
# 4 C
# 5 D
# 6 C
# 7 B
# 8 C
# 9 B
# 10 A
# 11 AB
# 12 BCD
# 13 BC
# 14 BD
# 15 BD


# -3
# Error
# 5
# 3
# Error
# update get
# a, b = b, a
# []
# print({i:'alex' for i in range(1, 4)})/print(dict.fromkeys([1, 2, 3], 'alex'))


# 终止函数的运行，并返回相应的返回值

# 可以被for循环遍历的可迭代对象，通过yield返回值并可以通过next取值。

# 位置参数、默认参数、动态参数；  顺序：位置参数、动态参数*args、默认参数、动态参数**kwargs。

# 在不修改原函数及其调用方式的情况下对原函数功能进行扩展

# s2 = s1.encode('utf-8').decode('utf-8').encode('gbk')

# def wrapper(func):  # 1
#     def inner(*args, **kwargs):
#         print('函数执行之前')  # 4
#         ret = func(*args, **kwargs)  # 5
#         print('函数执行之后')  # 6
#         return ret  # 7
#     return inner
#
#
# @wrapper
# def func():  # 2
#     pass
#
#
# func()  # 3


# [1, [22, 33, 44, '55'], 3, 4, 66] [1, [22, 33, 44, '55'], 3, 4, 66] [1, [22, 33, 44, '55'], 3, 4]

# l = ['alex', 'WuSir', '老男孩', '太白']
# a = [i + str(l.index(i)) for i in l]

# func = lambda x, y: [{x[0]: y[0]}, {x[1], y[1]}]
# print(func((('a'), ('b')), (('c'), ('d'))))

# alist = [{'a': 5, 'b': 2}, {'a': 2, 'b': 8}, {'a': 8, 'b': 2}]
# alist = sorted(alist, key=lambda x:x['a'])
# print(alist)

# alist = [3, 1, -4, -2]
# alist = sorted(alist, key=abs)
# print(alist)


# def func(file):
#     alist = []
#     with open(file, encoding='utf-8') as f:
#         a1, a2, a3, a4, a5 = f.__next__().strip().split()
#         for i in f.readlines():
#             b1, b2, b3, b4, b5 = i.strip().split()
#             alist.append({a1: b1, a2: b2, a3: b3, a4: b4, a5: b5})
#         print(alist)
#
#
# func('t1.txt')


# def func(file,mode,*args):
#     if mode == 'r':
#         with open(file,mode,encoding='utf-8') as f:
#             print(f.read())
#     else:
#         with open(file,mode,encoding='utf-8') as f:
#             f.write('老男孩教育')
#
#
# func('t1.txt','w')


# def func(file, *args):
#     sss = ''
#     for i in args:
#         i = i.replace(i[0], '') + '*'
#         sss += i
#     with open(file, 'a', encoding='utf-8') as f:
#         f.write(sss)
#
#
# func('t1.txt', 'asdf', 'asdf', 'asdf', 'asdf')


import time
from functools import wraps

flag = 'logout'
user_name = ''


def wrapperlogin(func):
    @wraps(func)
    def inner(*args, **kwargs):
        global flag, user_name
        if flag == 'logout':
            a = 1
            while flag == 'logout' and a < 4:
                name = input('登录认证，请输入用户名：')
                pwd = input('登录认证，请输入用密码：')
                with open('register', encoding='utf-8')as f:
                    for i in f.readlines():
                        if i.strip():
                            username, password = i.strip().split(',')
                            if name == username and pwd == password:
                                print('登录成功')
                                flag = 'login'
                                user_name = username
                                break
                    else:
                        print('账号或者密码错误，你还剩%s次输入机会' % (3 - a))
                        if a == 3:
                            quit()
                        a += 1
        ret = func(*args, **kwargs)
        return ret

    return inner


def wrapperlog(func):
    @wraps(func)
    def inner(*args, **kwargs):
        global user_name
        now_time = time.localtime()
        view_time = time.strftime('%Y-%M-%D %H:%M:%S', now_time)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('用户：%s 在 %s 执行了 %s \n' % (user_name, view_time, func.__name__))
        ret = func(*args, **kwargs)
        return ret

    return inner


def star():
    with open('t2.txt', encoding='utf-8') as f:
        for i in f.readlines():
            print(i.strip())


@wrapperlogin
def login():
    pass


def register():
    global flag
    name = input('注册账号，请输入您的姓名：')
    pwd1 = input('注册账号，请输入您的密码：')
    pwd2 = input('注册账号，请再次输入您的密码：')
    if pwd1 == pwd2:
        with open('register', 'a', encoding='utf-8') as f:
            f.write('\n' + name + ',' + pwd1)
        print('注册成功,已经为您自动登录')
        flag = 'login'
        star()


@wrapperlogin
@wrapperlog
def article():
    print('欢迎%s 访问文章页面' % user_name)


@wrapperlogin
@wrapperlog
def diary():
    print('欢迎%s 访问日志页面' % user_name)


@wrapperlogin
def comment():
    pass


@wrapperlogin
@wrapperlog
def collect():
    print('欢迎%s 访问收藏页面' % user_name)


def logout():
    global flag
    flag = 'logout'
    print('您已经成功退出。')


def dropout():
    print('您已经退出本系统。')
    quit()


def choice():
    flag1 = True
    while flag1:
        enter = input('Num:')
        if enter == '1':
            login()
        elif enter == '2':
            register()
        elif enter == '3':
            article()
        elif enter == '4':
            diary()
        elif enter == '5':
            comment()
        elif enter == '6':
            collect()
        elif enter == '7':
            logout()
        elif enter == '8':
            flag1 = False
            dropout()


star()
choice()