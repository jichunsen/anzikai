# 老男孩Python全栈13期练习题 考试时间4h
# 一、简答题(30)
# 1、常用字符串格式化的方式有哪些?并说明他们的区别(4)
# '{}'.format('')
# s1 = '%s'% ''
# s2 = '77'
# s3 = f'22{s2}'
# print(s3)
# 2、L = range(100) （4分）
# 1) 取第一到第三个元素_______
# L = range(100)
# print(list(L)[0:3])
# 2) 取倒数第二个元素_______
# print(list(L)[-2])
# 3) 取后十个元素_______
# print(list(L)[90:])
# 4) 把L复制给L1用_______
# 3、解释python中深拷贝和浅拷贝的区别(2)
'''浅拷贝：不管多复杂的数据结构，浅拷贝都只会copy一层。
深拷贝：深拷贝则不管数据结构多么复杂，只要遇到可能发生改变的数据类型，就会重新开辟一块儿内存空间把内容复制下来
        直到最后一层，不再有复杂的数据类型，就保持其原引用。'''
# 4、Python中定义函数时如何书写可变参数和关键字参数？(2)
# *arg **kwargs
# 5、装饰器是什么时候被执行的(3)
# 装饰器是在程序加载的时候被执行。（解析器加载代码监测到@符号，执行装饰器外层函数，返回inner，被装饰函数被调用，
# 实则调用inner函数，inner是在程序运行之前执行的。）
# 6、简述面向对象的三大特性分别是什么，以及主要功能(5)
# 封装 继承 多态
# 封装：隐藏对象的属性 和 实现细节，仅对外提供公共访问方式
# 继承：子类自动共享父类数据结构和方法机制。单继承，多继承
# 多态：多态是指相同的操作或函数、过程可作用于多种类型的对象上，并获得不同的结果。
#       不同的对象，收到同一消息可以产生不同的结果，这种现象称为多态性；
# 7、利用python打印指定时间的时间戳时间，时间为"1989-12-25"（面试题）(4)
# import time
# s = time.strptime('1989-12-25','%Y-%m-%d')
# print(s)
# t = time.mktime(s)
# print(t)
# print(time.time())
# 8、python中如何实现随机整数的取值？默认的随机数范围是多少？(2)
# import random
# print()
# 9、在类中使用classmethod装饰的方法被存储在哪块内存中,使用什么调用？参数有什么特点？(3)

# 存在内存中，用cls 调用


# 10、说明__init__和__new__的作用(2)
# 实例化的时候先执行__new__,执行__new__方法决定了实例化了一个什么类型的对象，
# 再执行__init__，执行__init__用来为每个实例对象定制自己的特征
# 11、简述反射是怎么回事？(3)
# 主要是指程序可以访问、检测、和修改它本身状态或行为的一种能力（自省）
# 12、新式类和经典类(旧式类)的区别(4)一种一分
# 13、如何使用python删除一个文件（2）




# 二、读程序(20)
# 1、下面程序的输出结果是：（3分）
# d = lambda p: p * 2
# t = lambda p: p * 3
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
# print (x)


# 2、以下的代码的输出将是什么:___(3分)
#
# def extendList(val,list = []):
# list.append(val)
# return list
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList(‘a’)
# print “list1 = % s” % list1
# print “list2 = % s” % list2
# print “list3 = % s” % list3


# 3、sum的结果是多少？（3）
# kvps = {'1':1,'2':2}
# theCopy = kvps
# print(theCopy)
# kvps['1'] = 5
# print(theCopy)
# sum = kvps['1'] + theCopy['1']
# print(sum)

# 4、自定义一个类，并实例化。使用反射给对象添加一个属性name，值为你的名字。使用反射查看name的值。(5分)
# class A():
#     def __init__(self,name,sex,hp):
#         self.name= name
#         self.sex=sex
#         self.hp=hp
# a= A('哈哈','男',30)
# print(getattr(a,'name'))
# 5、读程序，使用注释标注执行顺序，并说出下列代码的结果以及产生这样结果的原因？(4)
# class Base:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print('in base')
#
# class A(Base):
#     Country = 'China'
#     print(Country)
#
#     def func(self):
#         print('in A')
#
# A()

# 6、简述下列代码的输出以及输出的原因(2)
# class A:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,new_name):
#         print(new_name)
#
# obj = A('alex')
# obj.name = 'egon'
# print(obj.name)


# 三、编程题(50)
# 1、用至少2种不同的方式删除一个list里面的重复元素,列表如下:(5)
# 	a = [1, 2, 2, 4, 34, 3, 4, 56, 65, 456, 5, 6456, 456, 54, 45, 6, 464, 564](5)

# 2、使用python简单实现打印九九乘法表(5)
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # print('%s * %s = %s' % (j, i, i * j), end='\t')
#         print('{} * {} = {}'.format(i, j, i * j), end='   ')
    # print(   '          '   )

# 3、写一个单例模式(5)
class Base:
    __a = None

    # 写法1：
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'__a'):
            cls.__a = object.__new__(cls)
        return cls.__a

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


# 5、斐波那契数列1, 2, 3, 5, 8, 13, 21.....根据这样的规律，编程求出400万以内最大的斐波那契数，并求出他是第几个斐波那契数。(5)
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4, "f": "hello"}
dict2 = {"b": 3, "d": 5, "e": 7, "m": 9, "k": "world"}

# 6、要求写一段代码，实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串就拼接，如上示例得到结果为：（5）
# dictc = {"a": 1, "b": 5, "c": 3, "d": 9, "e": 7, "m": 9, "f": "hello", "k": "world"}
def add_dic(dic1, dic2):
    for i in dic2:
        if i in dic1:
            dic1[i] = dic1[i] + dic2[i]
        else:
            dic1[i] = dic2[i]
    return dic1


print(add_dic(dict1, dict2))

# 7、写函数完成抢"拼手气"红包函数，用户输入红包金额和个数，返回随机的红包金额，使得规定个数红包的总额达到红包金额。(5)

# 8、写函数完成计算文件夹大小的需求,文件夹中可能还有其他文件和文件夹(5)


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
# def select(data, fields):
#     # TODO:implementation
#     return result
#
# 2.以下代码的输出是什么？请给出答案并解释。
# def multipliers():
#     return [lambda x: i * x for i in range(4)]
#
# print(m\[m(2)
# for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。
#

#     •    现有两元组(('a'), ('b')), (('c'), ('d')), 请使用python中匿名函数生成列表[{'a': 'c'}, {'b': 'd'}]
#
#     •    请描述unicode, utf - 8, gbk等编码之间的关系？
#
#     •    什么是装饰器？写一个装饰器，可以打印输出方法执行时长的信息