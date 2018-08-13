# 老男孩Python全栈13期练习题 考试时间4h
# 一、简答题(30)
# 1、常用字符串格式化的方式有哪些?并说明他们的区别(4)
s1 = ' {} '.format('  ')
s2 = 'aaa%s' % '666'
s3 = '777'
s4 = f'888{s3}'
print(s1, s2, s4)
# 2、L = range(100) （4分）
# 1) 取第一到第三个元素_______
L = range(100)
list(L[0:3]), tuple(L[0:3]), set(L[0:3])
# 2) 取倒数第二个元素_______L[-2]
print(L[-2])
# 3) 取后十个元素_______L[-10:-1]
print(list(L[-10:]))
# 4) 把L复制给L1用_______L1 = L[:]
L1 = L[:]
L2 = L
print(L1, L2, id(L1), id(L2))
# 3、解释python中深拷贝和浅拷贝的区别(2)
"""
浅拷贝：不管多复杂的数据结构，浅拷贝都只会copy一层。
深拷贝：深拷贝则不管数据结构多么复杂，只要遇到可能发生改变的数据类型，就会重新开辟一块儿内存空间把内容复制下来
        直到最后一层，不再有复杂的数据类型，就保持其原引用。
"""
# 4、Python中定义函数时如何书写可变参数和关键字参数？(2)
# 可变参数：*args；关键字参数：**kwargs
# 5、装饰器是什么时候被执行的(3)
# 装饰器是在程序加载的时候被执行。（解析器加载代码监测到@符号，执行装饰器外层函数，返回inner，被装饰函数被调用，
# 实则调用inner函数，inner是在程序运行之前执行的。）
# 6、简述面向对象的三大特性分别是什么，以及主要功能(5)
# 封装、继承、多态。
# 封装：隐藏对象的属性和实现细节，仅对外提供公共访问方式；
# 继承：子类自动共享父类数据结构和方法的机制。单继承、多继承；
# 多态：多态是指相同的操作或函数、过程可作用于多种类型的对象上，并获得不同的结果。
#       不同的对象，收到同一消息可以产生不同的结果，这种现象称为多态性；
# 7、利用python打印指定时间的时间戳时间，时间为"1989-12-25"（面试题）(4)
import time

s = time.strptime('1989-12-25', '%Y-%m-%d')
t = time.mktime(s)
print(t)
# 8、python中如何实现随机整数的取值？默认的随机数范围是多少？(2)
import random

print(random.randint(1,10))  # 取值范围取决于randint里的参数


# 9、在类中使用classmethod装饰的方法被存储在哪块内存中？使用什么调用？参数有什么特点？(3)
# 存在定义类的内存中；使用类名调用；必须有cls，不能用self；
# 10、说明__init__和__new__的作用(2)
# 实例化的时候先执行__new__,执行__new__方法决定了实例化了一个什么类型的对象，
# 再执行__init__，执行__init__用来为每个实例对象定制自己的特征
# 11、简述反射是怎么回事？(3)
# 主要是指程序可以访问、检测、和修改它本身状态或行为的一种能力（自省）
# python面向对象中的反射：通过字符串的形式操作对象相关的属性。python中的一切事物都是对象（都可以使用反射）
# 四个可以实现自省的函数：hasattr、getattr、setattr、delattr
# 12、新式类和经典类(旧式类)的区别(4)一种一分
# 默认继承：新式类默认继承object；经典类则可以通过继承object和不继承object定义不同的类。
# 新式类继承：广度优先；经典类继承：深度优先
# 13、如何使用python删除一个文件（2）
# os.remove(filename)


# 二、读程序(20)
# 1、下面程序的输出结果是：（3分）
d = lambda p: p * 2
t = lambda p: p * 3
x = 2
x = d(x)
x = t(x)
x = d(x)
print (x)
# 在python2中运行结果是24
# 在python3中运行结果报错


# 2、以下的代码的输出将是什么:___(3分)
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
# print(list1, list2, list3) 运行结果：[10, 'a'] [123] [10, 'a']
# print “list1 = % s” % list1
# print “list2 = % s” % list2
# print “list3 = % s” % list3


# 3、sum的结果是多少？（3）
# Kvps = {‘1’:1,’2’:2}
# theCopy = kvps
# kvps[‘1’] = 5
# sum = kvps[‘1’] + theCopy[‘1’]
# Print sum
# 运行结果是：10

# 4、自定义一个类，并实例化。使用反射给对象添加一个属性name，值为你的名字。使用反射查看name的值。(5分)
# class A:
#     def __init__(self):
#         pass
#
#
# a = A()
# setattr(a, 'name', '666')
# print(getattr(a, 'name'))
# 5、读程序，使用注释标注执行顺序，并说出下列代码的结果以及产生这样结果的原因？(4)
# py文件的执行顺序
class Base:  # 1 python3解释器下，默认继承object并创建一个类空间
    def __init__(self):  # 2 Base类定义__init__方法，实例化时才调用此方法，并执行方法内的代码  # 9 被第8步调用
        self.func()  # 10 执行self.func()，self是指A()，所以会调用class A 的func()方法

    def func(self):  # 3 Base类定义（封装）一个方法
        print('in base')


class A(Base):  # 4 创建命名空间"A"继承Base
    Country = 'China'  # 5 给当前类封装一个静态属性
    print(Country)  # 6 执行print函数

    def func(self):  # 7 给当前类封装一个方法，调用此方法，才执行此方法内的代码。   # 11 func()被第10步调用，执行func()
        print('in A')  # 执行print函数


A()  # 8 实例化A，触发A的__init__方法。A中没有，用其父类的。
"""
代码执行结果：
China
in A
"""

# 6、简述下列代码的输出以及输出的原因(2)
class A:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print(new_name)
#
#
# obj = A('alex')  # 实例化对象A，触发A的__init__方法，给obj对象设置一个私有属性并把alex赋值给这个属性
# obj.name = 'egon'  # @property把属性变方法，obj.name = 'egon'会触发@name.setter装饰的name属性，执行print函数，打印传进来的egon
# print(obj.name)  # @property属性变方法，obj.name触发@property装饰的name函数，函数返回值是self.__name,实例化obj对象时设置了__name为alex


# 三、编程题(50)
# 1、用至少2种不同的方式删除一个list里面的重复元素,列表如下:(5)
# a = [1, 2, 2, 4, 34, 3, 4, 56, 65, 456, 5, 6456, 456, 54, 45, 6, 464, 564]
# 方式一：list(set(a))
# 方式二：
# l = []
# [l.append(i) for i in a if i not in l]
# print(l)

# 2、使用python简单实现打印九九乘法表(5)
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%s * %s = %s' % (j, i, i * j), end='\t')
#         # print('{} * {} = {}'.format(i, j, i * j), end='   ')
#     print()


# 3、写一个单例模式(5)
# 单例模式是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
# 课上示例
class A(object):
    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(A, '_instance'):
            A._instance = A(*args, **kwargs)
        return A._instance


aa = A()
bb = A()
print(aa, bb)


# 进阶写法
class Base:
    __a = None

    # 写法1：
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls,'__a'):
    #         cls.__a = object.__new__(cls)
    #     return cls.__a

    # 写法2：
    # def __new__(cls, *args, **kwargs):
    #     return cls.__a if cls.__a else object.__new__(cls)


a = Base()
b = Base()
print(a, b)

# 4、面向对象编程(15)
"""
一：定义一个学生类。有下面的类属性：
1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
zm = Student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100
"""

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        try:
            return int(self.age)
        except ValueError:
            return '输入的年龄不是整数'

    def get_course(self):
        try:
            return max(self.score)
        except TypeError:
            return '输入的成绩格式不合法'


zm = Student('zhangming', 20, [69, 88, 100])
print(zm.get_name(), zm.get_age(), zm.get_course())

# 5、斐波那契数列1, 2, 3, 5, 8, 13, 21.....根据这样的规律，编程求出400万以内最大的斐波那契数，并求出他是第几个斐波那契数。(5)
a, b = 1, 2
count = 1
while b < 4000000:
    a, b = b, a + b
    count += 1
print(f'{a}是400万以内最大的斐波那契数，是第{count}个斐波那契数')


# 6、要求写一段代码，实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串就拼接，如上示例得到结果为：（5）
dicta = {"a": 1, "b": 2, "c": 3, "d": 4, "f": "hello"}
dictb = {"b": 3, "d": 5, "e": 7, "m": 9, "k": "world"}


# dictc = {"a": 1, "b": 5, "c": 3, "d": 9, "e": 7, "m": 9, "f": "hello", "k": "world"}
def add_dic(dic1, dic2):
    for i in dic2:
        if i in dic1:
            dic1[i] = dic1[i] + dic2[i]
        else:
            dic1[i] = dic2[i]
    return dic1


print(add_dic(dicta, dictb))


# 7、写函数完成抢"拼手气"红包函数，用户输入红包金额和个数，返回随机的红包金额，使得规定个数红包的总额达到红包金额。(5)
import random


def user_enter():
    money = input('拼手气红包，请输入红包金额：')
    number = input('拼手气红包，请输入红包个数：')
    return money, number


try:
    money, number = user_enter()
    money_, number_ = int(money), int(number)
except ValueError:
    print('红包金额与个数请输入整数')
    user_enter()


def red_envelopes(money, number):
    l = []
    while number > 1:
        s = round(random.uniform(0.0, (2 * money / number)), 2)
        money -= s
        number -= 1
    l.append(round(money, 2))
    return l


print('您自己抢到的红包为：{}'.format(red_envelopes(money_, number_)))


# 8、写函数完成计算文件夹大小的需求,文件夹中可能还有其他文件和文件夹(5)
import os
def get_size(file_path):
    ret = os.listdir(file_path)
    total = 0
    for name in ret:
        abs_pass = os.path.join(file_path, name)
        if os.path.isdir(abs_pass):
            total += get_size(abs_pass)
        else:
            total += os.path.getsize(abs_pass)  # 计算文件的大小
    return total


print(get_size(os.getcwd()))

# 附加题（20）
# 1.有一个数据结构如下所示，请编写一个函数从该结构数据中返回由指定的字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
# data:{"time": "2016-08-05T13:13:05",
#       "some_id": "ID1234",
#       "grp1": {"fld1": 1,
#                "fld2": 2},
#       "xxx2": {"fld3": 0,
#                "fld5": 0.4},
#       "fld6": 11,
#       "fld7": 7,
#       "fld46": 8}
# fields:由
# "|"
# 连接的以
# "fld"
# 开头的字符串, 如:fld2 | fld3 | fld7 | fld19
#
#
def select(data, fields):
    # TODO:implementation
    return result
#
# 2.以下代码的输出是什么？请给出答案并解释。
def multipliers():
    return [lambda x: i * x for i in range(4)]

print(m\[m(2)
for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。
#

#     •    现有两元组(('a'), ('b')), (('c'), ('d')), 请使用python中匿名函数生成列表[{'a': 'c'}, {'b': 'd'}]
#
#     •    请描述unicode, utf - 8, gbk等编码之间的关系？
#
#     •    什么是装饰器？写一个装饰器，可以打印输出方法执行时长的信息
