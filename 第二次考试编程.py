# def func():
#     with open('t1.txt',encoding='utf-8')as f:
#         l = []
#         a1, b1, c1, d1, e1 = f.readline().strip().split()
#         # print(a1, b1, c1, d1, e1)# 写法一
#         # print(f.__next__())  # 写法二
#         for i in f.readlines():
#             a2, b2, c2, d2, e2 = i.strip().split()
#             l.append({a1:a2,b1:b2,c1:int(c2),d1:d2,e1:e2})
#     return l
# print(func())
# a = 'abcd'
# b= 'defa'
# def main(file_path,*args):
#     for line in args:
#         new_line = line[1:]
#         with open(file_path, encoding='utf-8', mode='a') as f:
#             f.write('*'.join(new_line) + '\n')
# main('t1.txt', a, b)
#
# import  os
# def func(path,mode,*args):
#     if os.path.exists(path):
#         print("没有此文件!")
#         return None
#     if mode=="r":
#         with open(path,mode="r",encoding="utf-8") as f:
#             f.read()
#     elif mode == "w":
#         with open(path,mode="w",encoding="utf-8") as f:
#             f.write("老男孩教育")
#     elif mode == "a":
#         with open(path,mode="a",encoding="utf-8") as f:
#             f.write("老男孩教育")



def wrapperlog():
    pass


def wrapper():
    pass



@wrapper
def register():
    pass


def login():
    pass


def star():
    print("......")


def choice():
    pass