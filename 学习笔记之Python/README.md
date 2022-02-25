# 学习笔记之Python

* [Welcome to Python.org](https://www.python.org/)
  * [3.9.5 Documentation (python.org)](https://docs.python.org/3/)
  * [The Python Standard Library — Python 3.10.2 documentation](https://docs.python.org/3/library/index.html)
  * [Glossary — Python 3.9.7 documentation](https://docs.python.org/3/glossary.html#glossary)
  * [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
  * [Programming FAQ — Python 3.9.6 documentation](https://docs.python.org/3/faq/programming.html)
  * [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
* [Python（计算机编程语言）_百度百科 (baidu.com)](https://baike.baidu.com/item/Python/407313?fr=aladdin#reference-[12]-21087-wrap)
  * 自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和Web编程。
  * Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
  * Python允许像数学的常用写法那样连着写两个比较运行符。比如a < b < c与a < b and b < c等价。C++的结果与Python不一样，首先它会先计算a < b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。
  * Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。
* [Python Technologies Tutorials](https://www.tutorialspoint.com/python_technologies_tutorials.htm)
  * [Python 3 Tutorial](https://www.tutorialspoint.com/python3/index.htm)
* [Python3 教程 | 菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)
* [Python 入门指南 — Python tutorial 3.6.0 documentation](http://www.pythondoc.com/pythontutorial3/index.html)

## NOTES

* [python/面试总结之Python at main · haoran119/python](https://github.com/haoran119/python/tree/main/%E9%9D%A2%E8%AF%95%E6%80%BB%E7%BB%93%E4%B9%8BPython)
* [学习笔记之盘一盘 Python 系列 1 & 2 - 入门篇 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11289321.html)
* [学习笔记之Python开发环境 IDE ( Anaconda / PyCharm ) - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/8915306.html)
* [学习笔记之Python 3 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/10825575.html)
* [学习笔记之Django - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11556233.html)
* [学习笔记之pytest - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/13769672.html)
	* [5 分钟快速上手 pytest 测试框架](https://mp.weixin.qq.com/s/uOUG5fqHqPWMckCa5WOC4Q)
* [《Python入门必备指南》之如何系统地自学 Python？_腾讯课堂](https://ke.qq.com/course/217064)
  * 通过实例知道下list，dict实际使用中一些技巧
  * 了解web编程的学习线路图，知识网络
  * get(key[, default])
    * https://docs.python.org/3/library/stdtypes.html?highlight=get#dict.get
    * Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError. 
  * [sorted(iterable, *, key=None, reverse=False)](https://docs.python.org/3/library/functions.html?highlight=sorted#sorted)
    * Return a new sorted list from the items in iterable.
    * key specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). The default value is None (compare the elements directly).
    * reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
    * Use functools.cmp_to_key() to convert an old-style cmp function to a key function.
    * [functools — Higher-order functions and operations on callable objects — Python 3.9.6 documentation](https://docs.python.org/3/library/functools.html#functools.cmp_to_key)
      * Transform an old-style comparison function to a key function. Used with tools that accept key functions (such as sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()). This function is primarily used as a transition tool for programs being converted from Python 2 which supported the use of comparison functions.
      * A comparison function is any callable that accept two arguments, compares them, and returns a negative number for less-than, zero for equality, or a positive number for greater-than. A key function is a callable that accepts one argument and returns another value to be used as the sort key. 
    * [key function - Glossary — Python 3.9.6 documentation](https://docs.python.org/3/glossary.html#term-key-function)
      * A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions.
    * [Sorting HOW TO — Python 3.9.6 documentation](https://docs.python.org/3/howto/sorting.html#sortinghowto)
      * Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
    ```python
    import functools

    bids = [[1, 5, 0], [2, 7, 8], [3, 5, 2], [4, 3, 3]]

    # ORDER BY bids[1] DESC, bids[2] ASC
    def compare(x, y):
        if x[1] != y[1]:
            return y[1] - x[1]
        else:
            return x[2] - y[2]

    sorted_bids = sorted(bids, key=functools.cmp_to_key(compare))

    print(sorted_bids)  # [[2, 7, 8], [1, 5, 0], [3, 5, 2], [4, 3, 3]]
    ```
  * items()
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dict.items
    * Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
  * 4.7.5. Lambda Expressions
    * https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions
    * Small anonymous functions can be created with the lambda keyword.
	```python
	#!/usr/bin/python3

	res = {}
	with open('demo.txt') as f:
			for ch in f.read().replace(' ', ''):
		res[ch] = res.get(ch, 0) + 1

	# lambda x[1] stands for value in dictionary, x[0] stands for key in dictionary
	for char, num in sorted(res.items(), key=lambda x: x[1], reverse=True)[:3]:
			print('char %s count is %d' % (char, num))
	```
* [深入浅出带你学Python冲击年薪30万【马哥教育】_腾讯课堂](https://ke.qq.com/course/134017)
  * Python哲学
    * import this
  * Python使用引用计数记录所有变量的引用数
    * 当变量引用数变为0，它就可以被垃圾回收GC。
    * 计数增加：赋值给其他变量就增加引用计数。E.g. x = 3; y = x;
    * 计数减少：
      * 函数运行结束时，局部变量就被自动销毁，对象引用计数减少；
      * 变量被赋值给其他变量。x = 3; y = x; x = 4;

## RESOURCES

* [在 Windows 上使用 Python 进行开发 - Windows apps | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/python/)
* [网络课程 python 网络教育-百度传课](https://chuanke.baidu.com/course/_python_____.html)
* [Python Example](https://www.programcreek.com/python/)
* [一文总结学习 Python 的 14 张思维导图 - 人工智能与大数据技术](https://mp.weixin.qq.com/s/yuxqP0cNsUgYnfLlStEQ5Q)
  * https://woaielf.github.io/2017/06/13/python3-all/
  * 本文主要涵盖了 Python 编程的核心知识（暂不包括标准库及第三方库，后续会发布相应专题的文章）。
  * 第1张图
    *   基础知识图一包括了基本规则、Python语言特点、计算机语言、如何运行Python、变量赋值五个方面，辅助你快速掌握Python编程的基底知识。
  * 第2张图
    *   基础知识图二包含了模块结构、布局、IO编程流程、标识符、Python对象、内存管理、动态类型六大模块，两张基础知识导图可以帮助你区域化了解Python的组成部分及基本操作。
  * 第3张图
    *   学习Python少不了对数据的了解，这张图整理了数据类型的分类、作用、空值、标准数据、if语句等等模块。
  * 第4张图
    *   这张图整理了序列的有序排列、标准操作符与序列类型操作符的重点知识，以及可操作性的BIF。
  * 第5张图
    *   字符串是个比较庞大而精细的部分，接着上图的BIF可分为标准类型、序列类型、字符串类型，字符串可分为五种操作符类型，此图还整理了序列的独特特性以及编码问题，可以说很详细了。
  * 第6张图
    *   关于列表|元素，首先说拷贝问题，分深浅拷贝两种形式。tuple的内建函数、特殊特性与list的操作符、内建函数是重点部分。
  * 第7张图
    *   这张图主要整理了字典|集合中set、dict的功能、分类、BIF、操作问题。
  * 第8张图
    *   条件|循环包含生成器、迭代器、列表解析的使用、拓展，相关BIF、if语句循环控制也能够快速掌握重点。
  * 第9张图
    *   关于文件对象内建方法、内建函数、内建属性都有具体内容，文件迭代的运用，标准文件对象如何输入输出以及分隔符的运用都在导图中详细标明。
  * 第10张图
    *   错误|异常这张图的点介绍了如何调试、处理异常情况。
  * 第11张图
    *   函数一介绍了函数概述，注意vs函数的引用、调用，装饰器的定义、“堆叠”。参数具有自己的完整语法以及自己的传递方式。
  * 第12张图
    *   函数二图整理了递归函数、返回（回调）函数、变量作用域、偏函数、函数式编程、匿名函数、高阶函数BIF的详细介绍。
  * 第13张图
    *   这张图的重点是模块的标准区域、名称空间以及模块的作用域（三种变量的运用）。
  * 第14张图
    *   最后一张图整理了面向对象编程，弄清楚面向对象的基本概念，继承与多态、结构组织以及对象的性质、访问限制等重点，对于python就算是入门了。
* [Python语法有多简单？一张图就能学会！](https://mp.weixin.qq.com/s/Nqiz6uInH7hHZoERuWWkfQ)
  * https://github.com/coodict/python3-in-one-pic
* [Python 语法速览与实战清单](https://segmentfault.com/a/1190000012129654)
* [Python 教程：从零到大师](https://learnku.com/python/t/22976/python-tutorials-from-zero-to-master-suitable-for-experienced-developers)
  * https://www.freecodecamp.org/news/learning-python-from-zero-to-hero-120ea540b567/
* [Python三十年技术演变史](https://mp.weixin.qq.com/s/xFWpAXWJ4m78bZHYcc3VzQ)
* [全面的 Python 重点](https://mp.weixin.qq.com/s/TFPI0hdlbcHVVO0id6tT4A)
  * https://segmentfault.com/a/1190000018737045
* [【Python入门只需20分钟】从安装到数据抓取、存储原来这么简单 - 旺旺笔记 - 博客园](https://www.cnblogs.com/zhaww/p/9517514.html)

## BASIC

* [Python 关键字知识点大放送](https://mp.weixin.qq.com/s/l8cxp-SPO6NCRmrSvseyAw)
  * ![image](https://user-images.githubusercontent.com/34557994/132124927-684e0dc0-a4a1-4aee-9efc-10b8a560fb65.png)
  * 7、try、except、finally、raise
    * try、except、finally、raise都是与异常有关的关键词，用法如下：
      * try：在try...except块中使用，它定义了一个代码块，并在没有问题的情况下执行块。如果包含任何错误，可以为不同的错误类型定义不同的块。
      * except：在try... except块中使用。如果try块引发错误，并在有问题的情况下执行对应的代码块。
      * [8. Errors and Exceptions — Python 3.9.7 documentation](https://docs.python.org/3/tutorial/errors.html)
        * The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception.
        * You can use the else keyword to define a block of code to be executed if no errors were raised
      * finally：在try...except块中使用。它定义了一个代码块，当try...except...else块结束时，该代码块将运行。无论try块是否引发错误，都将执行finally代码块。
      * raise：raise关键字用于引发异常，可以定义引发哪种错误，以及向用户显示错误信息。
    ```python
    def func(x):
        try:
            100 // x
        except:
            print("ZeroDivisionError: division by zero(除数不能是0)")
        else:
            print(f"结果是：{str(100 // x)}")
        finally:
            print("无论如何，都会执行！")

    func(10)  # 结果是：10 
    func(0)   # 无论如何，都会执行！
    ```
  * 11、lambda
    * lambda关键字用于创建一个 “匿名函数”。
    ```python
    x = lambda a: a + 8
    x(2)  # 10
    ```
  * 13、global、nonlocal
    * global关键字用于创建一个全局变量。nonlocal关键字用于声明一个非局部变量，用于标识外部作用域的变量。
    ```python
    # 定义一个函数:
    def func():
        global x
        x = "函数中的变量"

    # 执行函数:
    func()

    # x定义在函数中，按说这里打印x会报错，我们看看
    print(x)  # 函数中的变量
    ```
  * 14、in、is
    * is：用于判断两个变量是否是同一个对象，如果两个对象是同一对象，则返回True，否则返回False。要与== 区别开来，使用==运算符判断两个变量是否相等。
    ```python
    x = 2.0
    y = 2.0
    x is y  # False
    x == y  # True
    ```
  * 15、None
    * None关键字用于定义一个空值（根本没有值），与0，False或空字符串不同。None是其自身的数据类型（NoneType），只能为None。
  * 16、assert
    * 调试代码时，使用assert关键字。主要用于测试代码中的条件是否为True，如果为False，将引发AssertionError。
    ```python
    x = 666

    assert x == 666
    assert x == 888,"x应该等于666，你的输入有误！"  # AssertionError: x应该等于666，你的输入有误！
    ```
  * 17、with
    * with常和open使用，用于读取或写入文件。
    ```python
    with open("哈哈.txt","r") as f:
        print(f.read())
    ```
  * 18、yield
    * yield关键字结束一个函数，返回一个生成器，用于从函数依次返回值。
    ```python
    def f():
        yield 5

    print(f())  # <generator object f at 0x7facfc885f50>
    print(next(f()))    # 5
    ```
* [Python 为什么不支持 i++ 自增语法，不提供 ++ 操作符？ (qq.com)](https://mp.weixin.qq.com/s/gs3aZucOxXkeMGmP0H9fuA)
* [6.12. Assignment expressions - 6. Expressions — Python 3.9.7 documentation](https://docs.python.org/3/reference/expressions.html?highlight=walrus#assignment-expressions)
  * assignment_expression ::=  [identifier ":="] expression
  * An assignment expression (sometimes also called a “named expression” or “walrus”) assigns an expression to an identifier, while also returning the value of the expression.
  * One common use case is when handling matched regular expressions:
  ```python
  if matching := pattern.search(data):
      do_something(matching)
  ```
  * Or, when processing a file stream in chunks:
  ```python
  while chunk := file.read(9000):
      process(chunk)
  ```   
* [条件语句的七种写法](https://mp.weixin.qq.com/s?__biz=Mzg4NDQwNTI0OQ==&mid=2247522923&idx=4&sn=04c0072a03765c7741f459cd0807d9b7&source=41#wechat_redirect)

### Iterator / Generator

* [盘一盘 Python 系列特别篇 - 两大利「器」](https://mp.weixin.qq.com/s/o9REZiT-k-6UTcSnqCfCMQ)
  * 主要介绍 Python 里的两大利「器」，生成器 (generator) 和迭代器 (iterator)。
  * 生成器
    * 定义生成器 (generator) 有两种方法：
      * 使用函数 (function) 
      * 使用表达式 (expression)
    * 如何来看生成器里的元素呢？有两种方法：1. 转换成 list；2. 用 next()。
    * 总结：生成器可以用生成函数 (generator function) 来定义，记住要用 yield 而不是 return。
    * 总结：生成器可以用生成表达式 (generator expression) 来定义，记住和列表解析式很像，将 [] 改成 () 即可。
    * 生成器 vs 列表
      * 生成器好在哪里？好就好在生成器是按需求调用 (call-by-need) 的，你需要调用一个值，我就 yield 一个值，然后用 next() 更新内部状态，等待你下次调用。这套流程也称作惰性求值 (lazy evaluation)，目的是最小化计算机要做的工作。
      * 在大规模数据时，一次性处理往往抵消而且不方便，而惰性求值解决了这个问题，它把计算的具体步骤延迟到了要实际用该数据的时候。
      * 对比一下生成器和列表在运行简单操作时的用的时间和占的内存。
      ```python
      import timeit
      import sys

      print(timeit.timeit('l = [x+1 for x in range(10000000)]', number=1))    # 0.88682526

      l = [x+1 for x in range(10000000)]
      print(sys.getsizeof(l))     # 81528064

      print(timeit.timeit('g = (x+1 for x in range(10000000))', number=1))    # 1.501199999998093e-05

      g = (x+1 for x in range(10000000))
      print(sys.getsizeof(g))     # 128
      ```
  * 迭代器
    * 可迭代对象(Iterable)
      * 任何只要可以循环的东西就可称之可迭代对象 (iterable)。容器类型数据 (str, tuple, list, dict, set) 都可以被 for 循环，因此它们都是可迭代对象。
      * 在 Python 里万物皆对象，如果真要判断一个对象是否是可迭代对象，我们可以用 isinstance(x, Iterable)。
      * 在 Python 里万物皆对象，那么我们可以查看该对象对应的类里面的属性，用 dir() 函数。里面有 __iter__() 魔法方法 (magic method) 的对象就是可迭代对象。
    * 迭代器
      * 可被 for 循环的列表、字典、元组、集合和字符串都是可迭代对象，但实际上 for 循环里真正的对象是迭代器。
      * 首先用 isinstance(x, Iterator) 来判断，结果它们 5 个都不是迭代器。
      * 那它们怎么能被 for 循环呢？原来 for 循环先用 __iter__() 方法将它们都转成迭代器，再开始遍历它们的每个元素。
      * 被 __iter__() 方法包装之后，列表、字典、元组、集合和字符串都是迭代器了。注意 iter(x) 和 x.__iter__() 是等价的，后者太难看因此习惯用前者。
      * 既然能被迭代，那该对象里面肯定有 __next__() 魔法方法，要不然怎么可以一个元素一个元素往下走下去
      * 除了 __next__，迭代器里还有 __iter__，而 __iter__ 是判断可迭代对象的标准。因此可得只要是迭代器就是可迭代对象，但反过来不成立。
      * 有了 StopIteration  这个提示，我们甚至可以自己写代码来实现用 for 循环来打印。
      ```python
      i_nums = iter(nums)

      while True:
          try:
              print(next(i_nums))
          except StopIteration:
              break
      ```
    * 自定义迭代器
      * 上节讲了用 iter() 函数可以将可迭代对象转换成迭代器，本节再介绍两种定义迭代器的方法：1. 用类；2. 生成器。
      * 用类来定义
      ```python
      class MyRange:
          def __init__(self, start, end):
              self.value = start
              self.end = end

          def __iter__(self):
              return self

          def __next__(self):
              if self.value >= self.end:
                  raise StopIteration
              current = self.value
              self.value += 1
              return current


      if __name__ == '__main__':
          nums = MyRange(1, 5)

          # 可以被 for 循环
          # 1
          # 2
          # 3
          # 4
          for num in nums:
              print(num)

          nums = MyRange(1, 5)

          # 也可以使用 next() 函数
          print(next(nums))   # 1
          print(next(nums))   # 2
          print(next(nums))   # 3
          print(next(nums))   # 4
          print(next(nums))   # Traceback (most recent call last): ... StopIteration
      ```
      * 用生成器来定义
      ```python
      def range_generator(start, end):
          current = start
          while current < end:
              yield current
              current += 1


      if __name__ == '__main__':
          nums = range_generator(1, 5)

          # 可以被 for 循环
          # 1
          # 2
          # 3
          # 4
          for num in nums:
              print(num)

          nums = range_generator(1, 5)

          # 也可以使用 next() 函数
          print(next(nums))   # 1
          print(next(nums))   # 2
          print(next(nums))   # 3
          print(next(nums))   # 4
          print(next(nums))   # Traceback (most recent call last): ... StopIteration
      ```
    * 内置迭代器
      * 在 Python 里有不少内置的迭代器，用起来非常方便，我们会介绍 count, cycle, repeat, combinations, permudations, product 和 chain。
      * 首先引用 itertools，顾名思义就知道它里面有很多迭代器的工具。
      * count
        * count() 就像是计数器，不停的往前更新。它可用在给不知道大小的数据标注索引。
      * cycle
        * cycle() 作用是循环遍历！
      * repeat
        * repeat() 作用是重复，但是一旦设置 times 参数比如 3，那么不能打印次数不能超过 3，否则会报错。
        * repeat() 还可以和其他高阶函数一起用，如下列 map 函数。
      * combinations & permutations
        * 从 letters 里面 4 个元素取出 2 个来组合 (元素位置不重要)。
        * 从 letters 里面 4 个元素取出 2 个来排列 (元素位置重要)。
      * product
        * product() 是穷举出所有情况，本例只从 numbers 里面 4 个元素取出 2 个，不同位置元素可以重复。
        * 上面结果去除一些「位置不同但元素相同」，比如 (1, 2) 和 (2, 1) 只保留一个，就是 combinations_with_replacement() 的结果
        * 上面结果再去除「重复元素」，比如 (1, 1), (2, 2), ... ，就是 combinations() 的结果
      * chain
        * 用于三个不同类型的数据格式，列表 letters，元组 numbers 和集合 names，我们可用 chain() 将它们串起来成一个迭代器，再逐个遍历它里面的元素。
  * 总结
    * 字典用来创建映射关系
    * 函数用来创建可调用对象
    * 生成器用来创建迭代器
    * 当你想要个可用惰性计算的可迭代对象时，考虑用迭代器。
    * 当你想创建迭代器时，考虑用生成器。
    * 当你想创建生成器时，考虑用生成函数 (用 yield) 或生成表达式 (用小括号 ())。    
* [Python 迭代器与生成器](http://www.langzi.fun/%E8%BF%AD%E4%BB%A3%E5%99%A8%E4%B8%8E%E7%94%9F%E6%88%90%E5%99%A8.html)
* [Python 迭代器和 C++ 迭代器最大的不同](https://mp.weixin.qq.com/s/2qoNY-UNLf8vW7CGj8BQ2A)
* [带你彻底搞懂Python生成器](https://mp.weixin.qq.com/s/2HAPquA-VZNNRHYRN8E2bg)
```python
def incrementor(n: int):
    count = 0

    while count < n:
        yield count
        count += 1


if __name__ == '__main__':
    print(list(incrementor(3)))  # [0, 1, 2]

    my_incrementor = incrementor(3)

    print(my_incrementor)   # <generator object incrementor at 0x7fe9fd886350>
    print(next(my_incrementor))  # 0
    print(next(my_incrementor))  # 1
    print(next(my_incrementor))  # 2
    print(next(my_incrementor))  # Traceback (most recent call last): ... StopIteration
```

### [Built-in Functions](https://docs.python.org/3/library/functions.html)

* [图解 Python 函数](https://mp.weixin.qq.com/s/9AxWUaYaK15N4hsQMjlBjA)
* Python 69个内置函数分8类总结
  * [Built-in Functions — Python 3.9.7 documentation](https://docs.python.org/3/library/functions.html)
  * 1、内置函数
  * 2、类型相关
  * 3、数理统计相关
  * 4、进制转换
  * 5、面向对象相关
  * 6、迭代器相关
  * 7、map函数
  * 8、排序相关
  * 9 其他
* [open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)](https://docs.python.org/3/library/functions.html#open)
	* Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.
* [ord(c) - Built-in Functions — Python 3.9.7 documentation](https://docs.python.org/3/library/functions.html#ord)
  * Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of [chr()](https://docs.python.org/3/library/functions.html#chr).
* [reversed(seq)](https://docs.python.org/3/library/functions.html?highlight=reversed#reversed)
	* Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
* [len(x) 击败 x.len()，从内置函数看 Python 的设计思想 (qq.com)](https://mp.weixin.qq.com/s/IRMplJCoWtH98uNtAeFKxg)
* [Python高阶函数使用总结](https://mp.weixin.qq.com/s/xtO8NDq3lVacsT5Z7eQXmw)
  * 本文结合各种实际的例子详细讲解了Python5个内建高阶函数的使用，能够帮助理解Python的数据结构和提高数据处理的效率，这5个函数分别是：
    * map
    * reduce
    * filter
    * sorted/sort
    * zip
* [class complex([real[, imag]])](https://docs.python.org/3/library/functions.html?highlight=complex#complex)
	* Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

### [Functions](https://www.tutorialspoint.com/python/python_functions.htm)

* [*args and **kwargs in Python - GeeksforGeeks](https://www.geeksforgeeks.org/args-kwargs-python/)
	* In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
	* Special Symbols Used for passing arguments:
	* 1.)*args (Non-Keyword Arguments)
	* 2.)**kwargs (Keyword Arguments)
* [Python中的*args和**kwargs是什么？该如何使用？](https://mp.weixin.qq.com/s/s7PFVE_wcAMZaRUds2MJDQ) 
  * https://medium.com/better-programming/what-are-args-and-kwargs-in-python-6aaf9e3cad73
* [为什么 Python 没有 main 函数？](https://mp.weixin.qq.com/s/Nr1nD6qKKRd-C55PCV-sGw)
  * https://towardsdatascience.com/why-doesnt-python-have-a-main-function-3afe6a8d093
* [Python | 掌握 Lambda 函数，四不要](https://mp.weixin.qq.com/s/tWibBZGcX4PtEKo0a1bvzQ)
  * https://github.com/xitu/gold-miner/blob/master/article/2020/master-python-lambda-functions-with-these-4-donts.md
    1. 不要返回任何值
    2. 不要忘记更好的选择
    3. 不要将它赋值给变量
    4. 不要忘记列表推导式

### [Built-in Constants](https://docs.python.org/3/library/constants.html)

### [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

#### [typing — Support for type hints](https://docs.python.org/3/library/typing.html)

* Note The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
* This module provides runtime support for type hints. The most fundamental support consists of the types Any, Union, Callable, TypeVar, and Generic. For a full specification, please see PEP 484. For a simplified introduction to type hints, see PEP 483.
* The function below takes and returns a string and is annotated as follows:
```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```
* In the function greeting, the argument name is expected to be of type str and the return type str. Subtypes are accepted as arguments.
* [typing.Any](https://docs.python.org/3/library/typing.html#typing.Any)
	* Special type indicating an unconstrained type.
		* Every type is compatible with Any.
		* Any is compatible with every type.
* [class typing.List(list, MutableSequence[T])](https://docs.python.org/3/library/typing.html#typing.List)
	* Generic version of list. Useful for annotating return types. To annotate arguments it is preferred to use an abstract collection type such as Sequence or Iterable.

#### [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

* [干货|理解Python列表和元组](https://mp.weixin.qq.com/s/U-ctO-brjwxpm0LbLTB-dw)
* [list.remove(x) - 5. Data Structures — Python 3.9.7 documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  * Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
  * [Python list remove() - GeeksforGeeks](https://www.geeksforgeeks.org/python-list-remove/)
```python
a = [1, 2, 2, 3, 4]
b = [1, 2, 2, 3, 4]


def even(x):
    return x % 2 == 0


for item in a:
    if even(item):
        # just remove the first occurrence
        a.remove(item)

print(a)    # [1, 2, 3]


for item in b:
    if even(item):
        # remove all occurrence in list
        while item in b:
            b.remove(item)

print(b)    # [1, 3]
```
* [Python 列表排序 sort 与 sorted 详解](https://mp.weixin.qq.com/s/R16hyfikRCOEUGhDGOBVcQ)
  * https://maida6244.xyz/

#### [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

* [str.count(sub[, start[, end]])](https://docs.python.org/3/library/stdtypes.html#str.count)
	* Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
* [str.format(*args, **kwargs)](https://docs.python.org/3/library/stdtypes.html#str.format)
	* Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
* [盘一盘 Python 系列特别篇 - 格式化 String](https://mp.weixin.qq.com/s/jTiZOazn66nK6CU1SAtpTw)
* 如何多行字符串拼接?
```python
# -*- coding: utf-8 -*-
"""
@author: Hao
"""

start_timestamp = "2018-01-01 00:00:00"
end_timestamp = "2018-01-02 00:00:00"

# =============================================================================
# SELECT "timestamp", col1
# FROM tbl
# WHERE "timestamp" >= '2018-01-01 00:00:00' AND "timestamp" <= '2018-01-02 00:00:00'
# ORDER BY "timestamp" ASC
# =============================================================================
query = """
    SELECT "timestamp", col1
    FROM tbl
    WHERE "timestamp" >= '"""             \
    + start_timestamp +                 \
    """' AND "timestamp" <= '"""        \
    + end_timestamp +                   \
    """'
    ORDER BY "timestamp" ASC
    """

print(query)

# =============================================================================
# SELECT "timestamp", col1
# FROM tbl
# WHERE "timestamp" >= '2018-01-01 00:00:00' AND "timestamp" <= '2018-01-02 00:00:00'
# ORDER BY "timestamp" ASC
# =============================================================================
query = ("""
    SELECT "timestamp", col1
    FROM tbl
    WHERE "timestamp" >= '"""
    + start_timestamp +
    """' AND "timestamp" <= '"""
    + end_timestamp +
    """'
    ORDER BY "timestamp" ASC
    """)

print(query)
```
* Python 字符串拼接总结
  * https://segmentfault.com/a/1190000015475309
  * [2.4.3. Formatted string literals - 2. Lexical analysis — Python 3.9.6 documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    * A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
    * See also [PEP 498](https://www.python.org/dev/peps/pep-0498/) for the proposal that added formatted string literals, and [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format), which uses a related format string mechanism.
  * [Efficient String Concatenation in Python](https://waymoot.org/home/python_string/)
  * 注意Python中list是可变对象，而str是不可变对象。fun1比fun2更高效。
```python
def fun1(s: str) -> str:
    results = []
    for i in range(len(s)):
        results.append(s[i])  # 仅需在列表尾部添加元素
    return ''.join(results)  # 申请一次内存

def fun2(s: str) -> str:
    results = ''
    for i in range(len(s)):
        results += s[i]  # 每次拼接都要新建一个字符串，申请N次内存
    return results
```
* [10 个 Python 字符串处理技巧](https://mp.weixin.qq.com/s/iaT30IyPT8NSQ42d3oVpVA)
  * [Text Sequence Type — str - Built-in Types — Python 3.9.7 documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
    * [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
  * [string — Common string operations — Python 3.9.7 documentation](https://docs.python.org/3/library/string.html)
  1. 空格剥离
  ```python
  s = '    This is a sentence with whitespace.   '

  print('Strip leading whitespace: "{}"'.format(s.lstrip()))   # Strip leading whitespace: "This is a sentence with whitespace.   "
  print('Strip trailing whitespace: "{}"'.format(s.rstrip()))  # Strip trailing whitespace: "    This is a sentence with whitespace."
  print('Strip all whitespace: "{}"'.format(s.strip()))        # Strip all whitespace: "This is a sentence with whitespace."

  s = 'This is a sentence with unwanted characters.AAAAAAAA'
  print('Strip unwanted characters: "{}"'.format(s.rstrip('A')))  # Strip unwanted characters: "This is a sentence with unwanted characters."
  ```
  2. 字符串拆分
  ```python
  s = ' KDnuggets is a fantastic resource '
  print(s.split())    # ['KDnuggets', 'is', 'a', 'fantastic', 'resource']

  s = 'these,words,are,separated,by,comma'
  print('"," separated split -> {}'.format(s.split(',')))     # "," separated split -> ['these', 'words', 'are', 'separated', 'by', 'comma']

  s = 'abacbdebfgbhhgbabddba'
  print('"b" separated split -> {}'.format(s.split('b')))     # "b" separated split -> ['a', 'ac', 'de', 'fg', 'hhg', 'a', 'dd', 'a']
  ```
  3. 将列表元素合成字符串
  ```python
  s = ['KDnuggets', 'is', 'a', 'fantastic', 'resource']
  print('"{}"'.format(' '.join(s)))   # "KDnuggets is a fantastic resource"

  s = ['Eleven', 'Mike', 'Dustin', 'Lucas', 'Will']
  print('"{}"'.format(' and '.join(s)))   # "Eleven and Mike and Dustin and Lucas and Will"
  ```
  4. 字符串反转
  ```python
  s = 'abcde'

  print(s[::-1])  # edcba
  print(reversed(s))  # <reversed object at 0x7f869db73c50>
  print(''.join(reversed(s)))     # edcba
  ```
  5. 大小写转换
  ```python
  s = 'KDnuggets'

  print('KDnuggets as uppercase: {}'.format(s.upper()))   # KDnuggets as uppercase: KDNUGGETS
  print('KDnuggets as lowercase: {}'.format(s.lower()))   # KDnuggets as lowercase: kdnuggets
  print('KDnuggets as swapped case: {}'.format(s.swapcase()))     # KDnuggets as swapped case: kdNUGGETS
  ```
  6. 检查是否有字符串成员
  ```python
  s1 = 'perpendicular'
  s2 = 'pen'
  s3 = 'pep'

  print('pen in perpendicular -> {}'.format(s2 in s1))    # pen in perpendicular -> True
  print('pep in perpendicular -> {}'.format(s3 in s1))    # pep in perpendicular -> False

  s = 'Does this string contain a substring?'

  print('string location -> {}'.format(s.find('string')))     # string location -> 10
  print('spring location -> {}'.format(s.find('spring')))     # spring location -> -1
  ```
  7. 子字符串替换
  * str.replace(old, new[, count])
    * Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
  ```python
  s1 = 'old things old things old things'
  s2 = 'new'

  print(s1.replace('old', s2))        # new things new things new things
  print(s1.replace('old', s2, 2))     # new things new things old things
  ```
  8. 组合多个列表的输出
  ```python
  countries = ['USA', 'Canada', 'UK', 'Australia']
  cities = ['Washington', 'Ottawa', 'London', 'Canberra']

  # The capital of USA is Washington.
  # The capital of Canada is Ottawa.
  # The capital of UK is London.
  # The capital of Australia is Canberra.
  for x, y in zip(countries, cities):
      print('The capital of {} is {}.'.format(x, y))
  ```
  9. 同字母异序词检查
  ```python
  from collections import Counter


  def is_anagram(s1, s2):
      return Counter(s1) == Counter(s2)


  s1 = 'listen'
  s2 = 'silent'
  s3 = 'runner'
  s4 = 'neuron'

  print('listen is an anagram of silent -> {}'.format(is_anagram(s1, s2)))    # listen is an anagram of silent -> True
  print('runner is an anagram of neuron -> {}'.format(is_anagram(s3, s4)))    # runner is an anagram of neuron -> False
  ```
  10. 回文检查
  ```python
  def is_palindrome(s):
      reverse = s[::-1]
      if (s == reverse):
          return True
      return False


  s1 = 'racecar'
  s2 = 'hippopotamus'

  print('racecar is a palindrome -> {}'.format(is_palindrome(s1)))    # racecar is a palindrome -> True
  print('hippopotamus is a palindrome -> {}'.format(is_palindrome(s2)))   # hippopotamus is a palindrome -> False
  ```

#### [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

* A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built-in dict, list, and tuple classes, and the collections module.)
* Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
* There are currently two built-in set types, set and frozenset. The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.
* Non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: {'jack', 'sjoerd'}, in addition to the set constructor.

#### [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

* A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. (For other containers see the built-in list, set, and tuple classes, and the collections module.)
* A dictionary’s keys are almost arbitrary values. Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)
* Dictionaries can be created by placing a comma-separated list of key: value pairs within braces, for example: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}, or by the dict constructor.
* [如何优雅的操作Python字典](https://mp.weixin.qq.com/s/mWjzDm9XNNnFiJGYhzpivA)
  * https://www.linuxzen.com/python-you-ya-de-cao-zuo-zi-dian.html
```python
"""
Implement a class to be used a key in dictionary
"""


class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __hash__(self) -> int:
        return hash((self.first_name, self.last_name))

    def __eq__(self, o: object) -> bool:
        return self.first_name == o.first_name and self.last_name == o.last_name


if __name__ == '__main__':
    person = Person('David', 'B')
    my_dict = {person: '123'}

    print("{} : {}".format(person, my_dict[person]))    # <__main__.Person object at 0x7f8cd0473ed0> : 123
```

### [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

### [Exceptions Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

* [学习笔记之Python Debug ( pdb ) - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/10437091.html)
* [盘一盘 Python 系列特别篇 - 错误类型](https://mp.weixin.qq.com/s/PBaDdLcYxDso2V4aZcFXpA)
* [盘一盘 Python 系列特别篇 - 异常处理](https://mp.weixin.qq.com/s/94O3Kz__8UQZoZtQ-WyOcQ)
* [一文教你读懂 Python 中的异常信息](https://realpython.com/python-traceback/)
* [Python 常见的17个错误分析](https://www.oschina.net/question/89964_62779)
  * https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/

### [Modules](https://www.tutorialspoint.com/python/python_modules.htm)

* [深入探讨Python的import机制：实现远程导入模块 | CSDN博文精选](https://mp.weixin.qq.com/s/Sx_WyKUpoZrnFtV9epAfpg)
* 你常常看到的 \_\_init\_\_.py 到底是个啥？
  * 综上，\_\_init\_\_.py 会在 import 的时候被执行，而空的 \_\_init\_\_.py 在 Python 新版本中已经不需要你额外去定义了，因为就算你不定义 init， Python 也知道你导入的包路径，但是如果你想要做一些初始化操作，或者像我们刚刚说的预先导入相关的模块，那么定义 \_\_init\_\_.py 还是很有必要的哟。
* [Python编程中的if \_\_name\_\_ == 'main' 的作用和原理](https://mp.weixin.qq.com/s/SXTo0h2ExujAQdWnLWggdg)
  * https://zhuanlan.zhihu.com/p/34112508
  * \_\_name\_\_ 是当前模块名，当模块被直接运行时模块名为 \_\_main\_\_ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
* [Python Logging 模块完全解读](https://mp.weixin.qq.com/s/iZEjyEoxVUQ5cner2VY1kg)

#### [Text Processing Services](https://docs.python.org/3/library/text.html)

##### [string — Common string operations](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#module-string)

* [String constants](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#string-constants)
	* [string.ascii_lowercase](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#string.ascii_lowercase)
		* The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
* [Custom String Formatting](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#custom-string-formatting)
* [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
* [Helper functions](https://docs.python.org/3/library/string.html?#helper-functions)
	* [string.capwords(s, sep=None)](https://docs.python.org/3/library/string.html?#string.capwords)
		* Split the argument into words using str.split(), capitalize each word using str.capitalize(), and join the capitalized words using str.join(). If the optional second argument sep is absent or None, runs of whitespace characters are replaced by a single space and leading and trailing whitespace are removed, otherwise sep is used to split and join the words.

#### [Data Types](https://docs.python.org/3/library/datatypes.html)

##### [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

* [Python - Date & Time](https://www.tutorialspoint.com/python/python_date_time.htm)
* Get date of the datetime instance
	* 8.1. datetime — Basic date and time types — Python 3.6.6rc1 documentation
		* https://docs.python.org/3/library/datetime.html#datetime.date
* timedelta Objects - datetime — Basic date and time types — Python 3.7.2 documentation
	* https://docs.python.org/3/library/datetime.html#timedelta-objects
	* class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
* [Python datetime to string without microsecond component - Stack Overflow](https://stackoverflow.com/questions/7999935/python-datetime-to-string-without-microsecond-component)
	* $ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	* 8.1. datetime — Basic date and time types — Python 3.3.7 documentation
		* https://docs.python.org/3.3/library/datetime.html#datetime.datetime.strftime
* How to increment the day in datetime? Python - Stack Overflow
	* https://stackoverflow.com/questions/3240458/how-to-increment-the-day-in-datetime-python
	* date += datetime.timedelta(days=1)
* datetime — Basic date and time types — Python 3.8.6rc1 documentation
	* https://docs.python.org/3.8/library/datetime.html#datetime.datetime.utcfromtimestamp
	* classmethod datetime.utcfromtimestamp(timestamp)
	* Return the UTC datetime corresponding to the POSIX timestamp, with tzinfo None. (The resulting object is naive.)
* Examples of Usage: datetime
	* [datetime — Basic date and time types — Python 3.8.8 documentation](https://docs.python.org/3.8/library/datetime.html#examples-of-usage-datetime)
	* [datetime — Basic date and time types — Python 3.8.8 documentation](https://docs.python.org/3.8/library/datetime.html#strftime-strptime-behavior)
		* strftime() and strptime() Behavior
	* [datetime — Basic date and time types — Python 3.8.8 documentation](https://docs.python.org/3.8/library/datetime.html#datetime.datetime.strptime)
		* classmethod datetime.strptime(date_string, format)
		* Return a datetime corresponding to date_string, parsed according to format.
	* [datetime — Basic date and time types — Python 3.8.8 documentation](https://docs.python.org/3.8/library/datetime.html#datetime.datetime.strftime)
		* datetime.strftime(format)
		* Return a string representing the date and time, controlled by an explicit format string.

##### [collections — Container datatypes](https://docs.python.org/3/library/collections.html)

* [四种高性能数据类型，Python collections助你优化代码、简洁任务](https://mp.weixin.qq.com/s/17xwTlwJi1ckht3wGk5ttA)
  * https://levelup.gitconnected.com/introducing-high-performance-datatypes-in-python-with-the-collections-library-3d8c334827a5
* [原来 collections 这么好用](https://mp.weixin.qq.com/s/BJ9FoirMv8RHr3ieZB0mDA)
  * [Python-collections模块](https://blog.csdn.net/mall_lucy/article/details/108822795)
  * collections模块：实现了特定目标的容器，以提供Python标准内建容器 dict、list、set、tuple 的替代选择。
  * Counter：字典的子类，提供了可哈希对象的计数功能。
    * [class collections.Counter([iterable-or-mapping])](https://docs.python.org/3/library/collections.html#collections.Counter)
      * A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
      * Elements are counted from an iterable or initialized from another mapping (or counter) 
      * most_common([n])
        * Return a list of the n most common elements and their counts from the most common to the least. If n is omitted or None, most_common() returns all elements in the counter. Elements with equal counts are ordered in the order first encountered
			```python
			Counter('abracadabra').most_common(3) # [('a', 5), ('b', 2), ('r', 2)]
			```
  * defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值。
  * OrderedDict：字典的子类，保留了他们被添加的顺序。
  * namedtuple：创建命名元组子类的工厂函数。
  * deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)。
  * ChainMap：类似字典的容器类，将多个映射集合到一个视图里面。
* [盘一盘 Python 系列特别篇 - Collection](https://mp.weixin.qq.com/s/C_bSgxE_1wIPhcqIF7w74w)
  * 我们在【盘一盘 Python 下】一贴介绍过 5 种类型的容器型（container）数据，分别是字符串（string）、列表（list）、元组（tuple）、字典（dictionary）和集合（set）。
  * 今天我们来介绍除上面 5 个之外的容器型数据，统称 Collection，见下图。
  * ![image](https://user-images.githubusercontent.com/34557994/132177945-18502039-6b02-4fec-8ed6-ab369c524663.png)
  * 上图中的 UserDict, UserList 和 UserString 只是字典、列表和字符串的一个简单封装，而 frozenset 就是“元素不可修改”的集合，它们平时使用的频率很少，因此略过不讲。
  * 本帖只介绍 6 种使用较多（和上面 4 种较少的相比而言）的 Collection，它们是
    * namedtuple
    * defaultdict
    * Counter
    * deque
    * ChainMap
    * OrderedDict
  * 再具体讲它们之前，我们来思考一个基础问题，为什么要创造它们？字符串列表元组字典集合这“五大金刚”不香吗？创造它们一定是五大金刚有缺陷，先看看它们之间的功能总结。
    * 元组的可读性太差但不可修改，字典的可读性强但可修改，两者一结合便是命名元组 (namedtuple)。
    * 在读写字典时，如果键不存在会报错，那么就有了默认字典 (defaultdict)。
    * 计数器 (Counter) 是个字典的子类，能快速计量元素出现的个数。
    * 列表只能从尾部添加元素，不能从头部，那么就有了双端队列 (deque)。
    * 在多个字典上操作效率不高，那么就有了链式映射 (ChainMap)。
    * 原来普通字典在读取中不能记录放入元素的顺序（现在可以了），那么就有了有序字典 (OrderedDict)。因此我觉得有序字典现在用处不大，但还是讲讲吧。
  * namedtuple
    * 命名元组 (namedtuple) 是元组和字典的混合体，它赋予每个元素含义 (字典的特性)，而且元素不可修改 (元组的特性)。
    * 创建命名元组需要设定两个必需参数：元组名称，字段名称。
    * 像字典一样查看其键 (用 \_fields)，像元组一样查看其值的索引 (用 index) 和计数 (用 count)。
    * 获取元素有三种方法：
      * 像元祖那样用数值索引
      * 像对象那样用点 .
      * 像对象那样用函数 getattr
    * 元组不可修改，命名元组也是，应该直接更新其元素会报错。
    * 但可以用 \_replace 函数更新其值，并生成新的命名元组
    * 用 \_make 函数创建新的命名元组
    * 还可以用字典打散的形式来创建命名元组
  * defaultdict
    * 默认字典 (defaultdict) 和字典不同，我们不需要检查键是否存在，对于不存在的键，会赋一个默认值。
  * Counter
    * 计数器 (Counter) 是字典的子类，提供了可哈希（hashable）对象的计数功能。可哈希就是可修改（mutable），比如列表就是可哈希或可修改。
  * deque
    * 双端队列 (deque) 可让我们从头/尾两端添加或删除元素。
    * 我们知道列表里用 append,extend 和 pop 方法，它们只能从尾部添加或删除元素，那么在双端队列里有 appendleft, extendleft 和 popleft 方法，从左边，即尾部，添加或删除元素。
    * 使用 append 和 appendleft，把参数来整块添加。
    * 使用 extend 和 extendleft ，把参数来打散添加，列表 ['Go', 0] 打散成两个元素添加上去，如果是 append 那么就把这个列表当成整体添加上去。
    * 使用 pop 和 popleft 来删除元素。
  * ChainMap
    * 链式映射 (ChainMap) 可看成字典的容器，将多个映射串联起来，这样它们就可以作为一个单元处理。通常比创建一个新字典和多次调用 update 函数要快很多。
    * 首先创建链式映射，先创建三个字典，再把它们打包成 ChainMap。
    * 如果多个字典都有某个键，那么返回第一个含该键的字典的值。
    * 用 get() 函数查看超级玛丽，'Super Mario'，如果每个字典都没此键，不返回值也不报错。
  * OrderedDict
    * 有序字典 (OrderedDict) 是字典的子类，就像常规字典一样，它会记录放入元素的顺序，但现在常规字典也有这种功能了，因此有序字典的存在意义也不大了。
    * 在有序词典中，有一个 reversed() 函数，可以逆序返回字典的键。

##### [heapq — Heap queue algorithm](https://docs.python.org/3/library/heapq.html)

* This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
* Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that its smallest element is always the root, heap[0].
* The API below differs from textbook heap algorithms in two aspects: (a) We use zero-based indexing. This makes the relationship between the index for a node and the indexes for its children slightly less obvious, but is more suitable since Python uses zero-based indexing. (b) Our pop method returns the smallest item, not the largest (called a “min heap” in textbooks; a “max heap” is more common in texts because of its suitability for in-place sorting).
* These two make it possible to view the heap as a regular Python list without surprises: heap[0] is the smallest item, and heap.sort() maintains the heap invariant!
* To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().
  * heapq.heappush(heap, item)
    * Push the value item onto the heap, maintaining the heap invariant.
  * heapq.heappop(heap)
    * Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
  * heapq.heappushpop(heap, item)
    * Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
  * heapq.heapify(x)
    * Transform list x into a heap, in-place, in linear time.

#### [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)

##### [cmath — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)

* [cmath.polar(x)](https://docs.python.org/3/library/cmath.html#cmath.polar)
	* Return the representation of x in polar coordinates. Returns a pair (r, phi) where r is the modulus of x and phi is the phase of x. polar(x) is equivalent to (abs(x), phase(x)).

#### [Functional Programming Modules](https://docs.python.org/3/library/functional.html)

##### [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)

* This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
  * [itertools.permutations(iterable, r=None)](https://docs.python.org/3/library/itertools.html#itertools.permutations)
    * Return successive r length permutations of elements in the iterable.
    * [Permutation and Combination in Python - GeeksforGeeks](https://www.geeksforgeeks.org/permutation-and-combination-in-python/)
* Infinite iterators:
  
| Iterator | Arguments | Results | Example |
| - | - | - | - |
| count() | start, [step] | start, start+step, start+2*step, … | count(10) --> 10 11 12 13 14 ... |
| cycle() | p | p0, p1, … plast, p0, p1, … | cycle('ABCD') --> A B C D A B C D ... | 
| repeat() | elem [,n] | elem, elem, elem, … endlessly or up to n times | repeat(10, 3) --> 10 10 10 | 

* Iterators terminating on the shortest input sequence:

| Iterator | Arguments | Results | Example | 
| - | - | - | - |
| accumulate() | p [,func] | p0, p0+p1, p0+p1+p2, … | accumulate([1,2,3,4,5]) --> 1 3 6 10 15 | 
| chain() | p, q, … | p0, p1, … plast, q0, q1, … | chain('ABC', 'DEF') --> A B C D E F | 
| chain.from_iterable() | iterable | p0, p1, … plast, q0, q1, … | chain.from_iterable(['ABC', 'DEF']) --> A B C D E F | 
| compress() | data, selectors | (d[0] if s[0]), (d[1] if s[1]), … | compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
| dropwhile() | pred, seq | seq[n], seq[n+1], starting when pred fails | dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
| filterfalse() | pred, seq | elements of seq where pred(elem) is false | filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
| groupby() | iterable[, key] | sub-iterators grouped by value of key(v)
| islice() | seq, [start,] stop [, step] | elements from seq[start:stop:step] | islice('ABCDEFG', 2, None) --> C D E F G
| starmap() | func, seq | func(*seq[0]), func(*seq[1]), … | starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
| takewhile() | pred, seq | seq[0], seq[1], until pred fails | takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
| tee() | it, n | it1, it2, … itn splits one iterator into n
| zip_longest() | p, q, … | (p[0], q[0]), (p[1], q[1]), … | zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

* Combinatoric iterators:

| Iterator | Arguments | Results | Examples | Results |
| - | - | - | - | - |
| product() | p, q, … [repeat=1] | cartesian product, equivalent to a nested for-loop | product('ABCD', repeat=2) | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
| permutations() | p[, r] | r-length tuples, all possible orderings, no repeated elements | permutations('ABCD', 2) | AB AC AD BA BC BD CA CB CD DA DB DC
| combinations() | p, r | r-length tuples, in sorted order, no repeated elements | combinations('ABCD', 2) | AB AC AD BC BD CD
| combinations_with_replacement() | p, r | r-length tuples, in sorted order, with repeated elements| combinations_with_replacement('ABCD', 2) | AA AB AC AD BB BC BD CC CD DD

### [Files I/O](https://www.tutorialspoint.com/python/python_files_io.htm)

* How to input and output file ?
  * 7. Input and Output — Python 3.7.4 documentation
    * https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
    * https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json
    * For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code
  * Python3 File 方法 | 菜鸟教程
    * http://www.runoob.com/python3/python3-file-methods.html
  * python - How to read a file line-by-line into a list? - Stack Overflow
    * https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
  * Python dump dict to json file - Stack Overflow
    * https://stackoverflow.com/questions/17043860/python-dump-dict-to-json-file
  * Python Dictionary to CSV - Stack Overflow
    * https://stackoverflow.com/questions/8331469/python-dictionary-to-csv
  * [Python JSON: Read, Write, Parse JSON (With Examples) (programiz.com)](https://www.programiz.com/python-programming/json)
  * [Python File I/O: Read and Write Files in Python (programiz.com)](https://www.programiz.com/python-programming/file-operation)
  * [json — JSON encoder and decoder — Python 3.9.2 documentation](https://docs.python.org/3/library/json.html?highlight=json#json.load)
    * json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
    * Deserialize fp (a .read()-supporting text file or binary file containing a JSON document) to a Python object using this conversion table.
  * [json — JSON encoder and decoder — Python 3.9.2 documentation](https://docs.python.org/3/library/json.html?highlight=json#json.dump)
    * json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
    * Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.
    * If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
    * If sort_keys is true (default: False), then the output of dictionaries will be sorted by key.
  * How to write datetime object to json file ?
    * [python - How to overcome "datetime.datetime not JSON serializable"? - Stack Overflow](https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844)
      * $ json.dumps(my_dictionary, indent=4, sort_keys=True, default=str) 
    * [How to write a datetime object to JSON in Python (kite.com)](https://www.kite.com/python/answers/how-to-write-a-datetime-object-to-json-in-python#)
      * Call datetime.datetime.isoformat() to convert datetime.datetime into a ISO date format, which is compatible with JSON.
```python
with open( filename, 'r' ) as f:
    for line in f:
        print(line, end='')

import json
with open( filename, 'w' ) as f:
    json.dump(text, f)

with open(filename, 'r') as f:
    x = json.load(f)
```
* How to iterate directory for files ?
  * os — Miscellaneous operating system interfaces — Python 3.7.4 documentation
    * https://docs.python.org/3/library/os.html?highlight=os%20walk#os.walk
    * Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
  * Python3 OS 文件/目录方法 | 菜鸟教程
    * http://www.runoob.com/python3/python3-os-file-methods.html
  * Python list directory, subdirectory, and files - Stack Overflow
    * https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
```python
import os

root = '.'

for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith('.json'):
            filename = os.path.join(path, name)
            print(filename) # '.\path\test.json'
```
* [Text I/O - io — Core tools for working with streams — Python 3.10.2 documentation](https://docs.python.org/3/library/io.html?highlight=textiowrapper#text-i-o)
	* [class io.TextIOBase](https://docs.python.org/3/library/io.html#io.TextIOBase)
		* [read(size=- 1)](https://docs.python.org/3/library/io.html#io.TextIOBase.read)
			* Read and return at most size characters from the stream as a single str. If size is negative or None, reads until EOF.
		* [readline(size=- 1)](https://docs.python.org/3/library/io.html#io.TextIOBase.readline)
			* Read until newline or EOF and return a single str. If the stream is already at EOF, an empty string is returned.
			* If size is specified, at most size characters will be read.
		* [write(s)](https://docs.python.org/3/library/io.html#io.TextIOBase.write)
			* Write the string s to the stream and return the number of characters written.
	* [class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)](https://docs.python.org/3/library/io.html#io.TextIOWrapper)
* [3.3.9. With Statement Context Managers - 3. Data model — Python 3.9.7 documentation](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers)
  * A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement (described in section The with statement), but can also be used by directly invoking their methods.
  * Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.
  * object.__enter__(self)
    * Enter the runtime context related to this object. The with statement will bind this method’s return value to the target(s) specified in the as clause of the statement, if any.
  * object.__exit__(self, exc_type, exc_value, traceback)
    * Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.
    * If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method.
    * Note that __exit__() methods should not reraise the passed-in exception; this is the caller’s responsibility.
  * [8.5. The with statement - 8. Compound statements — Python 3.9.7 documentation](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
    * The with statement is used to wrap the execution of a block with methods defined by a context manager (see section With Statement Context Managers). This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.
  * [Context Manager in Python - GeeksforGeeks](https://www.geeksforgeeks.org/context-manager-in-python/)
```python
class ContextManager:
    def __init__(self, file_name) -> None:
        print('Entry of __init__()')
        self.file_name = file_name

    def __enter__(self):
        print('Entry of __enter__()')
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print('Entry of __exit__()')
        self.file.close()


if __name__ == '__main__':
    # Entry of __init__()
    # Entry of __enter__()
    # With statement block
    # Entry of __exit__()
    with ContextManager('my_file.txt') as xfile:
        print('With statement block')
        xfile.write('hello world')
```
* [Python 数据形态及IO操作](https://mp.weixin.qq.com/s/97v0k_hWdgJeppx1oF7Vxw)
* [13 ways to access data in Python. How to get data from local files… | by John Micah Reid | Towards Data Science](https://towardsdatascience.com/13-ways-to-access-data-in-python-bac5683e0063)
* [Python处理CSV、JSON和XML数据的简便方法](https://mp.weixin.qq.com/s/1PyeBLIJNzswO3zd-mHiTQ)
  * https://towardsdatascience.com/the-easy-way-to-work-with-csv-json-and-xml-in-python-5056f9325ca9
* [利用 tornado 实现表格文件预览](https://mp.weixin.qq.com/s/NVAzXKP801mfAfNRMvCjBw)
  * https://github.com/percent4/csv_file_review
* [Python 处理分析 128 张 Excel 表格竟不到3秒？| 附数据集](https://mp.weixin.qq.com/s/ZhWomp6LDgHHjf9Tr1dzvg)
  * https://github.com/seizeeveryday/DA-cases/tree/master/Python%2Bexcel
* [将Python字符串生成PDF](https://mp.weixin.qq.com/s/5R6t_oiOOV7qG4YkdLcpvA)
* [用 Python 操作 Word 文档](https://mp.weixin.qq.com/s/awN9gLqVn_s-STRzhioPXQ)
* [用 Python 实现文件自动归类](https://mp.weixin.qq.com/s/Ech_OeoDdYkd1ZmNjRIm_w)
* [5个案例让Python输出漂亮的表格！](https://mp.weixin.qq.com/s/8uxc2t53N_j_mRPYbiG0sA)
  * https://linuxops.org/blog/python/prettytable.html
  * prettytable可以打印出美观的表格，并且对中文支持相当好

## ADVANCE

* [5张图理解Python中的浅拷贝与深拷贝](https://mp.weixin.qq.com/s/em4OBWLdTqC7jdvyCs7Jhg)
* [图解 Python 中深浅拷贝](https://mp.weixin.qq.com/s/TtGFFDTKdPwCYj7gmIdp_Q)
  * https://blog.csdn.net/mall_lucy/article/details/104531218
  * 赋值运算
  	* l2 = l1是一个指向，是赋值，和深浅copy无关。
  * 浅copy
    * 浅copy：会在内存中新开辟一个空间，存放这个copy的列表，但是列表里面的内容还是沿用之前对象的内存地址。
  * 深copy
    * 深copy：会在内存中开辟新空间，将原列表以及列表里面的可变数据类型重新创建一份，不可变数据类型则沿用之前的。
  * 为什么Python默认的拷贝方式是浅拷贝？
    * 时间角度：浅拷贝花费时间更少。
    * 空间角度：浅拷贝花费内存更少。
    * 效率角度：浅拷贝只拷贝顶层数据，一般情况下比深拷贝效率高。
  * 总结：
    * 不可变对象在赋值时会开辟新空间。
    * 可变对象在赋值时，修改一个的值，另一个也会发生改变。
    * 深、浅拷贝对不可变对象拷贝时，不开辟新空间，相当于赋值操作。
    * 浅拷贝在拷贝时，只拷贝第一层中的引用，如果元素是可变对象，并且被修改，那么拷贝的对象也会发生变化。
    * 深拷贝在拷贝时，会逐层进行拷贝，直到所有的引用都是不可变对象为止。
    * Python 有多种方式实现浅拷贝，copy模块的copy 函数 ，对象的 copy 函数 ，工厂方法，切片等。
    * 大多数情况下，编写程序时，都是使用浅拷贝，除非有特定的需求。
    * 浅拷贝的优点：拷贝速度快，占用空间少，拷贝效率高。
* [Python 程序员如何防止数据被修改？](https://mp.weixin.qq.com/s/V8x6clZRK6k9T2rXwj2aDQ)
* [Python 进阶：全面解读高级特性之切片](https://mp.weixin.qq.com/s/afhvyDGjt8U2XzHCZHOJJA)
* [聊一聊 Python 中的闭包](https://mp.weixin.qq.com/s/qYKNGqItnSXq0-Zq2kMCKA)
  * https://segmentfault.com/a/1190000007321972
* [聊一聊 Python 中的“垃圾”回收](https://www.heroyf.club/2019/10/24/python_gc/)
* [Python 中 -m 的典型用法、原理解析与发展演变](https://mp.weixin.qq.com/s/tD3eSb2WdOPN_dKAQ9d6Ag)
* [IPython 中常用的魔法命令](https://mp.weixin.qq.com/s/5ZyfyR9r9zBod6ZP7scewA)

### [Classes / Object Oriented](https://www.tutorialspoint.com/python/python_classes_objects.htm)

* [Python 面向对象编程](http://www.langzi.fun/Python%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B.html)
  * 面向过程编程
  * 面向对象编程
  * 类的基本用法
  * 类与实例
  * 调用类的三种方法
    * 实例方法
    * 静态方法
    * 类方法
  * 类的特性
    * 封装
    * 继承
    * 多态
  * 魔法方法
    * \_\_doc\_\_
      * 说明性文档和信息。Python自建，无需自定义。　　
    * \_\_init\_\_
      * 实例化方法，通过类创建实例时，自动触发执行。　　
    * \_\_module\_\_ / \_\_class\_\_
      * module 表示当前操作的对象在属于哪个模块。
      * class 表示当前操作的对象属于哪个类。
      * 这两者也是Python内建，无需自定义。　　
    * \_\_del\_\_
      * 析构方法，当对象在内存中被释放时，自动触发此方法。
      * 注：此方法一般无须自定义，因为Python自带内存分配和释放机制，除非你需要在释放的时候指定做一些动作。析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。
    * \_\_call\_\_
      * 如果为一个类编写了该方法，那么在该类的实例后面加括号，可会调用这个方法。
      * 注：构造方法的执行是由类加括号执行的，即：对象 = 类名()，而对于call() 方法，是由对象后加括号触发的，即：对象() 或者 类()()
      * 可以用Python内建的callable()函数进行测试，判断一个对象是否可以被执行。
    * \_\_dict\_\_
      * 列出类或对象中的所有成员！非常重要和有用的一个属性，Python自建，无需用户自己定义。　　
    * \_\_str\_\_
      * 如果一个类中定义了str()方法，那么在打印对象时，默认输出该方法的返回值。这也是一个非常重要的方法，需要用户自己定义。　　
    * \_\_getitem\_\_ / \_\_setitem\_\_ / \_\_delitem\_\_
      * 取值、赋值、删除这“三剑客”的套路，在Python中，我们已经见过很多次了，比如前面的@property装饰器。
      * Python中，标识符后面加圆括号，通常代表执行或调用方法的意思。而在标识符后面加中括号[]，通常代表取值的意思。Python设计了getitem()、setitem()、delitem()这三个特殊成员，用于执行与中括号有关的动作。它们分别表示取值、赋值、删除数据。
      * 如果有一个类同时定义了这三个魔法方法，那么这个类的实例的行为看起来就像一个字典一样
    * \_\_iter\_\_
      * 这是迭代器方法！列表、字典、元组之所以可以进行for循环，是因为其内部定义了 iter()这个方法。如果用户想让自定义的类的对象可以被迭代，那么就需要在类中定义这个方法，并且让该方法的返回值是一个可迭代的对象。当在代码中利用for循环遍历对象时，就会调用类的这个iter()方法。　　
    * \_\_len\_\_
      * 在Python中，如果你调用内置的len()函数试图获取一个对象的长度，在后台，其实是去调用该对象的len()方法
      * Python的list、dict、str等内置数据类型都实现了该方法，但是你自定义的类要实现len方法需要好好设计。
    * \_\_repr\_\_
      * 这个方法的作用和str()很像，两者的区别是str()返回用户看到的字符串，而repr()返回程序开发者看到的字符串，也就是说，repr()是为调试服务的。通常两者代码一样。
    * \_\_add\_\_ / \_\_sub\_\_ / \_\_mul\_\_ / \_\_div\_\_ / \_\_mod\_\_ / \_\_pow\_\_
      * 这些都是算术运算方法，需要你自己为类设计具体运算代码。有些Python内置数据类型，比如int就带有这些方法。Python支持运算符的重载，也就是重写。　　
    * \_\_cmp\_\_
      * 比较运算
    * \_\_author\_\_
      * 作者信息　　
    * \_\_slots\_\_
      * Python作为一种动态语言，可以在类定义完成和实例化后，给类或者对象继续添加随意个数或者任意类型的变量或方法，这是动态语言的特性。
      * 但是！如果我想限制实例可以添加的变量怎么办？可以使slots限制实例的变量，比如，只允许Foo的实例添加name和age属性。
      * 需要提醒的是，slots定义的属性仅对当前类的实例起作用，对继承了它的子类是不起作用的。想想也是这个道理，如果你继承一个父类，却莫名其妙发现有些变量无法定义，那不是大问题么？如果非要子类也被限制，除非在子类中也定义slots，这样，子类实例允许定义的属性就是自身的slots加上父类的slots。
  * 成员保护与访问机制
    * 私有成员
    * 使用get-set-del方法操作私有成员
  * Propety装饰器
  * 常用的调用方法
  * 使用装饰器
  * 更加减半的使用property()函数
* [盘一盘 Python 系列特别篇 - 面向对象编程](https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247488340&idx=1&sn=572a046a414e830e209e8ea1c7cc92e0&chksm=e890905ddfe7194b2478fa00075469b83d997133290aef42d6c2af0db3aca1b46a6543823e11&scene=21#wechat_redirect)
  * 第一章 - 对象初体验
    * 1.1 整型 int
      * 在 C++ 和 Java 里，整数只是一个基础 (primitive) 类型，而在 Python 里，整数是一个类，可以用来创建很多整数型对象。
      * 用 dir(i) 可以浏览到整数下的属性
      * 对于 Python 使用者，用普通二进制操作符 (binary operator) + 和 * 就能实现加法和乘法运算。
      * 但对于 Python 开发者来说，他们是用魔法方法 (magic methods) __add__ 和 __mul__ 来实现加法和乘法运算的。
      * 这种更改 Python中运算符的含义的操作，被称为运算符重载 (overload operator)。
      * 最后看一个开发者用的最多的魔法函数，__repr__，它是 representation 的缩写。它会返回对象的一个编码字符串，可以用来重新创建对象，或者给开发者详细的显示。
      * 此外还有个 __str__ 魔法函数，它是 string 的缩写，作用和 __repr__ 差不多。它返回的编码字符串更加易读，因此是面向用户的，而不像 __repr__ 是面向开发者的。
    * 1.2 列表 list
      * 列表对象下没有字段 (fields)，只有方法 (methods)。
      * 首先介绍 __getitem__ 魔法方法，它的功能就是索引
    * 1.3 NumPy 数组 - ndarray
      * 你看 np 是类，arr 是对象，那么可以抽象成一下两种等价调用。
        * 对象.方法()
        * 类.方法(对象)
      * 虽然第二种语法更符合类中的方法定义，但第一种语法更简洁些，因此用的比较多。
      * 现在大概了解 __repr__ 和 __str__ 的区别了吧，前者准确无歧义，后者可读性强。
    * 1.4 Pandas 数据帧 - dataframe
  * 第二章 - 面向对象编程
    * 上节体验了四个 Python 内置类别：int, list, ndarray 和 dataframe。本节来以「雇员」为场景，来学习如何构建类、并弄清类的四大特征：封装、抽象、继承、多态。
    * 2.1 极简类和对象
    * 2.2 __init__() 和 self
      * 上节的类里是空的，实际的类是将属性聚集的，用的就是 __init__ 方法。这种将属性聚在一起称作封装 (encapsulation)，这是类的第一个特征。
      * 调用 __init__ 方法就是在构建类的实例，即对象。
    * 2.3 类变量 (千人千面)
      * 如果你想查看一个类或一个对象的详细信息，可以用 __dict__ 方法。
      * 总结：如果想让类变量千人千面，用 self.类变量
    * 2.4 类变量 (千人一面)
      * 总结：如果想让类变量千人一面，用 类名.类变量
    * 2.5 类方法 + 静态方法
      * 到目前为止，类里的方法都是实例方法 (instance method)，它们都适用于对象。本节介绍类方法 (class method) 和静态方法 (static method)。
      * 类方法适用于该类，即对该类下的所有对象的作用的相同的。类方法有两个特点：
        * 第一行要有装饰器 @classmethod (记住就行了)
        * 函数第一个参数必须是关键词 clf (对象一个参数必须是关键词 self）
      * 总结：类方法是所有对象和类都能调用，而且产生的效果是一样。
      * 一个类还会有些效用函数 (utility function)，它们不随对象和类的属性而改变，因此我们称它们为静态方法。
      * 静态方法也有两个特点：
        * 第一行要有装饰器 @staticmethod (记住就行了)
        * 函数参数绝对不能有关键词 clf 和 self
    * 2.6 其他构建函数
    * 2.7 继承和多态
      * 如果你想查看一个类里面详细内容的话，可以用 help(class)。如下图所示，注意灰色高亮处的 Method resolution order。
      * 现在完善子类 Developer，但是 __init__ 方法里面的代码重复。
      * 怎么精简？用 super 方法。见图第 6 行的 super().__init__() 就是在利用父类里的对象构造函数，而我们只用处理对于 Developer 对象的新字段
      * 因此它的构造函数 __init__ 有一个参数是 employee，初始值为 None。为什么不用空列表 [] 当初始值呢？原因就是列表是可变的 (mutable)。
      * 函数 isinstance(a, A) 是检查 a 是不是 A 的一个实例。
      * 函数 issubclass(A, B) 是检查 A 是不是 B 的一个子类。
    * 2.8 魔法方法
      * 魔法方法 (magic method) 的方法名前后被双下划线 (dunder) 所包围，构造函数 __init__ 就是最常见的魔法方法。
      * 其实所有类都是 object 类的子类，而 object 类里有两个重要的魔法方法，__repr__ 和 __str__，任何 object 的子类都会继承这两个方法。
      * 如果 Employee 中实现了 __str__，那么 print() 函数打印出来的是 __str__ 方法里的内容。
      * 如果 Employee 中没实现 __str__ 但实现了 __repr__，那么 print() 函数打印出来的是 __repr__方法里的内容。
      * 那么为了让 Employee 对象的打印出来信息更有用或者可读性更强，我们需要「用心」实现 __repr__ 和 __str__ 这两种方法。
      * __repr__()
        * 该方法是给开发者用的，因此输出应该是准确而无歧义的。
      * __str__()
        * 该方法是给用户用的，因此输出应该是可读性强的。
      * __add__()
        * 魔法方法 __add__ 重载了二元运算符 +。
    * 2.9 属性装饰器
      * 接下来我们用聪明方法，即属性装饰器 (property decorator)。
      * 只用加一句 @property。这样所有方法都可以当成属性用，即调用它们时不用打括号了
      * 这时我们需要用装饰器来定义 setter 方法，语法为 @fullname.setter。
      * 按同样的思路，用 @fullname.delete 来实现删除方法。
  * 总结
    * 在学习 OOP 之前，我们通过整数、列表、数组和数据帧这些“变量”，来看看它们下面属性，即字段和方法。先从思维上把“变量”转成“对象”。
    * 在学习 OOP 时，我们用雇员为例，学习如何定义类、构建对象、定义类方法和静态方法、继承父类雇员多态出开发者和经理、使用魔法方法、使用属性装饰器。并在中间穿插介绍了类的四大特征：封装、抽象、继承、多态。
```python
"""
盘一盘 Python 系列特别篇 - 面向对象编程
    https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247488340&idx=1&sn=572a046a414e830e209e8ea1c7cc92e0&chksm=e890905ddfe7194b2478fa00075469b83d997133290aef42d6c2af0db3aca1b46a6543823e11&scene=21#wechat_redirect
"""

import datetime


class Employee:
    num_of_emps = 0
    raise_rate = 1.05

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name: ', self.fullname)
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_rate)

    def __repr__(self) -> str:
        return 'Employee(\'{}\', \'{}\', {})'.format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname, self.email)

    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False

        return True


class Developer(Employee):
    raise_rate = 1.1

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname)
        print('---')


if __name__ == '__main__':
    print(Employee.num_of_emps)     # 0

    emp_1 = Employee('Steven', 'Wang', 200000)

    print(Employee.num_of_emps)     # 1

    emp_2 = Employee('Sherry', 'Zhang', 100000)

    print(Employee.num_of_emps)     # 2

    print(emp_1.pay)                # 200000
    emp_1.apply_raise()
    print(emp_1.pay)                # 210000

    print(Employee.raise_rate)      # 1.05
    print(emp_1.raise_rate)         # 1.05
    print(emp_2.raise_rate)         # 1.05

    Employee.raise_rate = 1.1

    print(Employee.raise_rate)      # 1.1
    print(emp_1.raise_rate)         # 1.1
    print(emp_2.raise_rate)         # 1.1

    emp_1.raise_rate = 1.05

    print(Employee.raise_rate)      # 1.1
    print(emp_1.raise_rate)         # 1.05
    print(emp_2.raise_rate)         # 1.1

    Employee.set_raise_rate(1.1)

    print(Employee.raise_rate)      # 1.1
    print(emp_1.raise_rate)         # 1.05 ?
    print(emp_2.raise_rate)         # 1.1

    emp_1.set_raise_rate(1.2)

    print(Employee.raise_rate)      # 1.2
    print(emp_1.raise_rate)         # 1.05 ?
    print(emp_2.raise_rate)         # 1.2

    my_date = datetime.date(2019, 10, 2)
    print(Employee.is_workday(my_date))     # True

    emp_str_3 = 'James-Harden-1000000'
    emp_3 = Employee.from_string(emp_str_3)

    print(emp_3.email)              # James.Harden@gmail.com

    dev_1 = Developer('Steven', 'Wang', 200000, 'Python')
    dev_2 = Developer('Sherry', 'Zhang', 100000, 'SQL')

    print(dev_1.email)              # Steven.Wang@gmail.com
    print(dev_1.prog_lang)          # Python

    print(help(Developer))
# Help on class Developer in module __main__:

# class Developer(Employee)
#  |  Developer(first, last, pay, prog_lang) -> None
#  |
#  |  Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, first, last, pay, prog_lang) -> None
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  raise_rate = 1.1
#  |
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Employee:
#  |
#  |  __repr__(self) -> str
#  |      Return repr(self).
#  |
#  |  __str__(self) -> str
#  |      Return str(self).
#  |
#  |  apply_raise(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods inherited from Employee:
#  |
#  |  from_string(emp_str) from builtins.type
#  |
#  |  set_raise_rate(rate) from builtins.type
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods inherited from Employee:
#  |
#  |  is_workday(day)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Employee:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  email
#  |
#  |  fullname
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Employee:
#  |
#  |  num_of_emps = 5

# None

    print(dev_1.pay)                # 200000
    dev_1.apply_raise()
    print(dev_1.pay)                # 220000

    mgr_1 = Manager('Jack', 'Black', 500000, [dev_1])

    print(mgr_1.email)              # Jack.Black@gmail.com
    mgr_1.print_emp()               # --> Steven Wang

    mgr_1.add_emp(dev_2)
    mgr_1.print_emp()               # --> Steven Wang --> Sherry Zhang

    mgr_1.remove_emp(dev_1)
    mgr_1.print_emp()               # --> Steven Wang

    print(isinstance(mgr_1, Manager))           # True
    print(isinstance(mgr_1, Employee))          # True
    print(isinstance(mgr_1, Developer))         # False

    print(isinstance(dev_1, Developer))         # True
    print(isinstance(dev_1, Employee))          # True
    print(isinstance(dev_1, Manager))           # False

    print(issubclass(Manager, Employee))        # True
    print(issubclass(Developer, Employee))      # True
    print(issubclass(Employee, Developer))      # False
    print(issubclass(Employee, Manager))        # False
    print(issubclass(Manager, Developer))       # False
    print(issubclass(Developer, Manager))       # False

    emp_1 = Employee('Steven', 'Wang', 200000)

    print(emp_1)                                # Steven Wang - Steven.Wang@gmail.com
    print(emp_1.__repr__())                     # Employee('Steven', 'Wang', 200000)
    print(emp_1.__str__())                      # Steven Wang - Steven.Wang@gmail.com

    print(emp_1.first)                          # Steven
    print(emp_1.email)                          # Steven.Wang@gmail.com
    print(emp_1.fullname)                       # Steven Wang

    emp_1.fullname = 'Tracy Mcgrady'

    print(emp_1.first)                          # Tracy
    print(emp_1.email)                          # Tracy.Mcgrady@gmail.com
    print(emp_1.fullname)                       # Tracy Mcgrady

    emp_1 = Employee('Steven', 'Wang', 200000)
    print(emp_1.fullname)                       # Steven Wang

    del emp_1.fullname                          # Delete Name:  Steven Wang
    print(emp_1.fullname)                       # None None
```
* [简单理解python面向对象及装饰器](https://mp.weixin.qq.com/s/jaoMUy5okkMZ9QOYK-og1Q)
  * 一、类
  * 二、继承
  * 三、多态
  * 四、封装
  * 五、装饰器
  * 六、闭包
    * @property：@property把类方法改成类属性，实现存取器
    * @classmethod：可以用来定义类方法（不用实例就可以调用）
    * @staticmethod：主要是方便将外部函数集成到类体中，并且用staticmethod包装的方法可以内部调用,也可以通过类访问或类实例化访问。
* [如何理解 Python 中的面向对象编程？](https://mp.weixin.qq.com/s/Jy1toECgoQyzJwCnEjQz-g)
  * https://www.blog.duomly.com/object-oriented-programming-in-python/
* [9.5.1. Multiple Inheritance - 9. Classes — Python 3.9.7 documentation](https://docs.python.org/3/tutorial/classes.html?highlight=method%20resolution%20order#multiple-inheritance)
  * For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
  * [method resolution order - Glossary — Python 3.9.7 documentation](https://docs.python.org/3/glossary.html#term-method-resolution-order)
    * Method Resolution Order is the order in which base classes are searched for a member during lookup. See [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) for details of the algorithm used by the Python interpreter since the 2.3 release.
  * [What is MRO in Python?](https://www.educative.io/edpresso/what-is-mro-in-python)
    * Method Resolution Order
    * MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
    * In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.
```python
class A:
    def method(self):
        print("A.method() called")


class B:
    def method(self):
        print("B.method() called")


class C(A, B):
    pass


class D(C, B):
    pass


d = D()
d.method()  # A.method() called
print(D.mro())  # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```
* [盘一盘 Python 系列特别篇 - 装饰器](https://mp.weixin.qq.com/s/ZWGZLur6_bdgZaIp_XzOxA)
* [5分钟全面掌握 Python 装饰器](https://mp.weixin.qq.com/s/Dx887iB-jn-BMdj3F1vHDQ)
* [读懂 Python 装饰器](https://mp.weixin.qq.com/s/pezg8naU4Afkf8DTm_m13w)
* [Python中的元编程：一个关于修饰器和元类的简单教程](https://mp.weixin.qq.com/s/bV7g9ugGmFjojGDMIc_kpQ)
  * https://medium.com/better-programming/meta-programming-in-python-7fb94c8c7152
* [如何将 Python 的一个类方法变为多个方法？](https://mp.weixin.qq.com/s/WPbtNQoMbMWVmD2IGOw8Rg)
* [写 Python 代码不可不知的函数式编程技术](https://mp.weixin.qq.com/s/cTUmjl8-laztpUSfSCW1hQ)
  * https://medium.com/better-programming/introduction-to-functional-programming-in-python-3d26cd9cbfd7

### [Regular Expressions](https://www.tutorialspoint.com/python/python_reg_expressions.htm)

* [Online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript](https://regex101.com/)
* [Regular Expressions Cheat Sheet by DaveChild - Download free from Cheatography - Cheatography.com: Cheat Sheets For Every Occasion](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)
* [Python3 正则表达式 | 菜鸟教程](http://www.runoob.com/python3/python3-reg-expressions.html)
* [盘一盘 Python 系列特别篇 - 正则表达式](https://mp.weixin.qq.com/s/Tewaynja3ggkcpzAli-1YQ)
* [re — Regular expression operations — Python 3.10.2 documentation](https://docs.python.org/3/library/re.html#module-re)
	* [re.compile(pattern, flags=0)](https://docs.python.org/3/library/re.html#re.compile)
		* Compile a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods, described below.
		* The expression’s behaviour can be modified by specifying a flags value. Values can be any of the following variables, combined using bitwise OR (the | operator).
	* [re.findall(pattern, string, flags=0)](https://docs.python.org/3/library/re.html#re.findall)
		* Return all non-overlapping matches of pattern in string, as a list of strings. The string is scanned left-to-right, and matches are returned in the order found. If one or more groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group. Empty matches are included in the result.
		* Changed in version 3.7: Non-empty matches can now start just after a previous empty match.
	* [re.search(pattern, string, flags=0)](https://docs.python.org/3/library/re.html#re.search)
		* Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
	* [re.match(pattern, string, flags=0)](https://docs.python.org/3/library/re.html#re.match)
		* If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern; note that this is different from a zero-length match.
		* Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
		* If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
* [Regular Expression HOWTO — Python 3.7.4 documentation](https://docs.python.org/3/howto/regex.html)
* [regex - Get all unnamed groups in a Python match object - Stack Overflow](https://stackoverflow.com/questions/30293064/get-all-unnamed-groups-in-a-python-match-object)
* [regex - Extracting 2 strings from regular expression Python - Stack Overflow](https://stackoverflow.com/questions/23658156/extracting-2-strings-from-regular-expression-python)
* [regex - Python extract pattern matches - Stack Overflow](https://stackoverflow.com/questions/15340582/python-extract-pattern-matches)
* [Python 正则表达式 re 模块简明笔记](https://mp.weixin.qq.com/s/8M_xiHMNB1a93ZunpxMsLg)
	* https://funhacks.net/2016/12/27/regular_expression/
* [Python正则表达式](https://mp.weixin.qq.com/s/bc-Puk4AVc1XxusrbSwaHg)
	* re模块主要定义了9个常量、12个函数、1个异常，每个常量和函数都会通过实际代码案例讲解，让大家能更直观的了解其作用！
```python
import re

filename = 'test.log'
pattern = re.compile('FinishedMessage from (?P<truck>.*):.*d=(?P<dump>.*)')
dumps = {}

with open( filename, 'r' ) as f:
    for line in f:
        print(line)

        match = re.search(pattern, line)
        print(match)

        if match:
            print(match.group(0))
            print(match.group(1))
            print(match.group(2))
            print(match.groupdict())
            print(match.groupdict()['truck'])
            print(match.groupdict()['dump'])

            dump = match.groupdict()['dump']

            if dump not in dumps:
                dumps[ dump ] = [ match.groupdict()['truck'] ]
            else:
                dumps[ dump ].append(match.groupdict()['truck'])
        print()

import pprint
pprint.pprint(dumps, width=1)

# =============================================================================
# [1] FinishedMessage from t1: group=[1] d=D1
#
# <re.Match object; span=(4, 43), match='FinishedMessage from t1: group=[1] d=D1'>
# FinishedMessage from t1: group=[1] d=D1
# t1
# D1
# {'truck': 't1', 'dump': 'D1'}
# t1
# D1
#
# [2] FinishedMessage from t2: group=[2] d=D2
#
# <re.Match object; span=(4, 43), match='FinishedMessage from t2: group=[2] d=D2'>
# FinishedMessage from t2: group=[2] d=D2
# t2
# D2
# {'truck': 't2', 'dump': 'D2'}
# t2
# D2
#
# [3] FinishedMessage from t3: group=[3] d=D2
# <re.Match object; span=(4, 43), match='FinishedMessage from t3: group=[3] d=D2'>
# FinishedMessage from t3: group=[3] d=D2
# t3
# D2
# {'truck': 't3', 'dump': 'D2'}
# t3
# D2
#
# {'D1': ['t1'],
#  'D2': ['t2',
#         't3']}
# =============================================================================
```

### [Database Access](https://www.tutorialspoint.com/python/python_database_access.htm)

* [Python与MySQL数据库的交互实战](https://blog.csdn.net/weixin_41261833/article/details/103832017)

```python
import psycopg2


class DBTest(object):
    """
    Database data retrieval
    """

    def __init__(self, config):
        self.connection = None

        self.db_config = {
            'host': config['host'],
            'database': config['name'],
            'user': config['user'],
            'password': config['password'],
            'port': config['port'] if 'port' in config else None,
            'application_name': 'equipment_simulator'
        }

    def __enter__(self):
        self.connect(self.db_config)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self, kwargs):
        """
        Instantiate DB connection
        """

        try:
            self.connection = psycopg2.connect(**kwargs)
        except (psycopg2.DatabaseError, psycopg2.InterfaceError) as error:
            raise Exception(error.message)

    def close(self):
        """
        Close the connection to the database
        """

        try:
            if self.connection is not None:
                self.connection.close()
                self.connection = None
        except (psycopg2.DatabaseError, psycopg2.InterfaceError) as error:
            raise Exception(error.message)

    @staticmethod
    def dict_fetchall(cursor):
        """
        :param cursor:
        :return: Return all rows from a cursor as a dict
        """

        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def get_data(self, key):
        if not key:
            return None

        query = '''
            select *
            from test_table
            where name in {}
        '''.format(tuple(key))

        cursor = self.connection.cursor()
        cursor.execute(query)
        results = self.dict_fetchall(cursor)

        return results


if __name__ == "__main__":
    input_config = {}
    input_key = ''

    with DBTest(config=input_config) as my_dbtest:
        key = input_key

        data = my_dbtest.get_data(key=key)
        print(data)
```

### [Multithreaded Programming](https://www.tutorialspoint.com/python/python_multithreading.htm)

* [multiprocessing — Process-based parallelism — Python 3.9.5 documentation](https://docs.python.org/3/library/multiprocessing.html)
* [学习笔记之asyncio — Asynchronous I/O - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/13531730.html)
```python
import asyncio
import logging
import zmq
import zmq.asyncio


class TestService:

    def __init__(self, url):
        self._url = url

        self._is_running = False
        self._zmq_context = None
        self._socket = None

    def _start(self):
        if self._is_running:
            return

        self._zmq_context = zmq.asyncio.Context()
        self._socket = self._zmq_context.socket(zmq.REP)
        self._socket.bind(self._url)

    def _stop(self):
        if not self._is_running:
            return

        if not self._socket.closed:
            self._socket.close()

    async def _process_message(self, data):
        # Process message here
        return data

    async def _recv_and_process(self):
        # need while loop to keep receiving and processing messages
        while (True):
            msg = await self._socket.recv_multipart()
            reply = await self._process_message(msg)
            await self._socket.send_multipart([reply,])

    def run(self):
        loop = None

        try:
            self._start()

            loop = asyncio.get_event_loop()
            loop.create_task(self._recv_and_process())
            loop.run_forever()

        except Exception as ex:
            logging.error('Error {}'.format(ex))

        finally:
            if loop is not None:
                loop.close()

            self._stop()
```
* [理解python多线程和多进程](https://mp.weixin.qq.com/s/pjoSXrpjvxvOHDmWAhYfFA)
* [深入理解python多线程和多进程](https://mp.weixin.qq.com/s/w0dZrtv8ogdtxO8FT2LrEg)
* [入门 | 三行Python代码，让数据预处理速度提高2到6倍](https://mp.weixin.qq.com/s/DgKuNIa_m-CsXWgHIz_3rQ)
  * https://towardsdatascience.com/heres-how-you-can-get-a-2-6x-speed-up-on-your-data-pre-processing-with-python-847887e63be5
* [Python 线程为什么要搞个 setDaemon ？](https://mp.weixin.qq.com/s/tRaQftWQNzE2a_ZKDLGE4w)
* [为什么 GIL 让多线程变得如此鸡肋？](https://mp.weixin.qq.com/s/QP4h36qqTWUKchrxN56v9A)
	* 这篇文章我们主要讲了 Python GIL 相关的问题。
	* 首先，我们了解到 GIL 属于 Python 解释器层面的，它并不是 Python 语言的特性，这一点我们一定不要搞混了。GIL 的存在会让 Python 在执行代码时，只允许同一时刻只有一个线程在执行，其目的是为了保证在执行过程中内存管理的安全性。
	* 之后我们通过一个例子，观察到 Python 在多线程运行 CPU 密集型任务时，执行效率比单线程还要低，其原因是因为在多核 CPU 环境下，GIL 的存在会导致多线程切换时无效的资源消耗，因此会降低程序运行的效率。
	* 但如果使用多线程运行 IO 密集型的任务，由于线程更多地是在等待 IO，所以并不会消耗 CPU 资源，这种情况下，使用多线程是可以提高程序运行效率的。
	* 最后，我们分析了 GIL 存在的原因，更多是因为历史问题导致，也正因为 GIL 的存在，很多 Python 开发者默认 Python 是线程安全的，这也间接增加了去除 GIL 的困难性。
	* 基于这些前提，我们平时在部署 Python 程序时，一般更倾向于使用多进程的方式去部署，就是为了避免 GIL 的影响。
	* 任何一种编程语言，都有其优势和劣势，我们需要理解它的实现机制，发挥其长处，才能更好地服务于我们的需求。

### 编码

* [一文透彻掌握 Python 编码问题](https://mp.weixin.qq.com/s/CFDH58dwU3ilMn1axJVccg)
* [一图看懂 Python 2 / Python 3 编码 | CSDN 博文精选](https://mp.weixin.qq.com/s/V9fM7G5c0JirQezoZAJVaw)

## PYTHONIC STYLE

### STYLE GUIDE

* [学习笔记之Python最简编码规范 - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/10387079.html)
* [写出漂亮 Python 代码的 20条准则](https://mp.weixin.qq.com/s/2I8clKTGDPbmR1fTOLWaZQ)
  * https://medium.com/better-programming/how-to-make-python-programming-more-elegant-and-decent-4b5962695aa9
* [Python 编码风格指南](https://mp.weixin.qq.com/s/JnrLSfQfH4CGAZSK_rnumg)
* [Python 简洁编码之道](https://mp.weixin.qq.com/s/UeOkqf37HQH-RQZbpJAiDQ)
* [改善Python程序的91个建议](https://zhuanlan.zhihu.com/p/32817459)
* [优雅编写Python3的62个小贴士](https://mp.weixin.qq.com/s/xkxpZo_8HixRlXU8PtMK7w)

### TIPS

* [@Python 程序员，如何最大化提升编码效率？](https://mp.weixin.qq.com/s/_-vCTkryiP2gq_IdX6pL8w)
  * https://towardsdatascience.com/five-python-tricks-you-need-to-learn-today-9dbe03c790ab
* [这些Python代码技巧，你肯定还不知道](https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/)
* [7个案例15分钟让你了解Python套路](https://www.jianshu.com/p/36ae91c38279)
* [Python带我飞：50个有趣而又鲜为人知的Python特性](https://github.com/leisurelicht/wtfpython-cn)
* [Python中实用却不常见的小技巧](https://hackernoon.com/python-tricks-101-2836251922e0)
  * https://github.com/brennerm/PyTricks
* [Python 开发中有哪些高级技巧？](https://mp.weixin.qq.com/s/6ierUk69wmooZcLKL3-XZw)
* [18 个 Python 高效编程技巧](https://mp.weixin.qq.com/s/2Bxc5u0X_NQtLuXbVvPfzQ)
* [10招玩转Python](https://mp.weixin.qq.com/s/WxYMY_b-5UPMD4KWPWIH9A)
* [学Python，从列表推导到zip()函数，这五种技巧应知应会](https://mp.weixin.qq.com/s/GDC3GeTPXspInK_1DPyuVA)
  * https://towardsdatascience.com/python-tricks-101-what-every-new-programmer-should-know-c512a9787022
* [Python的高级特征你知多少](https://mp.weixin.qq.com/s/VBiQ2X7Y93h51GkIosC_Vw)
* [26个Python实用技巧](https://mp.weixin.qq.com/s/ttuB63_N5SQdOhIwLFGYgg)
  * https://mp.weixin.qq.com/s/lPZTVURxfdRVYqIMUfnsBw
  * https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/
* [Python 有哪些不一样的技巧](https://mp.weixin.qq.com/s/w0OHrozLrD_n6v47Cit6BA)
* [即学即用的30段Python实用代码](https://mp.weixin.qq.com/s/KHj_j9PShDU7MFg6m15mBQ)
  * https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
* [每30秒学会一个Python小技巧](https://mp.weixin.qq.com/s/woVJXAI_8Gm7rIlaa6j7RQ)
  * https://github.com/30-seconds/30-seconds-of-python
* [Python的 5 种高级用法](https://towardsdatascience.com/5-advanced-features-of-python-and-how-to-use-them-73bffa373c84)
* [Python 的 20 个操作](https://mp.weixin.qq.com/s/WQHokL69JZIHdQ9j9fGJUw)
  * https://medium.com/better-programming/20-python-snippets-you-should-learn-today-8328e26ff124
* [Python技巧小贴士](https://mp.weixin.qq.com/s/SnUgTGvkZtsPwA7pkwEexA)
  * https://towardsdatascience.com/python-tips-and-trick-you-havent-already-seen-37825547544f
* [Python 十大语法](https://mp.weixin.qq.com/s/q_AiXIERqkq8wzEngMMxlQ)
* [20 个 Python 技巧](https://mp.weixin.qq.com/s/04BEb-rWp3igpzp1Av1hoA)
  * https://dev.to/duomly/20-useful-python-tips-and-tricks-you-should-know-3h8c
* [30 个 Python 的最佳实践、小贴士和技巧](https://mp.weixin.qq.com/s/B2jFB_m36_yaocsr3ZR-HQ)
  * https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5
* [几个 Python“小伎俩” | 内附代码](https://mp.weixin.qq.com/s/xM18GPGS794juIAzw2--IA)

## BEST PRACTICE

* [为什么有些高级开发不喜欢 Python？ (qq.com)](https://mp.weixin.qq.com/s/dVhGmbpOPYR5A1RvOFgalw)
  * [Why Some Senior Developers Don’t Like Python | by Mohammed Ayar | Better Programming](https://betterprogramming.pub/why-some-senior-developers-dont-like-python-974c5361fff2)
  * 动态类型
  * 全局解释器锁
  * 空白的敏感度
  * 空白的敏感度
* [Python编写循环的两个建议 | 鹅厂实战](https://mp.weixin.qq.com/s/Vh2pwcI_PjtoagaVmz2dHw)
  * https://github.com/piglei/one-python-craftsman
  * 什么是“地道”的循环？
    * enumerate() 所代表的编程思路
  * 建议1：使用函数修饰被迭代对象来优化循环
    * 使用 product 扁平化多层嵌套循环
    * 使用 islice 实现循环内隔行处理
    * 使用 takewhile 替代 break 语句
    * 使用生成器编写自己的修饰函数
  * 建议2：按职责拆解循环体内复杂代码块
    * 复杂循环体如何应对新需求
    * 使用生成器函数解耦循环体
  * 总结
    * 使用函数修饰被循环对象本身，可以改善循环体内的代码
    * itertools 里面有很多工具函数都可以用来改善循环
    * 使用生成器函数可以轻松定义自己的修饰函数
    * 循环内部，是一个极易发生“代码膨胀”的场地
    * 请使用生成器函数将循环内不同职责的代码块解耦出来，获得更好的灵活性
* [8个Python高效数据分析的技巧](https://mp.weixin.qq.com/s/l178i--vWqUaCdO99JG2pw)
  * https://towardsdatascience.com/python-for-data-science-8-concepts-you-may-have-forgotten-i-did-825966908393
* [7 个 Python 特殊技巧，有效提升数分效率！](https://mp.weixin.qq.com/s/nn-3GGhQwzgGf-qGS7TINg)
* 分享8点有用的Python编程建议
  * 项目文件事先做好归档
  * 永远不要手动修改源数据并且做好备份
  * 做好路径的正确配置
  * 代码必要的地方做好备注与说明
  * 加速你的Python循环代码
  * 可视化你的循环代码进度
  * 使用高效的异常捕获工具
  * 要多考虑代码健壮性
* [为什么Python不用设计模式？](https://mp.weixin.qq.com/s/HMZ0UJCGOS4GihjX_A5iNw)
* [动态类型一时爽，代码重构火葬场？](https://mp.weixin.qq.com/s/xjYK2f_ejVhshhn69uo7Cg)
* [Python 10大谬论](https://mp.weixin.qq.com/s/4UdLgFsZkt_Q_mdGOGHe4w)
* [给 Python 初学者的四条忠告](https://blog.csdn.net/xufive/article/details/102709538)
* [详解Python虚拟环境的原理及使用](https://mp.weixin.qq.com/s/kTyanAzsaiaieae8cpUwqg)
  * 本文先介绍虚拟环境的基础知识以及使用方法，然后再深入介绍虚拟环境背后的工作原理。

### 坑

* [Python 初学者常犯的5个错误，布尔型竟是整型的子类](https://mp.weixin.qq.com/s/RbITs-ekT2OJ41kA9RX9CA)
  * https://deepsource.io/blog/python-common-mistakes/
  * 可变的缺省参数
  * 将 assert 声明语句作为保证条件
  * 使用 isinstance 代替 type
    * type 和 isinstance 都能检查某个对象的类别是什么。但是它们间有非常重要的区别，isinstance 在解析目标类型时，它会关注继承关系，而 type 并不会。正因为这个区别，isinstance 在某些时候并不是我们所想的那样。
    * 因为布尔类型的变量在 Python 中是 int 的子类，isinstance(num, int) 同样会得出 True，这并不是我们想要的。在特定的类别中，使用 type 可能更加正确。
    * [type and isinstance in Python - GeeksforGeeks](https://www.geeksforgeeks.org/type-isinstance-python/)
      * If you’re checking to see if an object has a certain type, you want isinstance() as it checks to see if the object passed in the first argument is of the type of any of the type objects passed in the second argument. Thus, it works as expected with subclassing and old-style classes, all of which have the legacy type object instance.
      * type(), on the other hand, simply returns the type object of an object and comparing what it returns to another type object will only yield True when you use the exact same type object on both sides.
      * In Python, it’s preferable to use Duck Typing( type checking be deferred to run-time, and is implemented by means of dynamic typing or reflection) rather than inspecting the type of an object.
      * The next reason not to use type() is the lack of support for inheritance.
  * 不必要的 lambda 表达式
  * NotImplemented错误

### 运行速度

* [为什么Python这么慢?](https://hackernoon.com/why-is-python-so-slow-e5074b6fe55b)
* [一行代码让 Python 的运行速度提高100倍](https://mp.weixin.qq.com/s?__biz=MzUyODg4Nzk2MQ==&mid=2247490550&amp;idx=4&amp;sn=3a18cd95623880fd108ac0492bd9ec15&source=41#wechat_redirect)
  * https://mp.weixin.qq.com/s/Vm0BKSljCzMMgRmIBbpxdQ
* [24式加速你的Python](https://mp.weixin.qq.com/s/oEQOHLRdDkjOVzZhuIFeLg)
* [十步，教你把Python运行速度提升 30%](https://mp.weixin.qq.com/s/PJq0G8ae2H66QRCEs9FNrg)
  * https://towardsdatascience.com/making-python-programs-blazingly-fast-c1cd79bd1b32
* [如何加速Python代码？](https://mp.weixin.qq.com/s/QWH9qhKzECX-1rqDLfZyhw)
  * https://towardsdatascience.com/how-to-speed-up-your-python-code-d31927691012
  * 首先考虑优化你的算法和代码。
  * 如果原始速度可以解决你的问题，请考虑使用 PyPy。
  * 对 IO 密集型软件使用 threading 库和 asyncio。
  * 使用 multiprocessing 库解决 CPU 密集型问题。
  * 如果所有这些措施还不够的话，可以利用 Hadoop 等云计算平台进行扩展规模。
* [【进阶】[] 与 list() 哪个快？为什么快？快多少呢？](https://mp.weixin.qq.com/s/VndSpfOYFrrM_a2tzdOGDg)
  * [] 是 list() 的三倍快
  * list() 比 [] 执行步骤多
  * list() 的速度提升

### 内存

* [Python技巧 | 一行代码减少一半内存占用](https://mp.weixin.qq.com/s/0nTQ_oL2WWn8gytjqvn7SA)
* [如何降低 Python 的内存消耗量？](https://mp.weixin.qq.com/s/I4fNWX5sw6sAbRoyXiNNpw)
* [Python 内存分配时的小秘密](https://mp.weixin.qq.com/s/ZKscctriK6Hqw_MHwpQWIg)

### 资源库工具

* [Python算法实现资源汇总](https://mp.weixin.qq.com/s/1ODoGvRXQ0quk58rVPj4yQ)
  * https://github.com/TheAlgorithms/Python
* [那些有趣/用的 Python 库](https://mp.weixin.qq.com/s/gj6Dn5TLBoz_rqTeqYGduw)
* [140种Python标准库、第三方库和外部工具都有了](https://mp.weixin.qq.com/s/Qp12DRURa2I9AVjQ7gpxVw)
* [介绍几款 Python 类型检查工具](https://mp.weixin.qq.com/s/IvYJkpAmWJ-3ZEHtZzRiCQ)
  * pyright
* [Python中的两个测试工具](https://mp.weixin.qq.com/s/IUCoUkws923ojK__HPe3kA)
  * unittest: 一个通用的测试框架
  * doctest: 一个更简单的模块，是为检查文档而设计的，但也非常适合用来编写单元测试
* [Pytest - why it's more popular than unittest? - Blog j-labs](https://blog.j-labs.pl/2019/02/Pytest-why-its-more-popular-than-unittest)
  * Firstly, it’s worth to say, that pytest supports unittest.TestCase class from the beginning. All behaviors thought during writing tests with unittest (e.g.: writing assertions) remain the same, which gives extremely smooth transition to a new framework. Additionally, most unittest features work too, so pytest executor can run old tests as well (subtests are not supported).
  * Moreover, there are pytest features that work in unittest.TestCase subclasses like marking tests.
  * Experience from unittest in pytest – out-of-the-box
  * Distributed tests to multiple CPUs with xdist
  * Flowless integration with parameterized module
  * Marking tests as a manner of organizing the test suites
  * Handy extension - flake8
  * Generating HTML tests result
  * I personally prefer to use pytest instead of unittest. It’s fast and reliable. Despite the fact, that it reduces boilerplate code to the minimum, it still remains readable. Although, it’s not to be found in the standard library (which may be disadvantage for some), it may actually a clear advantage, because new releases of pytest are not bound to the Python official releases (which happens less frequently). Pytest helps me to organize my test suites and show test results to the others.  I highly recommend this tool.
* [用 coverage 模块提高 Python 开发效率](https://mp.weixin.qq.com/s/fP_mQtQnrssdzOOw6yPzQA)
  * Test with Coverage
  * Mock　
* [Python 中更优雅的日志记录方案](https://loguru.readthedocs.io/en/stable/index.html)
  * logging
  * loguru
* [如何编写完美的 Python 命令行程序？](https://mp.weixin.qq.com/s/sAS_NE8sIpw9ROOWSd60zw)
  * https://www.sicara.ai/blog/2018-12-18-perfect-command-line-interfaces-python
  * 我建议你遵循以下四条规则：
    * 尽可能提供默认参数值
    * 所有错误情况必须处理（例如，参数缺失，类型错误，找不到文件）
    * 所有参数和选项必须有文档
    * 不是立即完成的任务应当显示进度条
  * sys.argv
  * argparse
  * click
* [wxPython：Python首选的GUI库 | CSDN博文精选](https://mp.weixin.qq.com/s/pJIuKgZC1o757iwkrt3uUQ)
* [一份不可多得的数据科学与机器学习Python库](https://mp.weixin.qq.com/s/nkAKDx5OHx2Ld4Vo_RCXTQ)
* [收藏 | 34 个优秀好用的Python开源框架](https://github.com/Mybridge/amazing-python-2019)
  * https://medium.mybridge.co/34-amazing-python-open-source-libraries-for-the-past-year-v-2019-93d6ee11aceb
* [Python 依赖库管理哪家强？pip、pipreqs、pigar、pip-tools、pipdeptree](https://mp.weixin.qq.com/s/8kg7bgS0i4cPgKRwPKPOmA)
* [学习 Python，这 22 个包怎能不掌握？](https://mp.weixin.qq.com/s/vdDXAQlV94NdFBMb3eMF9w)
  * https://medium.com/better-programming/the-22-most-used-python-packages-in-the-world-7020a904b2e
* [3 个 Python 第三方模块的使用简介 ](https://mp.weixin.qq.com/s/PQqx6C0Ls-4YKCB0st2Ouw)
  * 本文将会介绍3个Python第三方模块的使用方法，它们分别是tqdm， pyyaml和traceback模块，各自的用途描述如下：
  * tqdm: 可以显示循环的进度条;
  * pyyaml：Python操作YAML文件的库；
  * tracebak：详细追踪错误信息的库。

## APPLICATION

* [用 Python 打包自己的库到 PYPI](https://mp.weixin.qq.com/s/9SdWsoJFJYDjkJal_QDocg)
  * https://www.zhihu.com/people/mai-da-3/activities
* [用 Pyinstaller 打包文件为应用程序](https://mp.weixin.qq.com/s/FuUds4jqj4o1GHEzCrz7Fw)
* [详细指南 | 如何在Github发布Python开源包](https://www.freecodecamp.org/news/from-a-python-project-to-an-open-source-package-an-a-to-z-guide-c34cb7139a22/)
* [用 Python 写一个安卓 APP](https://blog.51cto.com/youerning/1733534)
* [轻轻松松用Python写APP](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)
* [“堆”的 Python 实现与应用总结](https://mp.weixin.qq.com/s/cvUGuDSp_fb-kjHRe_zBPA)
  * https://zhuanlan.zhihu.com/p/85518062
* [如何用 Python 快速开发一个区块链数据结构？](https://mp.weixin.qq.com/s/m7hZY93ponge6dy2fvTzAg)
* [一文读懂Python复杂网络分析库networkx | CSDN博文精选](https://mp.weixin.qq.com/s/WYM7k9gddAndlLBuQWTbSA)
* [实战：基于技术分析的Python算法交易](https://mp.weixin.qq.com/s/J-ZwLl_CzvaRHZjKvTA3iw)
* [开发必学的验证码，教你从零写一个验证码](https://github.com/MiracleYoung/You-are-Pythonista/tree/master/PythonExercise/App/captcha_project)
* [用 Python 生成炫酷二维码及解析](https://mp.weixin.qq.com/s/V2g6DICFkVDOg-kI3QmnrA)
  * 我们通过 Python 生成以及识别二维码需要用到的库为：qrcode、myqr、zxing，安装通过 pip install qrcode/myqr/zxing 即可。
* [生成自定义二维码，5行Python代码就搞定](https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325)
* [万字干货 | Python后台开发的高并发场景优化解决方案](https://mp.weixin.qq.com/s/BHiM-mv7HXSmIY2KRf480g)
* [用 Python 偷偷抓取了她的行踪](https://github.com/xingag/spider_python/tree/master/%E8%8E%B7%E5%8F%96%E5%A5%B3%E5%8F%8B%E7%9A%84%E4%BD%8D%E7%BD%AE)
* [用Python可以算出了你的身份证号码](https://github.com/zpw1995/aotodata/blob/master/interest/ID_card/ID_card.py)
* [用 Python 自动监测 GitHub 项目更新](https://mp.weixin.qq.com/s/_nkx_cCKxz0VrfgGvWDcrA)
* [不到 50 行 Python 代码，做个刮刮卡](https://mp.weixin.qq.com/s/4WGYs4GMjObQZlObM2KkNQ)
* [用 Python 批量下载百度图片](https://mp.weixin.qq.com/s/q-obSiAt1Rs28itlKU2FiA)
* [用 Python 处理 B 站下载视频](https://mp.weixin.qq.com/s/dCTIUNeDQ_HeZqWQr0hesA)
* [如何用 Python 快速抓取 Google 搜索？](https://mp.weixin.qq.com/s/-GUgWH06Wy7pCzNbMjinXg)
  * https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal
  * https://github.com/getlinksc/scrape_google
* [用 Python 编写一个天气查询应用](https://mp.weixin.qq.com/s/iciMycq-HpwZj-LSE60NQQ)
* [大象装进冰箱要几步？Python 来解答](https://mp.weixin.qq.com/s/S5OWsuY1hT1qATadZ0v_kA)
* [用 Python 制作家用防盗工具](https://mp.weixin.qq.com/s/6RE1fwKF8gndI3Bnhb8UgA)
* [用 Python 制作“除夕夜倒计时”海报](https://mp.weixin.qq.com/s/MIhViQrYOca8QlQ7QEfoZw)
  * https://github.com/wwtm/gitpython_examples
* [Python GUI开发，效率提升10倍的方法](https://github.com/PySimpleGUI/PySimpleGUI)
* [用Python计算颜值数](https://mp.weixin.qq.com/s/d4r3oMReYCUBjUwCbAzE5w)
  * 现在很多拍照软件都有颜值测试及年龄识别功能，经过研究，发现 Python 也能实现，今天主要用 PyQt4 做个可视化工具，然后调用百度人脸识别api，识别出人脸的性别、年龄及颜值
* [用 Python 发一封邮件](https://mp.weixin.qq.com/s/wXAfYIdGxukKSstiFxLi4g)
* [如何用 Python 制作地球仪？](https://mp.weixin.qq.com/s/I6B5CDKRf8QDftAcIa_o_w)
  * 写在前面的话：在之前的文章 Python 图表利器 pyecharts 中有介绍了 pyecharts 的安装及使用,详细教程请到 官网 学习
  * pyecharts 功能很强大，只需要导入相应的模块就配置相应的选项即可生成对应的超文本文件，使用浏览器访问即可！具体实例请见下文

### AI

* [如何用 Python 构建机器学习模型？ (qq.com)](https://mp.weixin.qq.com/s/c-Sl7n_ceawz6AHm5Mtw0w)
  * 该 Notebook 包含了用于创建主要机器学习算法所需的代码模板。在 scikit-learn 中，我们已经准备好了几个算法。只需调整参数，给它们输入数据，进行训练，生成模型，最后进行预测。
```python
""" LinearRegression """

# Import modules
from sklearn import linear_model

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create linear regression object
linear = linear_model.LinearRegression()

# Train the model with training data and check the score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

# Collect coefficients
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

# Make predictions
predicted_values = linear.predict(x_test)

""" LogisticRegression """

# Import modules
from sklearn.linear_model import LogisticRegression

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create logistic regression object
model = LogisticRegression()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Collect coefficients
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

# Make predictions
predicted_vaues = model.predict(x_teste)

""" DecisionTreeRegressor """

# Import modules
from sklearn import tree

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted_variable

x_test  = test_dataset_precictor_variables

# Create Decision Tree Regressor Object
model = tree.DecisionTreeRegressor()

# Create Decision Tree Classifier Object
model = tree.DecisionTreeClassifier()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" GaussianNB """

# Import modules
from sklearn.naive_bayes import GaussianNB

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create GaussianNB object
model = GaussianNB()

# Train the model with training data
model.fit(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" svm """

# Import modules
from sklearn import svm

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create SVM Classifier object
model = svm.svc()

# Train the model with training data and checking the score
model.fit(x_train, y_train)
model.score(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" KNeighborsClassifier """

# Import modules
from sklearn.neighbors import KNeighborsClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create KNeighbors Classifier Objects
KNeighborsClassifier(n_neighbors = 6) # default value = 5

# Train the model with training data
model.fit(x_train, y_train)

# Make predictions
predicted_values = model.predict(x_test)

""" KMeans """

# Import modules
from sklearn.cluster import KMeans

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create KMeans objects
k_means = KMeans(n_clusters = 3, random_state = 0)

# Train the model with training data
model.fit(x_train)

# Make predictions
predicted_values = model.predict(x_test)

""" RandomForestClassifier """

# Import modules
from sklearn.ensemble import RandomForestClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Create Random Forest Classifier objects
model = RandomForestClassifier()

# Train the model with training data
model.fit(x_train, x_test)

# Make predictions
predicted_values = model.predict(x_test)

""" decomposition """

# Import modules
from sklearn import decomposition

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Creating PCA decomposition object
pca = decomposition.PCA(n_components = k)

# Creating Factor analysis decomposition object
fa = decomposition.FactorAnalysis()

# Reduc the size of the training set using PCA
reduced_train = pca.fit_transform(train)

# Reduce the size of the training set using PCA
reduced_test = pca.transform(test)

""" GradientBoostingClassifier """

# Import modules
from sklearn.ensemble import GradientBoostingClassifier

# Create training and test subsets
x_train = train_dataset_predictor_variables
y_train = train_dataset_predicted variable

x_test  = test_dataset_precictor_variables

# Creating Gradient Boosting Classifier object
model = GradientBoostingClassifier(n_estimators = 100, learning_rate = 1.0, max_depth = 1, random_state = 0)

# Training the model with training data
model.fit(x_train, x_test)

# Make predictions
predicted_values = model.predict(x_test)
```
* [不足 20 行 Python 代码，高效实现 k-means 均值聚类算法！](https://mp.weixin.qq.com/s/HCqzwwyA-EnDQpPsSUr8og)
  * https://blog.csdn.net/xufive/article/details/101448969
* [使用Python进行机器学习的假设检验（附链接&代码）](https://mp.weixin.qq.com/s/iC6I66_bBEHlnwZMEZsN_Q)
  * https://towardsdatascience.com/hypothesis-testing-in-machine-learning-using-python-a0dc89e169ce
* [Python 自然语言处理：轻松上手文本分类](https://mp.weixin.qq.com/s/ucPwBW5H-KBUPwCYEeFrug)
  * https://github.com/percent4/cnews_text_classification
* [用 Python 自制序列标注平台](https://mp.weixin.qq.com/s/CmlqkE0k8ccIVlz-hwrW2w)
  * https://github.com/percent4/entity_tagging_platform
* [用 Python 实现英文单词纠错功能](https://mp.weixin.qq.com/s/QeSYWq5bWzjN2atblkmFZw)
  * https://github.com/percent4/-word-
* [利用 50 行 Python 代码构建一个在线文本生成器！](https://mp.weixin.qq.com/s/HZmt38QfowwfpYhFxPx0aA)
  * https://towardsdatascience.com/build-a-text-generator-web-app-in-under-50-lines-of-python-9b63d47edabb
* [如何创建一个百分百懂你的产品推荐系统 | 深度教程（附代码详解）](https://mp.weixin.qq.com/s/Sj0fpz9xLOmJFjW4a7OcWQ)
* [如何通过 Python 和 OpenCV 实现目标数量监控？](https://mp.weixin.qq.com/s/pUGTKXplXgKtikH1Zh0tRA)
* [让二次元妹子动起来，用一张图生成动态虚拟主播](https://pkhungurn.github.io/talking-head-anime/)
* [用 Python 图像识别打造一个小狗分类器](https://mp.weixin.qq.com/s/il3Ou5wCMq0h2chP7Dnn1Q)
* [3行代码，搞定AI自动抠图](https://mp.weixin.qq.com/s/naSRo2heiACI0hTOSUZu9g)
* [Python中的图像增强技术](https://mp.weixin.qq.com/s/vqyaSK-Uis0vZrxu-KDMyw)
  * https://towardsdatascience.com/data-augmentation-techniques-in-python-f216ef5eed69
* [AI图像智能修复老照片](https://mp.weixin.qq.com/s/BlrViDMRKm8Hdj9nvkzxvQ)
  * 所使用的的python库有cv2库，目的是用来读取图片，处理图片像素值和保存图片等；numpy用来对读取过来的像素值矩阵进行运算。
* [19 行代码能搭建一个微信机器人](https://mp.weixin.qq.com/s/HP9zfgpHywaLi3NUPyFT5A)
  * wxpy 是一个封装好的微信个人号接口，在 itchat 的基础上，通过大量接口优化提升了模块的易用性。
* [当语音助手遇到机器人](https://mp.weixin.qq.com/s/I_hoLoLVPc0kfTCyMdSTag)
  * 图灵机器人（http://www.tuling123.com/）和 Siri 语音助手完成一次有趣的对话。
  * 使用到的技术有：
    * 图灵机器人（http://www.tuling123.com/）的 API 接口
    * 百度 AI开放平台的语音合成接口、OCR文字识别接口
    * ImageGrab 截图
    * 文件传输

### CRAWLER

* [Python 爬虫介绍 | 菜鸟教程](http://www.runoob.com/w3cnote/python-spider-intro.html)
  * https://blog.csdn.net/sinat_29957455/article/details/70846427
* [Scrapy Tutorial — Scrapy 2.5.0 documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [qzhsjz/BBCcrawl: A Spider to crawl Current BBC News. Using Scrapy Framework.](https://github.com/qzhsjz/BBCcrawl)
* [caiyingyi/news_classification_tool: 基于网络爬虫的外媒新闻分类统计工具的设计与实现](https://github.com/caiyingyi/news_classification_tool)
* [从零开始的 Python 爬虫速成指南](https://segmentfault.com/a/1190000008135000)
  * 本文主要内容：以最短的时间写一个最简单的爬虫，可以抓取论坛的帖子标题和帖子内容。
* [Python Scrapy爬虫框架学习 - SegmentFault 思否](https://segmentfault.com/a/1190000012041391?utm_source=sf-similar-article)
* [Python 爬虫分析豆瓣 TOP250 告诉你程序员业余该看什么书？- CSDN](https://mp.weixin.qq.com/s/nviBjYyJ0lyvkOFYaJ8cIg)
* [Python3 网络爬虫入门](https://cuijiahua.com/blog/2017/10/spider_tutorial_1.html)
* [如何炼成 Python 爬虫“王者”？](https://mp.weixin.qq.com/s/RGCGsinVeE9Nrm60mmix5g)
* [20行 Python 代码爬取王者荣耀全英雄皮肤 | 原力计划](https://mp.weixin.qq.com/s/3T8_L3j2sssNKHzzMgNkzQ)
  * https://blog.csdn.net/qq_42453117/article/details/103190981
* [基于 requests 的全能扫描王爬虫实践](https://mp.weixin.qq.com/s/J2DvsuEe9eO4ghPRlqKCrg)
* [基于微博数据的人物性格分类系统](https://mp.weixin.qq.com/s/MPepP7JaBT-KbFXiw7NZLA)
  * https://yishuihancheng.blog.csdn.net/
* [Python 分析国庆热门旅游景点](https://mp.weixin.qq.com/s/s-d5VxSbYKd1xmvS2XrvWQ)
  * https://github.com/pig6/qunar_spider
* [用 Python 总结分析男篮世界杯](https://mp.weixin.qq.com/s/z0HTipGNQ8ieVdEfSzkbVw)
* [用 Python 分析各国人口性别比例](https://mp.weixin.qq.com/s/tTMtJWQ6o10YJflmnGLxXg)
* [用Python分析全国高等教育分布情况](https://github.com/zhouwei713/data_analysis/tree/master/college)
* [Python 分析中国城市夜间灯光数据](https://mp.weixin.qq.com/s/iACTAa7OwkJqYGeO4zbq3g)
* [教你如何用Python自动下载抖音小姐姐](https://github.com/xingag/app_spider/tree/master/%E6%8A%96%E9%9F%B3-%E8%8E%B7%E5%8F%96%E5%A5%BD%E7%9C%8B%E7%9A%84%E5%B0%8F%E5%A7%90%E5%A7%90)
* [Python爬取的微信好友信息里我看到了自律 | CSDN博文精选](https://mp.weixin.qq.com/s/TOyQ3pfjyFOYG66HU0hpsg)
* [天气爬取+邮件发送](https://mp.weixin.qq.com/s/n93fPVfbcYuV4WfoprSe9g)
  * https://github.com/seizeeveryday/DA-cases/tree/master/Weather%2BEmail
* [基于 Fabric 部署分布式爬虫的思考](https://mp.weixin.qq.com/s/DSrAF40oWIStvtfKCE7pAA)
* [车票？工作？对象？Python 教你优雅解决年关三大难题](https://mp.weixin.qq.com/s/QQy2bs0t5jWC-tFysGtDpQ)
  * https://github.com/seizeeveryday/DA-cases/tree/master/Zhihu
* [用 Python 抓取公号文章保存成 PDF](https://mp.weixin.qq.com/s/jGjCfnGdxzK29FgC4E-_Cg)
* [Python 爬取 6271 家死亡公司数据，一眼看尽十年创业公司消亡史！ (qq.com)](https://mp.weixin.qq.com/s/c27WOcijEJw8d5zseK4Sxw)
  * aotodata/interest/6217 at master · zpw1995/aotodata (github.com)

#### FINANCE

* [看我如何抓取最新房价数据](https://mp.weixin.qq.com/s/7dGsf88Lm7T-isLHOzhz-Q)
* [看我如何抓取二手房价数据](https://mp.weixin.qq.com/s/fUFL_OjOUR48Ertx38F-xg)
* [用Python爬取淘宝](https://github.com/pig6/taobao_spider)
* [分析了16年的福利彩票记录，原来可以用Python这么买彩票](https://github.com/MiracleYoung/You-are-Pythonista/tree/master/PythonExercise/Tool/SSQ_Predict/)
* [用 Python 分析网易严选 Bra 销售信息](https://mp.weixin.qq.com/s/1_zWK4T6UNrQwnVQoxx7XQ)
* [爬了7000+条Bra信息](https://github.com/zhouwei713/data_analysis/tree/master/you163_spider)

#### MOVIE

* [Python登录豆瓣并爬取影评](https://mp.weixin.qq.com/s/Cpuh9S5rjvEkU_gPOoqQ5g)
* [Python 爬虫实战：猫眼电影](https://mp.weixin.qq.com/s/ROZfhenHD1EK6cbifj6oYg)
* [基于豆瓣影评数据的完整文本分析](https://mp.weixin.qq.com/s/qupUBFxVJvBSff9CksFI5w)
  * https://yishuihancheng.blog.csdn.net/
* [如何通过 Python 分析中国演员排名？](https://mp.weixin.qq.com/s/FezB7o5t5veSSKEt-YZV0w)
* [Python 爬取 3000 部电影，最具人气烂片排行榜出炉](https://mp.weixin.qq.com/s/sKvb-QgaO09DK7cGRGNFDg)
* [《庆余年》值得一看吗？Python告诉你谁在关注 | CSDN原力计划](https://mp.weixin.qq.com/s/dzZVtqQuJNFvjF-Qr7iPcw)
* [用 Python 抓取 bilibili 弹幕并分析](https://mp.weixin.qq.com/s/Skb9QSgBCH3iV4RfAV1szw)
* [用 Python 爬取分析每日票房数据](https://mp.weixin.qq.com/s/ag_BaGWNrcQokHlrFFSu2g)
  * http://blog.sina.com.cn/leonmovie
* [基于词典和弱标注信息的电影评论情感分析系统](https://mp.weixin.qq.com/s/3MX-fHI6WxuHGOHSY8RQCQ)
  * https://yishuihancheng.blog.csdn.net/

### DATA SCIENCE

* [《Python中神奇的第三方库：Faker》](https://mp.weixin.qq.com/s/1tk4xeWvwZ5oNhzaywgDgA)
  * [Python中第三方库-Faker](https://blog.csdn.net/mall_lucy/article/details/108655317)
  * 开发项目的时，为了测试常需要造假数据，经常要尽量的模拟真实环境，通常要费大量手工而且造出来的数据，而且通常手工造出来的看起来也很别扭，费时又费事，有没有更好的办法？有，这里给大家介绍一个“专业造数“库Faker，满足你对模拟数据的所有需求。
* [【实战】使用 Python 分析 14 亿条数据](https://juejin.im/post/5aceae206fb9a028d2084fea)
* [用 Python 绘制污染物玫瑰图](https://mp.weixin.qq.com/s/c3QMfbrkVgZhZ8BAvlqSgA)
  * https://yishuihancheng.blog.csdn.net/
* [用 Python 测算气象预报的空报率与漏报率](https://mp.weixin.qq.com/s/DiWXmYhm9IaeIqJVQaP3sg)
* [用 Python 观察台风气候](https://mp.weixin.qq.com/s/nStp7O9lznPeI1oTASgPZg)
* [用 Python 带你看各国 GDP 变迁](https://mp.weixin.qq.com/s/ILguXQZVAPcFqt7-7p3caA)
  * https://data.worldbank.org/
* [万字长文 | 超全代码详解Python制作精美炫酷图表教程](https://mp.weixin.qq.com/s/SFzAszv_T2yrSKbJYrd0gw)
  * https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f
* [用 Python 分析今年考研形势](https://mp.weixin.qq.com/s/1fABS9C3w87bWHxZ4SC_mQ)
* [用 Python 读取气象环境数据并绘图](https://mp.weixin.qq.com/s/RWPhPiYmJovxgfSrKOhAEg)
* [用Python数据分析了北京积分落户名单](https://github.com/zpw1995/aotodata/tree/master/bj_luohu)
* [如何用 Python 画出新型冠状病毒疫情地图？](https://mp.weixin.qq.com/s/DjBIu4851l0a_vN_aEjo7Q)
* [Python 硬核分析我国 14 亿人口，发现三大危机！](https://mp.weixin.qq.com/s/IFKYGMbxWbNTylBnE7zYBg)
  * https://github.com/pig6/china_population
* [怎么用 Python 画出好看的词云图？](https://mp.weixin.qq.com/s/Tuzfh9aKTN7_Fxt8YJ4q-w)
* [Python 竟能绘制出如此酷炫的三维图](https://jalammar.github.io/visual-numpy/)
* [用 Python 分析各国足球俱乐部排名](https://mp.weixin.qq.com/s/wakUY9phwcv1WPLo99og4A)
* [用 Python 对淘宝用户行为进行分析](https://mp.weixin.qq.com/s/CWTAhpu6VLsia1iCoLiuAA)
  * 本数据报告以淘宝app平台为数据集，通过行业的指标对淘宝用户行为进行分析，从而探索淘宝用户的行为模式，具体指标包括：日PV和日UV分析，付费率分析，复购行为分析，漏斗流失分析和用户价值RFM分析。
* [Python 制作动态图表，看全球疫情变化趋势](https://mp.weixin.qq.com/s/h3XaV7QfrcDMaUji1Y19Gw)
* [Python 招聘岗位数据可视化](https://mp.weixin.qq.com/s/lDiyXf9ORkDeD6akeqKEVA)
* [用 Python 做了一个全球疫情数据大屏](https://mp.weixin.qq.com/s/IbdEnZmG6UjCZvNVGWJcxg)
  * 爬虫模块负责从腾讯新闻获取数据，之后存入 Redis。Flask 是一个 Web 框架，负责 URL 和后台函数的映射，以及数据的传输。换言之，也就是从 Redis 中获取到原始数据，然后整理成相应的格式之后传递给前端页面，前端页面在拿到数据之后，调用百度的 ECharts 来实现图表的展示即可。
* [1行代码实现Python数据分析：图表美观清晰，自带对比功能](https://github.com/fbdesignpro/sweetviz)

### FINANCE

* [用 Python 获取股市交易数据](https://mp.weixin.qq.com/s/fPSIu4Czj5TxVAn9JEmV_Q)
  * Tushare 是一个免费、开源的 Python 财经数据接口包。主要实现对股票等金融数据从数据采集、清洗加工到数据存储的过程，能够为金融分析人员提供快速、整洁、和多样的便于分析的数据，为他们在数据获取方面极大地减轻工作量，使他们更加专注于策略和模型的研究与实现上。
* [用 Python 告诉你可转债打新能赚钱吗](https://mp.weixin.qq.com/s/xd8FDVKzVtaQejK8tGYrYw)
* [穿越熊市？用 Python 自制指数估值图](https://mp.weixin.qq.com/s/ka9DCqAOjSpID0lbMrBKSg)
  * 对于以定投指数的方式理财的朋友，最需要关注的指标便是各个指数的估值，在指数低估时买入，高估时卖出，那如何制作一张估值图来跟踪指数的估值情况呢？本文就从0到1介绍如何用Matplotlib画一张漂亮的指数估值图。
* [做时间的朋友，必须知道收益咋算](https://mp.weixin.qq.com/s/RAGr3DH-YLf8iApwWjAdMA)
  * https://github.com/Tacombel/XIRR.py
  * https://github.com/xiaolai/spreadsheets-for-investors
  * 年化复合回报 15% 意味着什么
  * 定投的收益
  * 定期不定额的收益率
  * 不定期不定额的收益率
* [定投改变命运？python 帮你解答](https://mp.weixin.qq.com/s/Jep0BGkmi0c_-9k4TkB3gA)
  * http://quotes.money.163.com/old/#HS
* [用 Python 创建一个比特币价格预警应用](https://mp.weixin.qq.com/s/qRMHlFVvviCwTX69MkQiVg)
  * 用 Python 发送电子邮件
  * 从 coinbase 交易所 API 中提取数据
  * 用 Python 在终端中隐藏密码
  * 在Time模块中使用超时功能
* [用苹果股价详解量化分析的4种基本操作](https://mp.weixin.qq.com/s/_6yXPJZx97pcbN5e_MMDaw)
  * 笔者今天就介绍一下Python在量化分析中的一些基本使用操作。今天讲的操作共有4种，都是我们经常用到的，而这4种操作都要用到pandas库，因为是量化分析，所以也要用到一些股票数据，我们就用“宇宙第一大股”苹果公司的股票数据来作为演示。
  * 首先还是导入各种库。
  * 这里我们稍微介绍一下yfinance，yfinance是使用Yahoo! Finance数据源的一个库，这个库的优点是下载速度快（没有被墙）、免费，同时导出来的数据就是pandas.DataFrame格式，非常好用。然后就是下载我们所需的苹果公司的股票数据
  * 有了数据，我们就开始介绍一下这4种基本操作。
    * 一、rolling window
    * 二、expanding window
    * 三、exponentially weighted moving window
    * 四、shift
* [酱香科技！用 Python 分析白酒类基金有多赚钱！](https://mp.weixin.qq.com/s/lNk79g2UK7vzSlIBac2Qcw)
  * 从采集基金数据然后进行分析
  * [招商中证白酒指数](https://danjuanapp.com/funding/161725?channel=1300100141)

### GAME

* [Python实现五子棋人机对战 | CSDN博文精选](https://mp.weixin.qq.com/s/SSdJW4aMgmv4wgJ02dr2MQ)
  * https://github.com/junxiaosong/AlphaZero_Gomoku
* [500行代码，教你用python写个微信飞机大战](https://github.com/MiracleYoung/You-are-Pythonista/tree/master/PythonExercise/App/plan_game)
* [手把手教你用Python实现“坦克大战”，附详细代码！](https://mp.weixin.qq.com/s/50iI6bfrZWnH7ASx9prqzA)
* [如何用 Python 实现超级玛丽的界面和状态机？](https://mp.weixin.qq.com/s/cOttH0PJKxJK2Y8dz3CLxQ)
  * https://blog.csdn.net/marble_xu/article/details/96427946
* [如何用 Python 实现超级玛丽的人物行走和碰撞检测？](https://mp.weixin.qq.com/s/GKx8cLRyJLUjlF92FZF9rQ)
  * https://blog.csdn.net/marble_xu/article/details/100022385
* [用 Python 实现植物大战僵尸代码！](https://mp.weixin.qq.com/s/w25oZEwPmTaBlrgvxBmG5Q)
  * https://blog.csdn.net/marble_xu/article/details/103100614
* [不到 150 行代码写一个 Python 版的贪吃蛇](https://mp.weixin.qq.com/s/ERVwKAOjB5M0yk-aCjQUCQ)
* [Python 小技之繁花盛开](https://mp.weixin.qq.com/s/vvXGXfMO1VSD3v8Mo3MVUQ)
  * 实现思路主要是利用之前学过的 Python 绘图模块 Turtle，Turtle 详细学习课程请参考趣玩 Python 之绘制基本图形 再结合随机函数生成任意的一棵树，樱花树主要组成部分有树干和花瓣以及飘落的花瓣构成。
* [用 Python 实现黑客帝国中的数字雨落既视感](https://mp.weixin.qq.com/s/95MKJwOzPcJCb_4Sn7RqBA)
  * 代码的实现还是比较简单，基本就是使用 pygame 库创建窗口，再定义数字的生成并让其不断的在窗口上面显示

## FAQ

* What's package and module ?
  * Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
  * 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。目录只有包含一个叫做 \_\_init\_\_.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
* How to install and update python ?
	* [How to Install Updated Python 3 on Mac](https://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/)
	* [Download Python | Python.org](https://www.python.org/downloads/)
* How to set pip install package index ?
  * Edit ~/.pip/pip.conf to set index-url / extra-index-url
  * [User Guide — pip 20.2.4 documentation (pypa.io)](https://pip.pypa.io/en/stable/user_guide/#configuration)
* Abstract base class v.s. Interface ?
  * Interfaces in Python: Protocols and ABCs · Abu Ashraf Masnun
  * There’s no interface keyword in Python. The Java / C# way of using interfaces is not available here. In the dynamic language world, things are more implicit. We’re more focused on how an object behaves, rather than it’s type/class.
  * PEP 3119 -- Introducing Abstract Base Classes | Python.org
    * https://www.python.org/dev/peps/pep-3119/
  * collections.abc — Abstract Base Classes for Containers — Python 3.8.0 documentation
    * https://docs.python.org/3/library/collections.abc.html#module-collections.abc
  * 3. Data model — Python 3.8.0 documentation
    * https://docs.python.org/3/reference/datamodel.html?highlight=__str__#object.__str__
    * Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable string representation of an object. The return value must be a string object.
  * Built-in Types — Python 3.8.0 documentation
    * https://docs.python.org/3/library/stdtypes.html#str
    * class str(object=b'', encoding='utf-8', errors='strict')
  * Duck typing - Wikipedia
    * https://en.wikipedia.org/wiki/Duck_typing
    * Duck typing in computer programming is an application of the duck test—"If it walks like a duck and it quacks like a duck, then it must be a duck"—to determine if an object can be used for a particular purpose. With normal typing, suitability is determined by an object's type. In duck typing, an object's suitability is determined by the presence of certain methods and properties, rather than the type of the object itself.[1]
  * 鸭子类型 - 维基百科，自由的百科全书
    * 鸭子类型（英语：duck typing）在程序设计中是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
    * 在鸭子类型中，关注点在于对象的行为，能作什么；而不是关注对象所属的类型。
    * 鸭子类型通常得益于"不"测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。
    * 在常规类型中，我们能否在一个特定场景中使用某个对象取决于这个对象的类型，而在鸭子类型中，则取决于这个对象是否具有某种属性或者方法——即只要具备特定的属性或方法，能通过鸭子测试，就可以使用。
  * oop - How do I implement interfaces in python? - Stack Overflow
    * https://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python
  * Difference between abstract class and interface in Python - Stack Overflow
    * https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
* How to use type annotations ?
  * typing — Support for type hints — Python 3.9.0 documentation
    * https://docs.python.org/3/library/typing.html
    * Note: The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
    * def greeting(name: str) -> str: ...
  * Using Python's Type Annotations - DEV
    * https://dev.to/dstarner/using-pythons-type-annotations-4cfe#:~:text=Type%20Annotations%20are%20a%20new,of%20a%20variable%20should%20be.&text=It%20is%20important%20to%20note,the%20program%20in%20any%20way.
* Comparisons
  * 6. Expressions — Python 3.7.4 documentation
    * https://docs.python.org/3/reference/expressions.html#comparisons
    * Unlike C, all comparison operations in Python have the same priority, which is lower than that of any arithmetic, shifting or bitwise operation. Also unlike C, expressions like a < b < c have the interpretation that is conventional in mathematics
    * Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).
* Conditional Expressions
  * 6. Expressions — Python 3.7.0 documentation
    * https://docs.python.org/3/reference/expressions.html?highlight=conditional%20expressions#conditional-expressions
    * x = 1 if y == 1 else 0
    * 注意Python中没有三元运算符 y == 1 ? 1 : 0
  * 1 PEP 308: Conditional Expressions
    * https://docs.python.org/2.5/whatsnew/pep-308.html
* How to display a decimal in scientific notation ?
  * '{:.2e}'.format(0.456) = '4.56e-01'
  * '{:.2f}'.format(0.456) = '0.46'
  * python - Display a decimal in scientific notation - Stack Overflow
    * https://stackoverflow.com/questions/6913532/display-a-decimal-in-scientific-notation
* What's the infinity number ?
  * float('inf')
  * Built-in Types — Python 3.7.4 documentation
    * https://docs.python.org/3/library/stdtypes.html?highlight=float%20inf
    * float also accepts the strings “nan” and “inf” with an optional prefix “+” or “-” for Not a Number (NaN) and positive or negative infinity.
  * sys.maxsize
  * python - Maximum and Minimum values for ints - Stack Overflow
    * https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
    * In Python 3, this question doesn't apply. The plain int type is unbounded.
    * However, you might actually be looking for information about the current interpreter's word size, which will be the same as the machine's word size in most cases. That information is still available in Python 3 as sys.maxsize, which is the maximum value representable by a signed word. Equivalently, it's the size of the largest possible list or in-memory sequence.
  * sys — System-specific parameters and functions — Python 3.8.2 documentation
    * https://docs.python.org/3/library/sys.html#sys.maxsize
    * An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2\*\*31 - 1 on a 32-bit platform and 2\*\*63 - 1 on a 64-bit platform.
* zip
  * https://docs.python.org/3/library/2to3.html?highlight=zip#2to3fixer-zip
  * Wraps zip() usage in a list call. This is disabled when from future_builtins import zip appears. 
* How to convert dictionary to list ?
  * Converting Python Dictionary to List - Stack Overflow
    * https://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
  * 4. Built-in Types — Python 3.6.6rc1 documentation
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dict.items
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dictionary-view-objects
  * 5. Data Structures — Python 3.8.3 documentation
    * https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
* How to convert list to string ?
  * stest = str(['test1', 'test2', 'test3']).strip('[]')
  * 4. Built-in Types — Python 3.6.6rc1 documentation
    * https://docs.python.org/3/library/stdtypes.html?highlight=str#text-sequence-type-str
    * https://docs.python.org/3/library/stdtypes.html?highlight=str#str.strip
  * python - TypeError: cannot concatenate 'str' and 'list' objects in email - Stack Overflow
    * https://stackoverflow.com/questions/26521899/typeerror-cannot-concatenate-str-and-list-objects-in-email
* How to convert list to tuple ?
  * tuple( list_obj )
  * Python | Convert a list into a tuple - GeeksforGeeks
    * https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
    * tuple(list)
    * tuple(i for i in list)
    * (*list, )
* How to check if a list contains elements of another list ?
  * check = all(item in List1 for item in List2)
  * check = any(item in List1 for item in List2)
  * Check if Python List Contains Elements of Another List
    * https://www.techbeamers.com/program-python-list-contains-elements/
  * Built-in Functions — Python 3.7.4 documentation
    * https://docs.python.org/3/library/functions.html?highlight=any#any
    * https://docs.python.org/3/library/functions.html?#all
* How to change values in a list with for loop ?
  * enumerate
  * Change values in a list using a for loop (python) - Stack Overflow
    * https://stackoverflow.com/questions/54974579/change-values-in-a-list-using-a-for-loop-python
```python
list_a = [0] * 10
 
for index, value in enumerate(list_a):
    if index > 5:
        list_a[index] = -1
```
* How to reverse list ?
  * r_tests = tests[::-1]
  * r_tests = reversed(tests)
  * [reversed - Built-in Functions — Python 3.9.6 documentation](https://docs.python.org/3/library/functions.html?highlight=reverse#reversed)
    * Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).
* How to check if substring exists ?
  * if "substring" in test_string:
  * if s.startswith(("a", "b")):
  * 6. Expressions — Python 3.7.2rc1 documentation - Membership test operations
    * https://docs.python.org/3/reference/expressions.html#membership-test-details
  * Built-in Types — Python 3.7.2rc1 documentation
    * str.startswith(prefix[, start[, end]])
    * Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
  * Does Python have a string 'contains' substring method? - Stack Overflow
    * https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
    * if "blah" not in somestring: 
* How to replace characters / substring in a string ?
  * 'www.example.com'.strip('cmowz.')
  * str.replace('html', 'log')
  * Pay attention that strip will only remove the leading and trailing characters.
  * Built-in Types — Python 3.7.1 documentation - str.strip([chars])
    * https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip
    * Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped
  * str.replace(old, new[, count])
    * https://docs.python.org/3/library/stdtypes.html?highlight=replace#str.replace
    * Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
* How to sort string ?
  * [How to sort the letters in a string alphabetically in Python - Stack Overflow](https://stackoverflow.com/questions/15046242/how-to-sort-the-letters-in-a-string-alphabetically-in-python)
  * ''.join(sorted(a))
* How to split string ?
  * [str.split(sep=None, maxsplit=-1) - Built-in Types — Python 3.9.6 documentation](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split) 
    * Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
    * If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
  * [python中split()和split(' ')的区别 - 少年与python - 博客园](https://www.cnblogs.com/python-coder/p/10073329.html)
    * split()的时候，多个空格当成一个空格；split(' ')的时候，多个空格都要分割，每个空格分割出来空。
* Two types usage of for loop ?
  * python - "for loop" with two variables? - Stack Overflow
    * https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
* How to find the min value in dictionary ?
  * min(d.items(), key=lambda x: x[1])
  * min(d.items(), key=d.get)
  * min(d.values())
  * min(d.keys())
  * python - Get the key corresponding to the minimum value within a dictionary - Stack Overflow
    * https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    * min(d, key=d.get)
  * python - Getting key with maximum value in dictionary? - Stack Overflow
    * https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
  * 2. Built-in Functions — Python 3.7.0 documentation
    * https://docs.python.org/3/library/functions.html?highlight=min#min
    * https://docs.python.org/3/library/stdtypes.html?highlight=dictionary#dict.get
      * get(key[, default])
      * Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
  * Python3 min() 函数 | 菜鸟教程
    * http://www.runoob.com/python3/python3-func-number-min.html
  * Python3 字典 get() 方法 | 菜鸟教程
    * http://www.runoob.com/python3/python3-att-dictionary-get.html
* How to iterate over a dictionary ?
  * for key in dict
  * for value in dict.values()
  * for key, value in dict.items()
  * Iterate over a dictionary in Python - GeeksforGeeks
    * https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
  * Python3 字典 in 操作符 | 菜鸟教程　　
    * https://www.runoob.com/python3/python3-att-dictionary-in-html.html
    * Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
* How to delete an item from dictionary ?
  * Built-in Types — Python 3.8.2 documentation
    * https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    * del d[key]
      * Remove d[key] from d. Raises a KeyError if key is not in the map.
    * pop(key[, default])
      * If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
  * Dictionary Tutorials & Notes | Python | HackerEarth
    * https://www.hackerearth.com/practice/python/working-with-data/dictionary/tutorial/
  * python - Delete a dictionary item if the key exists - Stack Overflow
    * mydict.pop("key", None)
* How to check if dictionary/list/string/tuple is empty ?
  * PEP 8 -- Style Guide for Python Code | Python.org
    * https://www.python.org/dev/peps/pep-0008/
    * For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
    * Yes: if not seq: / if seq:
    * No: if len(seq): / if not len(seq):
  * Python: Checking if a 'Dictionary' is empty doesn't seem to work - Stack Overflow
    * https://stackoverflow.com/questions/23177439/python-checking-if-a-dictionary-is-empty-doesnt-seem-to-work
  * python - How do I check if a list is empty? - Stack Overflow
    * https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
* How to print lists ?
  * Print lists in Python (4 Different Ways) - GeeksforGeeks
  * https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
```python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:05:55 2018

@author: h.tang
"""

# using for loop
a = [1, 2, 3, 4, 5]

# =============================================================================
# 1. Using for loop : Traverse from 0 to len(list) and print all elements of the list one by one uisng a for loop,
# this is the standard practice of doing it.
# =============================================================================
#1
#2
#3
#4
#5
#1 2 3 4 5

# printing the list using loop
for x in range(len(a)):
    print a[x]

for x in range(len(a)):
    print a[x],

# =============================================================================
# 2. Without using loops: * symbol is use to print the list elements in a single line with space.
# To print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively.
# =============================================================================
# Python program to print list
# without using loop

a = [1, 2, 3, 4, 5]

#1 2 3 4 5
#printing lists separated by commas
#1, 2, 3, 4, 5
#printing lists in new line
#1
#2
#3
#4
#5

# printing the list using * operator separated
# by space
print(*a)

# printing the list using * and sep operator
print("printing lists separated by commas")

print(*a, sep = ", ")

# print in new line
print("printing lists in new line")

print(*a, sep = "\n")

# =============================================================================
# 3. Convert a list to a string for display : If it is a list of strings we can simply join them using join() function,
# but if the list contains integers then convert it into string and then use join() function to join them to a string and print the string.
# =============================================================================
# Python program to print list
# by Converting a list to a
# string for display
a =["Geeks", "for", "Geeks"]

#Geeks for Geeks
#1, 2, 3, 4, 5

# print the list using join function()
print(' '.join(a))

# print the list by converting a list of
# integers to string
a = [1, 2, 3, 4, 5]

print str(a)[1:-1]

# =============================================================================
# 4. Using map : Use map() to convert each item in the list to a string if list is not a string, and then join them
# =============================================================================
# Python program to print list
# print the list by converting a list of
# integers to string using map
a = [1, 2, 3, 4, 5]
#1 2 3 4 5
#in new line
#1
#2
#3
#4
#5
print(' '.join(map(str, a)))

print"in new line"
print('\n'.join(map(str, a)))
```
* How to create and initialise list with repeated N times ?
  * x = [5]
  * print(x * 5)　　// [5, 5, 5, 5, 5]
  * print([x] * 5)　// [[5], [5], [5], [5], [5]]
  * Create List of Single Item Repeated n Times in Python - Stack Overflow
    * https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times-in-python/3459131
    * [e] * n
  * [ [ 1 for x in range(n) ] for x in range(m) ]
  * [How do I create a multidimensional list?](https://docs.python.org/3/faq/programming.html#how-do-i-create-a-multidimensional-list)
    * The reason is that replicating a list with * doesn’t create copies, it only creates references to the existing objects. The *3 creates a list containing 3 references to the same list of length two. Changes to one row will show in all rows, which is almost certainly not what you want.
    * The suggested approach is to create a list of the desired length first and then fill in each element with a newly created list
    * Or, you can use an extension that provides a matrix datatype; NumPy is the best known.
    * YES: A = [[None] * w for i in range(h)]
    * NO: A = [[None] * 2] * 3
    * https://docs.python.org/3/library/stdtypes.html?highlight=list#typesseq-common
      * What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are references to this single empty list. Modifying any of the elements of lists modifies this single list. 
      * YES: lists = [[] for i in range(3)]
      * NO: lists = [[]] * 3
* How to remove duplicates in lists ?
  * python - Removing duplicates in lists - Stack Overflow
    * https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
    * list(set(t))
  * 5. Data Structures — Python 3.7.0 documentation
    * https://docs.python.org/3/tutorial/datastructures.html#sets
    * Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
* How to print dictionary / list on multiple lines with pprint?
  * pprint — Data pretty printer — Python 3.7.4 documentation
    * https://docs.python.org/3.7/library/pprint.html
  * python - pprint dictionary on multiple lines - Stack Overflow
    * https://stackoverflow.com/questions/20171392/pprint-dictionary-on-multiple-lines
  * 如何美观地打印 Python 对象？这个标准库可以简单实现
    * https://mp.weixin.qq.com/s/ePlvdBu8VsS5xnqimv71CQ
* What's defaultdict ?
  * collections — Container datatypes — Python 3.8.5 documentation
  * https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict
  * class collections.defaultdict([default_factory[, ...]])
  * Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.
  * The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
* What's deque ?
  * collections — Container datatypes — Python 3.8.2 documentation
    * https://docs.python.org/3/library/collections.html?highlight=deque#deque-objects
    * class collections.deque([iterable[, maxlen]])
    * Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.
    * pop()
      * Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.
    * popleft()
      * Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.
  * queue — A synchronized queue class — Python 3.8.2 documentation
    * https://docs.python.org/3/library/queue.html
    * The queue module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when information must be exchanged safely between multiple threads. The Queue class in this module implements all the required locking semantics.
  * python - Queue.Queue vs. collections.deque - Stack Overflow
    * https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque
    * Queue.Queue and collections.deque serve different purposes. Queue.Queue is intended for allowing different threads to communicate using queued messages/data, whereas collections.deque is simply intended as a datastructure. That's why Queue.Queue has methods like put_nowait(), get_nowait(), and join(), whereas collections.deque doesn't. Queue.Queue isn't intended to be used as a collection, which is why it lacks the likes of the in operator.
    * It boils down to this: if you have multiple threads and you want them to be able to communicate without the need for locks, you're looking for Queue.Queue; if you just want a queue or a double-ended queue as a datastructure, use collections.deque.
* What's namedtuple ?
  * collections — Container datatypes — Python 3.8.0 documentation
    * https://docs.python.org/3/library/collections.html#collections.namedtuple
    * collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
    * Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
    * collections — Container datatypes — Python 3.8.2 documentation
      * https://docs.python.org/3.8/library/collections.html?highlight=namedtuple#collections.somenamedtuple._replace
      * somenamedtuple._replace(**kwargs)
      * Return a new instance of the named tuple replacing specified fields with new values
* How to use enumerations ?
  * enum — Support for enumerations — Python 3.8.1 documentation
    * https://docs.python.org/3/library/enum.html?highlight=enum#enum.Enum
  * Design and History FAQ — Python 3.8.1 documentation
    * https://docs.python.org/3/faq/design.html?highlight=switch%20case#why-isn-t-there-a-switch-or-case-statement-in-python
* How to check type of object ?
  * x = isinstance(5, int)
  * Built-in Functions — Python 3.7.4 documentation
    * https://docs.python.org/3/library/functions.html#isinstance
  * Python isinstance() Function
    * https://www.w3schools.com/python/ref_func_isinstance.asp
* How to check if object has an attribute ?
  * Built-in Functions — Python 3.8.5 documentation
    * [hasattr(object, name)](https://docs.python.org/3/library/functions.html#hasattr)
      * The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. (This is implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not.)
    * [object.__getattr__(self, name)](https://docs.python.org/3/reference/datamodel.html#object.__getattr__)
      * Called when the default attribute access fails with an AttributeError (either __getattribute__() raises an AttributeError because name is not an instance attribute or an attribute in the class tree for self; or __get__() of a name property raises AttributeError). This method should either return the (computed) attribute value or raise an AttributeError exception.
    * [object.__getattribute__(self, name)](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__)
      * Called unconditionally to implement attribute accesses for instances of the class. If the class also defines __getattr__(), the latter will not be called unless __getattribute__() either calls it explicitly or raises an AttributeError. This method should return the (computed) attribute value or raise an AttributeError exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example, object.__getattribute__(self, name).
  * How to know if an object has an attribute in Python - Stack Overflow
    * https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
* How to check if file exists ?
  * os.path — Common pathname manipulations — Python 3.7.2 documentation
    * https://docs.python.org/3/library/os.path.html?highlight=isfile#os.path.isfile
    * os.path.isfile(path)
    * Return True if path is an existing regular file. This follows symbolic links, so both islink() and isfile() can be true for the same path.
  * Python: Check if a File or Directory Exists
    * https://stackabuse.com/python-check-if-a-file-or-directory-exists/
    * Checking if a File Exists
      * os.path.isfile()
    * Checking if a Directory Exists
      * os.path.isdir()
    * Checking if Either Exist
      * os.path.exists()
* How to use try ... except ... finally statement for exception ?
  * 8.4. The try statement - 8. Compound statements — Python 3.7.4 documentation
    * https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
  * Manually raising (throwing) an exception in Python - Stack Overflow
    * https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python　　
* How to define custom exception ?
  * How to Define Custom Exceptions in Python? (With Examples)
    * https://www.programiz.com/python-programming/user-defined-exception
* How to use logging ?
  * Logging HOWTO — Python 3.7.0 documentation
    * https://docs.python.org/3.7/howto/logging.html#basic-logging-tutorial
  * 16.6. logging — Logging facility for Python — Python 3.7.0 documentation
    * https://docs.python.org/3.7/library/logging.html#logging.debug
    * https://docs.python.org/3.7/library/logging.html#logging.info
    * https://docs.python.org/3.7/library/logging.html#logging.warning
    * https://docs.python.org/3.7/library/logging.html#logging.error
    * https://docs.python.org/3.7/library/logging.html#logging.exception
    * https://docs.python.org/3.7/library/logging.html#logging.basicConfig
    * https://docs.python.org/3.7/library/logging.html?highlight=shutdown#logging.shutdown
    * logging.basicConfig( filename=output.replace('html', 'log'), filemode='w',  format='[%(asctime)s] \n%(message)s',  datefmt='%Y-%m-%d %H:%M:%S',  level=logging.DEBUG )
    * logging.getLogger(name=None)
      * https://docs.python.org/3.7/library/logging.html?highlight=getlogger#logging.getLogger　　
      * Return a logger with the specified name or, if name is None, return a logger which is the root logger of the hierarchy. If specified, the name is typically a dot-separated hierarchical name like ‘a’, ‘a.b’ or ‘a.b.c.d’. Choice of these names is entirely up to the developer who is using logging.
      * All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
  * Logging Cookbook — Python 3.7.0 documentation
    * https://docs.python.org/3/howto/logging-cookbook.html
  * Good logging practice in Python – Fang's coding note
    * https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
  * For the issue setLevel() doesn't work logger.setLevel(logging.DEBUG) , fix it with logging.basicConfig(level=logging.DEBUG).
  * To set logging level with variable e.g. loglevel
    * https://docs.python.org/3/howto/logging.html#logging-to-a-file
    * logging.basicConfig(level=getattr(logging, loglevel.upper()))
* How to measure execution time of code ?
  * timeit — Measure execution time of small code snippets — Python 3.8.0 documentation
    * https://docs.python.org/3.8/library/timeit.html
* How to import module from parent directory ?
  * import sys
  * sys.path.append('..')
  * from A import B
  * python - Importing modules from parent folder - Stack Overflow
    * https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
  * [学了半天，import 到底在干啥？](https://mp.weixin.qq.com/s/FN__-XO_-htH36jPLiiTZg)
* How to parse arguments for command-line options ?
  * 15.4. argparse — Parser for command-line options, arguments and sub-commands — Python 2.7.16 documentation
    * https://docs.python.org/2.7/library/argparse.html?highlight=arg%20parse#the-add-argument-method
  * python - What's the best way to parse command line arguments? - Stack Overflow
    * https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
  * python - Why use argparse rather than optparse? - Stack Overflow
    * https://stackoverflow.com/questions/3217673/why-use-argparse-rather-than-optparse
```python
import argparse

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(prog='test',
                                         description='Test class A')

        parser.add_argument('-c',
                            '--config',
                            metavar='file',
                            help='Path to file',
                            required=True)

        args = parser.parse_args()

        print("args.config = {0}\n".format(args.config))

    except (AttributeError, TypeError, RuntimeError) as err:
        logger.logError(err.message)

    except Exception as err:
        logger.logException(err.message)
```

### FIX OF ERRORS

* How to fix AttributeError: MyBokeh instance has no attribute 'plot_all' ?
  * Check the indentation for other class member functions prior to plot_all()
* How to fix "Invalid syntax" when using python3 feature typing?
	* add below on the top to specify the env python3
```python
#!/usr/bin/env python3
```
* How to fix memory error when slicing list ?
  * One possibility is to use generator
  * [python - string[i:length] giving memory error - Stack Overflow](https://stackoverflow.com/questions/11471158/stringilength-giving-memory-error)
  * [exception MemoryError - Built-in Exceptions — Python 3.9.7 documentation](https://docs.python.org/3/library/exceptions.html?highlight=memory%20error#MemoryError)
  ```python
  import sys


  class Solution:
      def slicing(self, x : int) -> list:
          inputs = [10**9] * 10**6
          results = []

          for i in range(len(inputs) - x):
              results.append(inputs[i : i + x])   # memory error

          # print(results)
          print(len(results))
          print(sys.getsizeof(results[0]))
          print(sys.getsizeof(results))


  if __name__ == '__main__':
      my_solution = Solution()

      for i in range(5):
          my_solution.slicing(i)  
  ```
* How to fix ModuleNotFoundError: No module named 'a.b' when from a.b.c import d ?
  * Check if there is __init.py__ under /a
* How to fix NameError: name 'var' is not defined when define var in try statement and use it in catch / finally statement ?
  * Declare the var before try statement with var = None
  * python - Using a variable in a try,catch,finally statement without declaring it outside - Stack Overflow
    * https://stackoverflow.com/questions/17195569/using-a-variable-in-a-try-catch-finally-statement-without-declaring-it-outside
  * python - How to make a variable inside a try/except block public? - Stack Overflow
    * https://stackoverflow.com/questions/25666853/how-to-make-a-variable-inside-a-try-except-block-public
* How to fix sqlite3.OperationalError: database is locked ?
  * SQLite is lightweight database and need to use, e.g. PostgrsSQL, for large number of connections. If the cache db file is in locked even if with one job, use the below cmds to recover it.
  * sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.7.4 documentation
    * https://docs.python.org/3.7/library/sqlite3.html
    * SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.
  * SQLite Frequently Asked Questions
    * https://www.sqlite.org/faq.html
  * Python SQLite: database is locked - Stack Overflow
    * https://stackoverflow.com/questions/2740806/python-sqlite-database-is-locked
    * $ fuser cache.db
    * $ mv cache.db-journal _cache.db-journal
    * $ sqlite3 cache.db "pragma integrity_check;"
      * ok
    * $ sqlite3 cache.db ".backup cache.db.bak"
    * $ rm cache.db
    * $ sqlite3 cache.db.bak ".schema"
* How to fix TypeError: slice indices must be integers or None or have an __index__ method ?
  * b = ['a', 'aa', 'aaa', 'b', 'c']
  * d = [c for c in b if c.startswith( 'a', 'b' )]
  * It's due to lack of parenthese. Change to 
  * d = [c for c in b if c.startswith( ('a', 'b') )]
* How to fix TypeError: 'int' object does not support indexing ?
  * [python - TypeError: 'int' object does not support indexing - Stack Overflow](https://stackoverflow.com/questions/18345825/typeerror-int-object-does-not-support-indexing)
  * You should pass query parameters to execute() as a tuple (an iterable, strictly speaking), (some_id,) instead of some_id
