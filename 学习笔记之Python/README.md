# 学习笔记之Python

* [python/学习笔记之Python at main · haoran119/python](https://github.com/haoran119/python/tree/main/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython)
* [Welcome to Python.org](https://www.python.org/)
  * [3.9.5 Documentation (python.org)](https://docs.python.org/3/)
  * [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
  * [Programming FAQ — Python 3.9.6 documentation](https://docs.python.org/3/faq/programming.html)
  * [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
* [Python（计算机编程语言）_百度百科 (baidu.com)](https://baike.baidu.com/item/Python/407313?fr=aladdin#reference-[12]-21087-wrap)
  * 自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和Web编程。
  * Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
  * Python允许像数学的常用写法那样连着写两个比较运行符。比如a < b < c与a < b and b < c等价。C++的结果与Python不一样，首先它会先计算a < b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。
  * Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。

## NOTES

* [python/面试总结之Python at main · haoran119/python](https://github.com/haoran119/python/tree/main/%E9%9D%A2%E8%AF%95%E6%80%BB%E7%BB%93%E4%B9%8BPython)
* [学习笔记之盘一盘 Python 系列 1 & 2 - 入门篇 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11289321.html)
* [学习笔记之Python开发环境 IDE ( Anaconda / PyCharm ) - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/8915306.html)
* [学习笔记之Python 3 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/10825575.html)
* [学习笔记之Python爬虫 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/10470560.html)
* [学习笔记之Django - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11556233.html)
* [学习笔记之pytest - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/13769672.html)
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
  * items()
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dict.items
    * Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
  * 4.7.5. Lambda Expressions
    * https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions
    * Small anonymous functions can be created with the lambda keyword.
  * https://github.com/haoran119/python/blob/d8d0841e46f42aa474a4108a441007607955bc8f/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/4.7.5.%20Lambda%20Expressions.py
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

* [Python3 教程 | 菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)
* [Python 入门指南 — Python tutorial 3.6.0 documentation](http://www.pythondoc.com/pythontutorial3/index.html)
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

* [Python 为什么不支持 i++ 自增语法，不提供 ++ 操作符？ (qq.com)](https://mp.weixin.qq.com/s/gs3aZucOxXkeMGmP0H9fuA)
* Python 字符串拼接总结
  * https://segmentfault.com/a/1190000015475309
  * [2.4.3. Formatted string literals - 2. Lexical analysis — Python 3.9.6 documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    * A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
    * See also [PEP 498](https://www.python.org/dev/peps/pep-0498/) for the proposal that added formatted string literals, and [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format), which uses a related format string mechanism.
  * [Efficient String Concatenation in Python](https://waymoot.org/home/python_string/)
  * 注意Python中list是可变对象，而str是不可变对象。fun1比fun2更高效。
```sh
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
* [Python字符串用法大全](https://mp.weixin.qq.com/s/yMVrjmOYp7opYB0Nvx47Dw)
* [Python字符串处理的8招秘籍](https://mp.weixin.qq.com/s/x_0Ahm-q8FAxAvJoUWnsEQ)
* [10 个 Python 字符串处理技巧](https://mp.weixin.qq.com/s/iaT30IyPT8NSQ42d3oVpVA)
  1. 空格剥离
  2. 字符串拆分
  3. 将列表元素合成字符串
  4. 字符串反转
  5. 大小写转换
  6. 检查是否有字符串成员
  7. 子字符串替换
  8. 组合多个列表的输出
  9. 同字母异序词检查
  10. 回文检查
* [如何优雅的操作Python字典 - 程序员大咖](https://mp.weixin.qq.com/s/mWjzDm9XNNnFiJGYhzpivA)
  * https://www.linuxzen.com/python-you-ya-de-cao-zuo-zi-dian.html
* [干货|理解Python列表和元组](https://mp.weixin.qq.com/s/U-ctO-brjwxpm0LbLTB-dw)
* [Python 列表排序 sort 与 sorted 详解](https://mp.weixin.qq.com/s/R16hyfikRCOEUGhDGOBVcQ)
  * https://maida6244.xyz/
* [图解 Python 函数](https://mp.weixin.qq.com/s/9AxWUaYaK15N4hsQMjlBjA)
* [Python 69个内置函数分8类总结](https://mp.weixin.qq.com/s/2ZFZ8olllPnrQ4wtCPPkMA)
  * https://docs.python.org/3/library/functions.html
  * 1、内置函数
  * 2、类型相关
  * 3、数理统计相关
  * 4、进制转换
  * 5、面向对象相关
  * 6、迭代器相关
  * 7、map函数
  * 8、排序相关
  * 9 其他
* [len(x) 击败 x.len()，从内置函数看 Python 的设计思想 (qq.com)](https://mp.weixin.qq.com/s/IRMplJCoWtH98uNtAeFKxg)
* [Python高阶函数使用总结](https://mp.weixin.qq.com/s/xtO8NDq3lVacsT5Z7eQXmw)
  * 本文结合各种实际的例子详细讲解了Python5个内建高阶函数的使用，能够帮助理解Python的数据结构和提高数据处理的效率，这5个函数分别是：
    * map
    * reduce
    * filter
    * sorted/sort
    * zip
* [Python | 掌握 Lambda 函数，四不要](https://mp.weixin.qq.com/s/tWibBZGcX4PtEKo0a1bvzQ)
  * https://github.com/xitu/gold-miner/blob/master/article/2020/master-python-lambda-functions-with-these-4-donts.md
    1. 不要返回任何值
    2. 不要忘记更好的选择
    3. 不要将它赋值给变量
    4. 不要忘记列表推导式
* [条件语句的七种写法](https://mp.weixin.qq.com/s?__biz=Mzg4NDQwNTI0OQ==&mid=2247522923&idx=4&sn=04c0072a03765c7741f459cd0807d9b7&source=41#wechat_redirect)

## ADVANCE

* [5张图理解Python中的浅拷贝与深拷贝](https://mp.weixin.qq.com/s/em4OBWLdTqC7jdvyCs7Jhg)
* [图解 Python 中深浅拷贝](https://mp.weixin.qq.com/s/TtGFFDTKdPwCYj7gmIdp_Q)
  * https://blog.csdn.net/mall_lucy/article/details/104531218
  * 赋值运算
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
* [聊一聊 Python 中的“垃圾”回收](https://mp.weixin.qq.com/s/P3G5InQxq_kw4QUlhsXRCg)
  * https://www.heroyf.club/2019/10/24/python_gc/
* [Python 中 -m 的典型用法、原理解析与发展演变](https://mp.weixin.qq.com/s/tD3eSb2WdOPN_dKAQ9d6Ag)
* [Python中的*args和**kwargs是什么？该如何使用？](https://mp.weixin.qq.com/s/s7PFVE_wcAMZaRUds2MJDQ) 
  * https://medium.com/better-programming/what-are-args-and-kwargs-in-python-6aaf9e3cad73
* [为什么 Python 没有 main 函数？](https://mp.weixin.qq.com/s/Nr1nD6qKKRd-C55PCV-sGw)
  * https://towardsdatascience.com/why-doesnt-python-have-a-main-function-3afe6a8d093
* [IPython 中常用的魔法命令](https://mp.weixin.qq.com/s/5ZyfyR9r9zBod6ZP7scewA)

### 迭代器与生成器

* [Python 迭代器与生成器](http://www.langzi.fun/%E8%BF%AD%E4%BB%A3%E5%99%A8%E4%B8%8E%E7%94%9F%E6%88%90%E5%99%A8.html)
* [Python 迭代器和 C++ 迭代器最大的不同](https://mp.weixin.qq.com/s/2qoNY-UNLf8vW7CGj8BQ2A)
* [带你彻底搞懂Python生成器](https://mp.weixin.qq.com/s/2HAPquA-VZNNRHYRN8E2bg)

### 模块

* [深入探讨Python的import机制：实现远程导入模块 | CSDN博文精选](https://mp.weixin.qq.com/s/Sx_WyKUpoZrnFtV9epAfpg)
* [Python Logging 模块完全解读](https://mp.weixin.qq.com/s/iZEjyEoxVUQ5cner2VY1kg)
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
  * defaultdict：字典的子类，提供了一个工厂函数，为字典查询提供了默认值。
  * OrderedDict：字典的子类，保留了他们被添加的顺序。
  * namedtuple：创建命名元组子类的工厂函数。
  * deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)。
  * ChainMap：类似字典的容器类，将多个映射集合到一个视图里面。
* [你常常看到的 \_\_init\_\_.py 到底是个啥？](https://mp.weixin.qq.com/s/5RW_wd1J9RsyX99Zbm_G0g)
  * 综上，\_\_init\_\_.py 会在 import 的时候被执行，而空的 \_\_init\_\_.py 在 Python 新版本中已经不需要你额外去定义了，因为就算你不定义 init， Python 也知道你导入的包路径，但是如果你想要做一些初始化操作，或者像我们刚刚说的预先导入相关的模块，那么定义 \_\_init\_\_.py 还是很有必要的哟。
* [Python编程中的if \_\_name\_\_ == 'main' 的作用和原理](https://mp.weixin.qq.com/s/SXTo0h2ExujAQdWnLWggdg)
  * https://zhuanlan.zhihu.com/p/34112508
  * \_\_name\_\_ 是当前模块名，当模块被直接运行时模块名为 \_\_main\_\_ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
* [heapq — Heap queue algorithm — Python 3.9.6 documentation](https://docs.python.org/3/library/heapq.html?highlight=heapq#module-heapq)
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

### IO / FILE

* [Python 数据形态及IO操作](https://mp.weixin.qq.com/s/97v0k_hWdgJeppx1oF7Vxw)
* [Python处理CSV、JSON和XML数据的简便方法](https://mp.weixin.qq.com/s/1PyeBLIJNzswO3zd-mHiTQ)
  * https://towardsdatascience.com/the-easy-way-to-work-with-csv-json-and-xml-in-python-5056f9325ca9

### 错误和异常

* [学习笔记之Python Debug ( pdb ) - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/10437091.html)
* [一文教你读懂 Python 中的异常信息](https://mp.weixin.qq.com/s/6cAuUpZgj5kZ-1KM7-ZV_Q)
  * https://realpython.com/python-traceback/
* [Python 常见的17个错误分析](https://mp.weixin.qq.com/s/_OZH8o9rHaha0TmCboCCJA)
  * https://www.oschina.net/question/89964_62779
  * https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/

### 面向对象

* [Python 面向对象编程](https://mp.weixin.qq.com/s/IFRloykz9Nnb3N94CQpieg)
  * http://www.langzi.fun/Python%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B.html
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
* [What is MRO in Python?](https://www.educative.io/edpresso/what-is-mro-in-python)
  * Method Resolution Order
  * MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
  * In Python, the MRO is from bottom to top and left to right. This means that, first, the method is searched in the class of the object. If it’s not found, it is searched in the immediate super class. In the case of multiple super classes, it is searched left to right, in the order by which was declared by the developer.
* [没看完这11 条，别说你精通 Python 装饰器](https://mp.weixin.qq.com/s/5hmauIKOTS1vqHbhE12KkA)
* [5分钟全面掌握 Python 装饰器](https://mp.weixin.qq.com/s/Dx887iB-jn-BMdj3F1vHDQ)
* [读懂 Python 装饰器](https://mp.weixin.qq.com/s/pezg8naU4Afkf8DTm_m13w)
* [Python中的元编程：一个关于修饰器和元类的简单教程](https://mp.weixin.qq.com/s/bV7g9ugGmFjojGDMIc_kpQ)
  * https://medium.com/better-programming/meta-programming-in-python-7fb94c8c7152
* [如何将 Python 的一个类方法变为多个方法？](https://mp.weixin.qq.com/s/WPbtNQoMbMWVmD2IGOw8Rg)
* [写 Python 代码不可不知的函数式编程技术](https://mp.weixin.qq.com/s/cTUmjl8-laztpUSfSCW1hQ)
  * https://medium.com/better-programming/introduction-to-functional-programming-in-python-3d26cd9cbfd7

### 多线程

* [理解python多线程和多进程](https://mp.weixin.qq.com/s/pjoSXrpjvxvOHDmWAhYfFA)
* [深入理解python多线程和多进程](https://mp.weixin.qq.com/s/w0dZrtv8ogdtxO8FT2LrEg)
* [入门 | 三行Python代码，让数据预处理速度提高2到6倍](https://mp.weixin.qq.com/s/DgKuNIa_m-CsXWgHIz_3rQ)
  * https://towardsdatascience.com/heres-how-you-can-get-a-2-6x-speed-up-on-your-data-pre-processing-with-python-847887e63be5
* [Python 线程为什么要搞个 setDaemon ？](https://mp.weixin.qq.com/s/tRaQftWQNzE2a_ZKDLGE4w)

### 编码

* [一文透彻掌握 Python 编码问题](https://mp.weixin.qq.com/s/CFDH58dwU3ilMn1axJVccg)
* [一图看懂 Python 2 / Python 3 编码 | CSDN 博文精选](https://mp.weixin.qq.com/s/V9fM7G5c0JirQezoZAJVaw)

## PYTHONIC STYLE

### STYLE GUIDE

* [学习笔记之Python最简编码规范 - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/10387079.html)
* [代码整洁之道-编写 Pythonic 代码](https://mp.weixin.qq.com/s/uYzO63krMt-_ztmf4SmI2w)
* [写出漂亮 Python 代码的 20条准则](https://mp.weixin.qq.com/s/2I8clKTGDPbmR1fTOLWaZQ)
  * https://medium.com/better-programming/how-to-make-python-programming-more-elegant-and-decent-4b5962695aa9
* [Python 编码风格指南](https://mp.weixin.qq.com/s/JnrLSfQfH4CGAZSK_rnumg)
* [Python 简洁编码之道](https://mp.weixin.qq.com/s/UeOkqf37HQH-RQZbpJAiDQ)
* [18式优雅你的Python](https://mp.weixin.qq.com/s/iiG3Jarc_bIzcvz1-lmmhg)
* [改善Python程序的91个建议](https://zhuanlan.zhihu.com/p/32817459)
* [符合语言习惯的 Python 优雅编程技巧](https://mp.weixin.qq.com/s/rE5OEFwwFxJNb_Omwmqvzw)
  * http://lovesoo.org/pythonic-python-programming.html?amhgxy=ov4fk
* [优雅编写Python3的62个小贴士](https://mp.weixin.qq.com/s/xkxpZo_8HixRlXU8PtMK7w)

### TIPS

* [@Python 程序员，如何最大化提升编码效率？](https://mp.weixin.qq.com/s/_-vCTkryiP2gq_IdX6pL8w)
  * https://towardsdatascience.com/five-python-tricks-you-need-to-learn-today-9dbe03c790ab
* [这些Python代码技巧，你肯定还不知道](https://mp.weixin.qq.com/s/UWd4hpeZztHmpHmmlftvlQ)
  * https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/
* [wtfPython—Python中一些奇妙的代码](https://mp.weixin.qq.com/s/B--tL_s8-eWF-x9ilCbvdQ)
  * http://yaoyaoblog.xyz/2017/09/04/wtfPython%E2%80%94Python%E4%B8%AD%E4%B8%80%E4%BA%9B%E5%A5%87%E5%A6%99%E7%9A%84%E4%BB%A3%E7%A0%81/
* [15个Pythonic的代码示例](https://mp.weixin.qq.com/s/vZcJ__SCcdLk2JopMx_yqA)
* [7个案例15分钟让你了解Python套路](https://mp.weixin.qq.com/s/8GQ8gP4S4yA7FmlLhbuiBA)
  * https://www.jianshu.com/p/36ae91c38279
* [Python带我飞：50个有趣而又鲜为人知的Python特性](https://mp.weixin.qq.com/s/ULy82R1DYdbx0MH4xD22IA)
  * https://github.com/leisurelicht/wtfpython-cn
* [Python中实用却不常见的小技巧](https://hackernoon.com/python-tricks-101-2836251922e0)
  * https://github.com/brennerm/PyTricks
* [Python 开发中有哪些高级技巧？](https://mp.weixin.qq.com/s/6ierUk69wmooZcLKL3-XZw)
* [18 个 Python 高效编程技巧](https://mp.weixin.qq.com/s/2Bxc5u0X_NQtLuXbVvPfzQ)
* [10招玩转Python](https://mp.weixin.qq.com/s/WxYMY_b-5UPMD4KWPWIH9A)
* [学Python，从列表推导到zip()函数，这五种技巧应知应会](https://mp.weixin.qq.com/s/GDC3GeTPXspInK_1DPyuVA)
  * https://towardsdatascience.com/python-tricks-101-what-every-new-programmer-should-know-c512a9787022
* [10 个不为人知的Python冷知识](https://mp.weixin.qq.com/s/NysJHFlw57Br_k1cpYTmMA)
* [Python的高级特征你知多少](https://mp.weixin.qq.com/s/VBiQ2X7Y93h51GkIosC_Vw)
* [26个Python实用技巧](https://mp.weixin.qq.com/s/ttuB63_N5SQdOhIwLFGYgg)
  * https://mp.weixin.qq.com/s/lPZTVURxfdRVYqIMUfnsBw
  * https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/
* [Python 有哪些不一样的技巧](https://mp.weixin.qq.com/s/w0OHrozLrD_n6v47Cit6BA)
* [即学即用的30段Python实用代码](https://mp.weixin.qq.com/s/KHj_j9PShDU7MFg6m15mBQ)
  * https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
* [每30秒学会一个Python小技巧](https://mp.weixin.qq.com/s/woVJXAI_8Gm7rIlaa6j7RQ)
  * https://github.com/30-seconds/30-seconds-of-python
* [Python的 5 种高级用法](https://mp.weixin.qq.com/s/_9LWP5K7mZckjghCRn6FPQ)
  * https://towardsdatascience.com/5-advanced-features-of-python-and-how-to-use-them-73bffa373c84
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
* [Python循环这样写，高效节省内存](https://mp.weixin.qq.com/s/rQtaQAjkDGnK8fmirE0O8w)
* [8个Python高效数据分析的技巧](https://mp.weixin.qq.com/s/l178i--vWqUaCdO99JG2pw)
  * https://towardsdatascience.com/python-for-data-science-8-concepts-you-may-have-forgotten-i-did-825966908393
* [7 个 Python 特殊技巧，有效提升数分效率！](https://mp.weixin.qq.com/s/nn-3GGhQwzgGf-qGS7TINg)
* [使用类型注解让 Python 代码更易读](https://mp.weixin.qq.com/s/SG7sybPIVM65JSP6BZT_4Q)
  * https://github.com/Germey/TypingTest
* [分享8点有用的Python编程建议](https://mp.weixin.qq.com/s/LtOUArQWA3BIdqFBjMkYcA)
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
* [给 Python 初学者的四条忠告](https://mp.weixin.qq.com/s/hAMzBoU1uscUiBywiyuJ4A)
  * https://blog.csdn.net/xufive/article/details/102709538
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
* [Python 中更优雅的日志记录方案](https://mp.weixin.qq.com/s/XOcyUbgIrCXEAYH2p3Zo5Q)
  * https://loguru.readthedocs.io/en/stable/index.html
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
* [收藏 | 34 个优秀好用的Python开源框架](https://mp.weixin.qq.com/s/Aa7gsmxE1-kBSsToaR4ltA)
  * https://github.com/Mybridge/amazing-python-2019
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
* [Python打包成exe](https://mp.weixin.qq.com/s/W3-Bty8jENedFWad06KnCA)
* [详细指南 | 如何在Github发布Python开源包](https://mp.weixin.qq.com/s/FTcGjx6YLmuldAKp03dhAQ)
  * https://www.freecodecamp.org/news/from-a-python-project-to-an-open-source-package-an-a-to-z-guide-c34cb7139a22/
* [Python 中自动导入缺失的库](https://mp.weixin.qq.com/s/NYbovYS6z6j40ifnEfEEKA)
* [用 Python 写一个安卓 APP](https://mp.weixin.qq.com/s/NTxNPZRci_b7zhZgU2MrGw)
  * https://blog.51cto.com/youerning/1733534
* [轻轻松松用Python写APP](https://mp.weixin.qq.com/s/CiJxNHQ8CjDO_8V3vK0bEw)
  * https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace
* [用Python把Linux命令写一遍](https://mp.weixin.qq.com/s/71fLATw5LStdknIk2PqHRQ)
* [“堆”的 Python 实现与应用总结](https://mp.weixin.qq.com/s/cvUGuDSp_fb-kjHRe_zBPA)
  * https://zhuanlan.zhihu.com/p/85518062
* [如何用 Python 快速开发一个区块链数据结构？](https://mp.weixin.qq.com/s/m7hZY93ponge6dy2fvTzAg)
* [一文读懂Python复杂网络分析库networkx | CSDN博文精选](https://mp.weixin.qq.com/s/WYM7k9gddAndlLBuQWTbSA)
* [实战：基于技术分析的Python算法交易](https://mp.weixin.qq.com/s/J-ZwLl_CzvaRHZjKvTA3iw)
* [开发必学的验证码，教你从零写一个验证码](https://mp.weixin.qq.com/s/XGhpxP4rTg_JeRkYZX2EzA)
  * https://github.com/MiracleYoung/You-are-Pythonista/tree/master/PythonExercise/App/captcha_project
* [用 Python 生成炫酷二维码及解析](https://mp.weixin.qq.com/s/V2g6DICFkVDOg-kI3QmnrA)
  * 我们通过 Python 生成以及识别二维码需要用到的库为：qrcode、myqr、zxing，安装通过 pip install qrcode/myqr/zxing 即可。
* [生成自定义二维码，5行Python代码就搞定](https://mp.weixin.qq.com/s/VyhoFRVu9KXOuMezouY6Og)
  * [https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325
* [万字干货 | Python后台开发的高并发场景优化解决方案](https://mp.weixin.qq.com/s/BHiM-mv7HXSmIY2KRf480g)
* [仅仅50行Python，就可以在手机端看电脑桌面！](https://mp.weixin.qq.com/s/k02vPOwgdFgeZ9K4_dmJvw)
* [用 Python 偷偷抓取了她的行踪](https://mp.weixin.qq.com/s/H6mxILglgko01GLqe7VRyQ)
  * https://github.com/xingag/spider_python/tree/master/%E8%8E%B7%E5%8F%96%E5%A5%B3%E5%8F%8B%E7%9A%84%E4%BD%8D%E7%BD%AE
* [谁偷偷删了你的微信？别慌！Python 帮你都揪出来了](https://mp.weixin.qq.com/s/iNkS550-8-Oj55x9Ye7Ykg)
* [使用Python假装装黑客，批量破解朋友的网站密码](https://mp.weixin.qq.com/s/ZqSvVZiZC7ehcMvRAZ4unw)
* [用Python可以算出了你的身份证号码](https://mp.weixin.qq.com/s/AuQu7rlDU8pkKv3F0SZffQ)
  * https://github.com/zpw1995/aotodata/blob/master/interest/ID_card/ID_card.py
* [用 Python 自动监测 GitHub 项目更新](https://mp.weixin.qq.com/s/_nkx_cCKxz0VrfgGvWDcrA)
* [不到 50 行 Python 代码，做个刮刮卡](https://mp.weixin.qq.com/s/4WGYs4GMjObQZlObM2KkNQ)
* [用Python做个海量小姐姐素描图](https://mp.weixin.qq.com/s/JIPdPBCurXMTcaPprWuZvw)
* [用 Python 批量下载百度图片](https://mp.weixin.qq.com/s/q-obSiAt1Rs28itlKU2FiA)
* [用 Python 处理 B 站下载视频](https://mp.weixin.qq.com/s/dCTIUNeDQ_HeZqWQr0hesA)
* [如何用 Python 快速抓取 Google 搜索？](https://mp.weixin.qq.com/s/-GUgWH06Wy7pCzNbMjinXg)
  * https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal
  * https://github.com/getlinksc/scrape_google
* [我用Python找到了隔壁蹭网妹子的QQ号](https://mp.weixin.qq.com/s/QKjc1nZo18PGq7j0K6sTIg)
* [用 Python 编写一个天气查询应用](https://mp.weixin.qq.com/s/iciMycq-HpwZj-LSE60NQQ)
* [大象装进冰箱要几步？Python 来解答](https://mp.weixin.qq.com/s/S5OWsuY1hT1qATadZ0v_kA)
* [用 Python 制作家用防盗工具](https://mp.weixin.qq.com/s/6RE1fwKF8gndI3Bnhb8UgA)
* [用 Python 制作“除夕夜倒计时”海报](https://mp.weixin.qq.com/s/MIhViQrYOca8QlQ7QEfoZw)
  * https://github.com/wwtm/gitpython_examples
* [Python GUI开发，效率提升10倍的方法！](https://mp.weixin.qq.com/s/tRKEbBwjDtGWR4VTAfEqPg)
  * https://github.com/PySimpleGUI/PySimpleGUI
* [用Python计算颜值数](https://mp.weixin.qq.com/s/d4r3oMReYCUBjUwCbAzE5w)
  * 现在很多拍照软件都有颜值测试及年龄识别功能，经过研究，发现 Python 也能实现，今天主要用 PyQt4 做个可视化工具，然后调用百度人脸识别api，识别出人脸的性别、年龄及颜值
* [用 Python 发一封邮件](https://mp.weixin.qq.com/s/wXAfYIdGxukKSstiFxLi4g)
* [用Python唱一首程序员版“惊雷”](https://mp.weixin.qq.com/s/CGFkdviDXu3-YEQTNywY7A)
* [如何用 Python 制作地球仪？](https://mp.weixin.qq.com/s/I6B5CDKRf8QDftAcIa_o_w)
  * 写在前面的话：在之前的文章 Python 图表利器 pyecharts 中有介绍了 pyecharts 的安装及使用,详细教程请到 官网 学习
  * pyecharts 功能很强大，只需要导入相应的模块就配置相应的选项即可生成对应的超文本文件，使用浏览器访问即可！具体实例请见下文
* [90行代码让微信开屏地球转起来](https://mp.weixin.qq.com/s/azBohOz_5mybLV32MSlaXQ)

### AI

* [如何用 Python 构建机器学习模型？ (qq.com)](https://mp.weixin.qq.com/s/c-Sl7n_ceawz6AHm5Mtw0w)
  * 该 Notebook 包含了用于创建主要机器学习算法所需的代码模板。在 scikit-learn 中，我们已经准备好了几个算法。只需调整参数，给它们输入数据，进行训练，生成模型，最后进行预测。
  * https://github.com/haoran119/python/blob/1703d4e453ed815710a777edd80089196b3b5968/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/%E5%A6%82%E4%BD%95%E7%94%A8%20Python%20%E6%9E%84%E5%BB%BA%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E6%A8%A1%E5%9E%8B.py

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
* [让二次元妹子动起来，用一张图生成动态虚拟主播](https://mp.weixin.qq.com/s/TgZ3KidFlioFvCpgSsdO9A)
  * https://pkhungurn.github.io/talking-head-anime/
* [用 Python 图像识别打造一个小狗分类器](https://mp.weixin.qq.com/s/il3Ou5wCMq0h2chP7Dnn1Q)
* [3行代码，搞定AI自动抠图](https://mp.weixin.qq.com/s/naSRo2heiACI0hTOSUZu9g)
* [Python中的图像增强技术](https://mp.weixin.qq.com/s/vqyaSK-Uis0vZrxu-KDMyw)
  * https://towardsdatascience.com/data-augmentation-techniques-in-python-f216ef5eed69
* [AI图像智能修复老照片](https://mp.weixin.qq.com/s/BlrViDMRKm8Hdj9nvkzxvQ)
  * 所使用的的python库有cv2库，目的是用来读取图片，处理图片像素值和保存图片等；numpy用来对读取过来的像素值矩阵进行运算。
* [用 Python 制作了一个朋友圈机器人](https://mp.weixin.qq.com/s/3OHpnKS9BrkoYIjF20ojvg)
* [19 行代码能搭建一个微信机器人](https://mp.weixin.qq.com/s/HP9zfgpHywaLi3NUPyFT5A)
  * wxpy 是一个封装好的微信个人号接口，在 itchat 的基础上，通过大量接口优化提升了模块的易用性。
* [当语音助手遇到机器人](https://mp.weixin.qq.com/s/I_hoLoLVPc0kfTCyMdSTag)
  * 图灵机器人（http://www.tuling123.com/）和 Siri 语音助手完成一次有趣的对话。
  * 使用到的技术有：
    * 图灵机器人（http://www.tuling123.com/）的 API 接口
    * 百度 AI开放平台的语音合成接口、OCR文字识别接口
    * ImageGrab 截图
    * 文件传输

### DATA SCIENCE

* [《Python中神奇的第三方库：Faker》](https://mp.weixin.qq.com/s/1tk4xeWvwZ5oNhzaywgDgA)
  * [Python中第三方库-Faker](https://blog.csdn.net/mall_lucy/article/details/108655317)
  * 开发项目的时，为了测试常需要造假数据，经常要尽量的模拟真实环境，通常要费大量手工而且造出来的数据，而且通常手工造出来的看起来也很别扭，费时又费事，有没有更好的办法？有，这里给大家介绍一个“专业造数“库Faker，满足你对模拟数据的所有需求。
* [【实战】使用 Python 分析 14 亿条数据](https://mp.weixin.qq.com/s/SUI3Gs5pUCVBrlsCqpdW0g)
  * https://juejin.im/post/5aceae206fb9a028d2084fea
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
* [用Python数据分析了北京积分落户名单](https://mp.weixin.qq.com/s/0jBZY8-LryScevzWv7z0-g)
  * https://github.com/zpw1995/aotodata/tree/master/bj_luohu
* [如何用 Python 画出新型冠状病毒疫情地图？](https://mp.weixin.qq.com/s/DjBIu4851l0a_vN_aEjo7Q)
* [Python 硬核分析我国 14 亿人口，发现三大危机！](https://mp.weixin.qq.com/s/IFKYGMbxWbNTylBnE7zYBg)
  * https://github.com/pig6/china_population
* [怎么用 Python 画出好看的词云图？](https://mp.weixin.qq.com/s/Tuzfh9aKTN7_Fxt8YJ4q-w)
* [Python 竟能绘制出如此酷炫的三维图](https://mp.weixin.qq.com/s/tBl3iI-dfJcV4om0aJBnbA)
  * https://jalammar.github.io/visual-numpy/
* [用 Python 分析各国足球俱乐部排名](https://mp.weixin.qq.com/s/wakUY9phwcv1WPLo99og4A)
* [用 Python 对淘宝用户行为进行分析](https://mp.weixin.qq.com/s/CWTAhpu6VLsia1iCoLiuAA)
  * 本数据报告以淘宝app平台为数据集，通过行业的指标对淘宝用户行为进行分析，从而探索淘宝用户的行为模式，具体指标包括：日PV和日UV分析，付费率分析，复购行为分析，漏斗流失分析和用户价值RFM分析。
* [Python 制作动态图表，看全球疫情变化趋势](https://mp.weixin.qq.com/s/h3XaV7QfrcDMaUji1Y19Gw)
* [Python 招聘岗位数据可视化](https://mp.weixin.qq.com/s/lDiyXf9ORkDeD6akeqKEVA)
* [用Python分析了《青春有你2》](https://mp.weixin.qq.com/s/FRpE3EHP0GLYls1EUL8vAw)
* [用 Python 做了一个全球疫情数据大屏](https://mp.weixin.qq.com/s/IbdEnZmG6UjCZvNVGWJcxg)
  * 爬虫模块负责从腾讯新闻获取数据，之后存入 Redis。Flask 是一个 Web 框架，负责 URL 和后台函数的映射，以及数据的传输。换言之，也就是从 Redis 中获取到原始数据，然后整理成相应的格式之后传递给前端页面，前端页面在拿到数据之后，调用百度的 ECharts 来实现图表的展示即可。
* [用 Python 做一个动态可视化的交互大屏](https://mp.weixin.qq.com/s/H6K1K-LE7IM6-6Vp2v8U4Q)
* [1行代码实现Python数据分析：图表美观清晰，自带对比功能](https://mp.weixin.qq.com/s/0T0e0lwx6bUOhGHr2J1Clg)
  * https://github.com/fbdesignpro/sweetviz

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
* [500行代码，教你用python写个微信飞机大战](https://mp.weixin.qq.com/s/IHAn_1cLCc-QQ3FWQIeaNQ)
  * https://github.com/MiracleYoung/You-are-Pythonista/tree/master/PythonExercise/App/plan_game
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

### IO / DATABASE / FILE

* [利用 tornado 实现表格文件预览](https://mp.weixin.qq.com/s/NVAzXKP801mfAfNRMvCjBw)
  * https://github.com/percent4/csv_file_review
* [Python 处理分析 128 张 Excel 表格竟不到3秒？| 附数据集](https://mp.weixin.qq.com/s/ZhWomp6LDgHHjf9Tr1dzvg)
  * https://github.com/seizeeveryday/DA-cases/tree/master/Python%2Bexcel
* [将Python字符串生成PDF](https://mp.weixin.qq.com/s/5R6t_oiOOV7qG4YkdLcpvA)
* [pdfkit | 自动化利器，生成PDF就靠它了](https://mp.weixin.qq.com/s/9OhS6hjpn6e0XAaATQOeXg)
* [用 Python 操作 Word 文档](https://mp.weixin.qq.com/s/awN9gLqVn_s-STRzhioPXQ)
* [用 Python 实现文件自动归类](https://mp.weixin.qq.com/s/Ech_OeoDdYkd1ZmNjRIm_w)
* [用Python一键批量将任意结构的CSV文件导入MySQL数据库。](https://mp.weixin.qq.com/s/ouuk4o739tlzF6b5cNjUwQ)
* [5个案例让Python输出漂亮的表格！](https://mp.weixin.qq.com/s/8uxc2t53N_j_mRPYbiG0sA)
  * https://linuxops.org/blog/python/prettytable.html
  * prettytable可以打印出美观的表格，并且对中文支持相当好
* [Python与MySQL数据库的交互实战](https://mp.weixin.qq.com/s/9D2bi_1W6fjMxI3jaH2teA)
  * https://blog.csdn.net/weixin_41261833/article/details/103832017

## FAQ

* What's package and module ?
  * Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
  * 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。目录只有包含一个叫做 \_\_init\_\_.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
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
* 如何多行字符串拼接?
  * https://github.com/haoran119/python/blob/e98be0d3dedb64f4440fe620ca47edbcde0e75a1/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/%E5%A6%82%E4%BD%95%E5%A4%9A%E8%A1%8C%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%8B%BC%E6%8E%A5.py
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
  * https://github.com/haoran119/python/blob/081816091c1372991cd1542028710399aa67de99/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20change%20values%20in%20a%20list%20with%20for%20loop.py
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
* datetime operation
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
  * https://github.com/haoran119/python/blob/cd05dd3d79480c527d38822b5bccf4879a471563/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20print%20lists.py
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
* How to iterate directory for files ?
  * os — Miscellaneous operating system interfaces — Python 3.7.4 documentation
    * https://docs.python.org/3/library/os.html?highlight=os%20walk#os.walk
    * Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
  * Python3 OS 文件/目录方法 | 菜鸟教程
    * http://www.runoob.com/python3/python3-os-file-methods.html
  * Python list directory, subdirectory, and files - Stack Overflow
    * https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
  * https://github.com/haoran119/python/blob/b754b5ae1339443d9c5fc9d54cf7b9de1349cc12/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20iterate%20directory%20for%20files.py 
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
  * https://github.com/haoran119/python/blob/c47e7b70db20a0eb7aff785806555f886c02f2cc/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20input%20and%20output%20file.py
* How to use try ... except ... finally statement for exception ?
  * 8.4. The try statement - 8. Compound statements — Python 3.7.4 documentation
    * https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
  * Manually raising (throwing) an exception in Python - Stack Overflow
    * https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python　　
* How to define custom exception ?
  * How to Define Custom Exceptions in Python? (With Examples)
    * https://www.programiz.com/python-programming/user-defined-exception
* How to use Regular Expression 正则表达式 ？
  * Python3 正则表达式 | 菜鸟教程
    * http://www.runoob.com/python3/python3-reg-expressions.html
  * re — Regular expression operations — Python 3.7.4 documentation
    * https://docs.python.org/3.7/library/re.html#module-re
  * Regular Expression HOWTO — Python 3.7.4 documentation
    * https://docs.python.org/3/howto/regex.html
  * regex - Get all unnamed groups in a Python match object - Stack Overflow
    * https://stackoverflow.com/questions/30293064/get-all-unnamed-groups-in-a-python-match-object
  * regex - Extracting 2 strings from regular expression Python - Stack Overflow
    * https://stackoverflow.com/questions/23658156/extracting-2-strings-from-regular-expression-python
  * regex - Python extract pattern matches - Stack Overflow
    * https://stackoverflow.com/questions/15340582/python-extract-pattern-matches
  * Python 正则表达式 re 模块简明笔记
    * https://mp.weixin.qq.com/s/8M_xiHMNB1a93ZunpxMsLg
    * https://funhacks.net/2016/12/27/regular_expression/
  * Online regex tester and debugger: PHP, PCRE, Python, Golang and JavaScript
    * https://regex101.com/
  * Python正则表达式
    * https://mp.weixin.qq.com/s/bc-Puk4AVc1XxusrbSwaHg
    * re模块主要定义了9个常量、12个函数、1个异常，每个常量和函数都会通过实际代码案例讲解，让大家能更直观的了解其作用！
  * https://github.com/haoran119/python/blob/66ca8ad50b905265dcb232de2437bd10c5372943/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20use%20Regular%20Expression%20%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F.py
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
  * https://github.com/haoran119/python/blob/b69260423d5abfefbf53b83c2a77d9962d4765cd/src/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython/How%20to%20parse%20arguments%20for%20command-line%20options.py
* How to use multiprocessing ?
  * [multiprocessing — Process-based parallelism — Python 3.9.5 documentation](https://docs.python.org/3/library/multiprocessing.html)

### FIX OF ERRORS

* How to fix AttributeError: MyBokeh instance has no attribute 'plot_all' ?
  * Check the indentation for other class member functions prior to plot_all()
* How to fix ModuleNotFoundError: No module named 'a.b' when from a.b.c import d ?
  * Check if there is __init.py__ under /a
How to fix NameError: name 'var' is not defined when define var in try statement and use it in catch / finally statement ?
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
