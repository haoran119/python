'''
函数参数

Python3 函数 | 菜鸟教程 (runoob.com)
https://www.runoob.com/python3/python3-function.html

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
  不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
  可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
  不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
  可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

# -*- coding: utf-8 -*-
"""
@author: hao
"""

def myfun1(x):
      x.append(1)

def myfun2(x):
      x += [2]

def myfun3(x):
      x[-1] = 3

def myfun4(x):
      x = [4]

def myfun5(x):
      x = [5]
      return x

# create a list
mylist = [0]
print(mylist)     # [0]

# change list
myfun1(mylist)
print(mylist)     # [0, 1]

# change list
myfun2(mylist)
print(mylist)     # [0, 1, 2]

# change list
myfun3(mylist)
print(mylist)     # [0, 1, 3]

# did NOT change list
myfun4(mylist)
print(mylist)     # [0, 1, 3]

# return a new list
mylist = myfun5(mylist)
print(mylist)     # [5]


def myfun(x=[1,2]):
      x.append(3)
      return x

print(myfun())    # [1, 2, 3]

# result is not [1, 2, 3] coz x was changed
print(myfun())    # [1, 2, 3, 3]
