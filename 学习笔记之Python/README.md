# 学习笔记之Python

* [Welcome to Python.org](https://www.python.org/)
  * [3.9.5 Documentation (python.org)](https://docs.python.org/3/)
  * [The Python Tutorial — Python 3.10.2 documentation](https://docs.python.org/3/tutorial/index.html)
  * [The Python Standard Library — Python 3.10.2 documentation](https://docs.python.org/3/library/index.html)
  * [Glossary — Python 3.9.7 documentation](https://docs.python.org/3/glossary.html#glossary)
  * [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
  * [Programming FAQ — Python 3.9.6 documentation](https://docs.python.org/3/faq/programming.html)
  * [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
  * [Installing packages using pip and virtual environments — Python Packaging User Guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
```shell
# MacOS
$ python3 -m pip install --user virtualenv
$ python3 -m venv .venv
$ source ~/.venv/bin/activate
(.venv) $ which python3
~/.venv/bin/python3
(.venv) $ python3 -m pip install numpy
(.venv) $ python3 -m pip install pandas
(.venv) $ python3
>>> import numpy
>>> import pandas
(.venv) $ deactivate

# Windows
$ py -m venv .venv
$ source .venv/Scripts/activate
$ py -m pip install --upgrade pip
$ py -m pip --version
$ py -m pip install requests
$ py -m pip install "requests==2.18.4"
$ py -m pip install "requests>=2.0.0,<3.0.0"
$ py -m pip install --upgrade requests
$ py -m pip install -r requirements.txt
$ py -m pip freeze

$ python -h
usage: /Library/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python
[option] ... [-c cmd | -m mod | file | -] [arg] ...
Options (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-P     : don't prepend a potentially unsafe path to sys.path
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env      : print help about Python environment variables and exit
--help-xoptions : print help about implementation-specific -X options and exit
--help-all      : print complete help information and exit
Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```
* [PyPI – the Python Package Index · PyPI](https://pypi.org/)
    * Find, install and publish Python packages with the Python Package Index
    * The Python Package Index (PyPI) is a repository of software for the Python programming language.
* [Python（计算机编程语言）_百度百科 (baidu.com)](https://baike.baidu.com/item/Python/407313?fr=aladdin#reference-[12]-21087-wrap)
  * 自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和Web编程。
  * Python是完全面向对象的语言。函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符和动态类型。
  * Python允许像数学的常用写法那样连着写两个比较运行符。比如a < b < c与a < b and b < c等价。C++的结果与Python不一样，首先它会先计算a < b，根据两者的大小获得0或者1两个值之一，然后再与c进行比较。
  * Python拥有一个强大的标准库。Python语言的核心只包含数字、字符串、列表、字典、文件等常见类型和函数，而由Python标准库提供了系统管理、网络通信、文本处理、数据库接口、图形系统、XML处理等额外的功能。
* [Python Technologies Tutorials](https://www.tutorialspoint.com/python_technologies_tutorials.htm)
  * [Python 3 Tutorial](https://www.tutorialspoint.com/python3/index.htm)
* [Python Programming Language - GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/?ref=shm)
* [Python3 教程 | 菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)
* [Python 入门指南 — Python tutorial 3.6.0 documentation](http://www.pythondoc.com/pythontutorial3/index.html)
* [Online Python-3 Compiler (Interpreter)](https://www.tutorialspoint.com/execute_python3_online.php)

## NOTES

* [python/面试总结之Python at main · haoran119/python](https://github.com/haoran119/python/tree/main/%E9%9D%A2%E8%AF%95%E6%80%BB%E7%BB%93%E4%B9%8BPython)
* [学习笔记之盘一盘 Python 系列 1 & 2 - 入门篇 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11289321.html)
* [学习笔记之Python开发环境 IDE ( Anaconda / PyCharm ) - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/8915306.html)
* [学习笔记之Python 3 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/10825575.html)
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

### [Python Cookbook, 3rd Edition](https://www.oreilly.com/library/view/python-cookbook-3rd/9781449357337/?_gl=1*4lnmwr*_ga*MTU3ODMwNTU5Ny4xNzQzNTAwNjk2*_ga_092EL089CH*MTc0MzUwMDY5NS4xLjEuMTc0MzUwMDcyMS4zNC4wLjA.)

* [dabeaz/python-cookbook: Code samples from the "Python Cookbook, 3rd Edition", published by O'Reilly & Associates, May, 2013.](https://github.com/dabeaz/python-cookbook/tree/master)
* by David Beazley, Brian K. Jones
* Released May 2013
* Book description
  * If you need help writing programs in Python 3, or want to update older Python 2 code, this book is just the ticket. Packed with practical recipes written and tested with Python 3.3, this unique cookbook is for experienced Python programmers who want to focus on modern tools and idioms.
  * Inside, you’ll find complete recipes for more than a dozen topics, covering the core Python language as well as tasks common to a wide variety of application domains. Each recipe contains code samples you can use in your projects right away, along with a discussion about how and why the solution works.
* Topics include:
  * Data Structures and Algorithms
  * Strings and Text
  * Numbers, Dates, and Times
  * Iterators and Generators
  * Files and I/O
  * Data Encoding and Processing
  * Functions
  * Classes and Objects
  * Metaprogramming
  * Modules and Packages
  * Network and Web Programming
  * Concurrency
  * Utility Scripting and System Administration
  * Testing, Debugging, and Exceptions
  * C Extensions

#### Data Structures and Algorithms

##### 1.2. Unpacking Elements from Iterables of Arbitrary Length

* You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a “too many values to unpack” exception.
```python
# example.py
#
# Unpacking of tagged tuples of varying sizes

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
```


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

### [Python Setup and Usage](https://docs.python.org/3/using/index.html)

#### [1. Command line and environment](https://docs.python.org/3/using/cmdline.html)

* The CPython interpreter scans the command line and the environment for various settings.

##### [1.1. Command line](https://docs.python.org/3/using/cmdline.html#command-line)

* When invoking Python, you may specify any of these options:
    * `python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]`
* The most common use case is, of course, a simple invocation of a script:
    * `python myscript.py`

###### 1.1.1. Interface options

#
[`-m <module-name>`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)

* Search [sys.path](https://docs.python.org/3/library/sys.html#sys.path) for the named module and execute its contents as the [__main__](https://docs.python.org/3/library/__main__.html#module-__main__) module.
* Since the argument is a module name, you must not give a file extension (`.py`). The module name should be a valid absolute Python module name, but the implementation may not always enforce this (e.g. it may allow you to use a name that includes a hyphen).
* Package names (including namespace packages) are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute `<pkg>.__main__` as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.
* `Note This option cannot be used with built-in modules and extension modules written in C, since they do not have Python module files. However, it can still be used for precompiled modules, even if the original source file is not available.`
* If this option is given, the first element of sys.argv will be the full path to the module file (while the module file is being located, the first element will be set to `"-m"`). As with the -c option, the current directory will be added to the start of sys.path.
* -I option can be used to run the script in isolated mode where sys.path contains neither the current directory nor the user’s site-packages directory. All PYTHON* environment variables are ignored, too.
* Many standard library modules contain code that is invoked on their execution as a script. An example is the timeit module:
```py
python -m timeit -s "setup here" "benchmarked code here"
python -m timeit -h # for details
```
* Raises an auditing event cpython.run_module with argument module-name.
* [Python 中 -m 的典型用法、原理解析与发展演变](https://mp.weixin.qq.com/s/tD3eSb2WdOPN_dKAQ9d6Ag)
    * 本文想要聊聊比较特殊的“-m”选项：关于它的典型用法、原理解析与发展演变的过程。
    * 首先，让我们用“--help”来看看它的解释：
        * `-m  mod run library module as a script (terminates option list)`
        * "mod"是“module”的缩写，即“-m”选项后面的内容是 module（模块），其作用是把模块当成脚本来运行。
        * “terminates option list”意味着“-m”之后的其它选项不起作用，在这点上它跟“-c”是一样的，都是“终极选项”。官方把它们定义为“接口选项”（Interface options），需要区别于其它的普通选项或通用选项。
    * -m 选项的五个典型用法
        * 在 Python3 中，只需一行命令就能实现一个简单的 HTTP 服务：
            * `python -m http.server 8000`
            * 执行后，在本机打开“http://localhost:8000”，或者在局域网内的其它机器上打开“http://本机ip:8000”，就能访问到执行目录下的内容
        * 与此类似，我们只需要一行命令`python -m pydoc -p xxx`，就能生成 HTML 格式的官方帮助文档，可以在浏览器中访问。
        * 它的第三个常见用法是执行 pdb 的调试命令`python -m pdb xxx.py`，以调试模式来执行“xxx.py”脚本：
        * 第四个同样挺有用的场景是用 timeit 在命令行中测试一小段代码的运行时间。
            * `python -m timeit "'.'.join(str(n) for n in range(100))"`
        * 最后，还有一种常常被人忽略的场景：`python -m pip install xxx`。我们可能会习惯性地使用`pip install xxx`，或者做了版本区分时用`pip3 install xxx`，总之不在前面用`python -m`做指定。但这种写法可能会出问题。
            * 很巧合的是，在本月初（2019.11.01），Python 的核心开发者、第一届指导委员会五人成员之一的 Brett Cannon 专门写了一篇博客《Why you should use "python -m pip"》，提出应该使用`python -m pip`的方式，并做了详细的解释。
            * 他的主要观点是：在存在多个 Python 版本的环境中，这种写法可以精确地控制三方库的安装位置。例如用`python3.8 -m pip`，可以明确指定给 3.8 版本安装，而不会混淆成其它的版本。
    * -m 选项的两种原理解析
        * 对于`python -m name`，一句话解释：Python 会检索sys.path ，查找名字为“name”的模块或者包（含命名空间包），并将其内容当成`__main__`模块来执行。
        * 1、对于普通模块
            * 以“.py”为后缀的文件就是一个模块，在“-m”之后使用时，只需要使用模块名，不需要写出后缀，但前提是该模块名是有效的，且不能是用 C 语言写成的模块。
            * 在“-m”之后，如果是一个无效的模块名，则会报错“No module named xxx”。
            * 如果是一个带后缀的模块，则首先会导入该模块，然后可能报错：Error while finding module specification for 'xxx.py' (AttributeError: module 'xxx' has no attribute '__path__'。
            * 由此差异，我们其实可以总结出“-m”的用法：已知一个模块的名字，但不知道它的文件路径，那么使用“-m”就意味着交给解释器自行查找，若找到，则当成脚本执行。
            * 那么，“-m”方式与直接运行脚本相比，在实现上有什么不同呢？
                * 直接运行脚本时，相当于给出了脚本的完整路径（不管是绝对路径还是相对路径），解释器根据文件系统的查找机制， 定位到该脚本，然后执行
                * 使用“-m”方式时，解释器需要在不 import 的情况下，在所有模块命名空间 中查找，定位到脚本的路径，然后执行。为了实现这个过程，解释器会借助两个模块：`pkgutil` 和 `runpy`，前者用来获取所有的模块列表，后者根据模块名来定位并执行脚本
        * 2、对于包内模块
            * 如果“-m”之后要执行的是一个包，那么解释器经过前面提到的查找过程，先定位到该包，然后会去执行它的“__main__”子模块，也就是说，在包目录下需要实现一个“__main__.py”文件。
            * 换句话说，假设有个包的名称是“pname”，那么，`python -m pname`，其实就等效于`python -m pname.__main__`。
    * -m 选项的十年演变过程

### [Python HOWTOs](https://docs.python.org/3/howto/index.html)

#### [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)

* [2to3 — Automated Python 2 to 3 code translation](https://docs.python.org/3/library/2to3.html)
    * 2to3 is a Python program that reads Python 2.x source code and applies a series of fixers to transform it into valid Python 3.x code. The standard library contains a rich set of fixers that will handle almost all code. 2to3 supporting library lib2to3 is, however, a flexible and generic library, so it is possible to write your own fixers for 2to3.
    * Deprecated since version 3.11, will be removed in version 3.13: The lib2to3 module was marked pending for deprecation in Python 3.9 (raising PendingDeprecationWarning on import) and fully deprecated in Python 3.11 (raising DeprecationWarning). The 2to3 tool is part of that. It will be removed in Python 3.13.

##### Learn the differences between Python 2 & 3

* Typically the two best ways of doing that is reading the [“What’s New”](https://docs.python.org/3/whatsnew/index.html#whatsnew-index) doc for each release of Python 3 and the [Porting to Python 3](http://python3porting.com/) book (which is free online). There is also a handy [cheat sheet](https://python-future.org/compatible_idioms.html) from the Python-Future project.

##### MISC

* What's the difference of default encoding between py2 and py3?
    * In Python, the default string encoding can vary between different versions:
        * Python 2: The default string in Python 2 is `ASCII`. This means that when you type a string directly into your Python 2 code, it's treated as an ASCII string. If you want to include non-ASCII characters in your string, you have to mark it as a Unicode string using the `u` prefix, like `u"こんにちは"`. For file encoding, Python 2 uses ASCII as well.
        * Python 3: Python 3 changed to use `UTF-8` as the default source code encoding. This means you can include non-ASCII characters in your strings without needing a special prefix. Moreover, the `str` type in Python 3 is equivalent to the `unicode` type in Python 2, and Python 3 introduced a separate `bytes` type for handling raw binary data. For file encoding, Python 3 uses `UTF-8` by default.
    * This change was part of Python's overall move towards better Unicode support in Python 3, which makes it easier to write code that handles international characters and works consistently across different languages and platforms.
    * Do note that while these are the defaults, Python both 2 and 3 allow you to specify a different encoding for a source code file using a special comment at the top of the file:
    * `# -*- coding: encoding -*-`
    * Replace encoding with the name of the encoding you want to use, like 'utf-8' or 'latin-1'. This will override the default encoding for that file.
* How to fix `exec("import lib") in globals()` in Python 3?
    * `exec("import lib", globals())`
* How to fix `[ERROR] 'Exception' object has no attribute 'message' in py3`?
    * In Python 2, exceptions had a message attribute where you could find the error message. However, this attribute was deprecated in Python 2.6 and removed in Python 3.
    * To get the message from an exception in Python 3, you should use the `str()` function or the `args` attribute.
```python
try:
    errorMsg = "Verification failed"
    raise Exception(errorMsg)
except Exception as e:
    print(str(e))  # use str function to print the error message
    print(e.args)  # or use args attribute which is a tuple containing all arguments passed to the exception
```
* What's the difference of using string.replace() with bytes object between py2 and py3?
    * There is indeed a key difference between how Python 2 and Python 3 handle strings and bytes, and this does affect the `replace()` method.
    * In Python 2, there's a `str` type, which is a sequence of bytes, and a `unicode` type, which is a sequence of Unicode characters.
    * In Python 3, however, the `str` type is a sequence of Unicode characters (equivalent to Python 2's `unicode`), and there's a new `bytes` type that's a sequence of bytes (equivalent to Python 2's `str`).
    * This means that if you want to use `replace()` on a bytes object in Python 3, you need to give it bytes arguments, not string arguments. Here's an example:
    ```python
    # Python 3
    b = b'Hello, world!'
    b = b.replace(b'world', b'Python')
    print(b)  # Outputs: b'Hello, Python!'
    ```
    * If you tried to give it string arguments, like `b.replace('world', 'Python')`, it would give you a `TypeError`, because it's expecting bytes, not strings.
    * In Python 2, the equivalent code would be:
    ```python
    # Python 2
    s = 'Hello, world!'
    s = s.replace('world', 'Python')
    print(s)  # Outputs: 'Hello, Python!'
    ```
    * This works with strings in Python 2 because Python 2's `str` type is a sequence of bytes. If you wanted to use Unicode strings in Python 2, you would use the `unicode` type and the `u` prefix.
    * Please note that for Python 2 code, to print a non-ASCII string in the console, you may need to encode it to an appropriate encoding (such as UTF-8).
* How to use lxml.etree.tostring() in Python 3?
    * https://lxml.de/tutorial.html
    * Using the `lxml.etree.tostring()` function in Python 3 is very similar to using it in Python 2. The function is used to create a string representation of an XML `Element` or `ElementTree`. Here's a basic example:
    ```python
    from lxml import etree

    # Create a root element
    root = etree.Element("root")

    # Add child elements
    child1 = etree.SubElement(root, "child1")
    child2 = etree.SubElement(root, "child2")

    # Add text to the child elements
    child1.text = "Text for child 1"
    child2.text = "Text for child 2"

    # Convert the root Element to a string
    output = etree.tostring(root, pretty_print=True, encoding='unicode')

    print(output)
    ```
    * This script will output:
    ```xml
    <root>
      <child1>Text for child 1</child1>
      <child2>Text for child 2</child2>
    </root>
    ```
    * In this example, `encoding='unicode'` is used to ensure that the `tostring` function returns a Python `str` object rather than a `bytes` object. If you omit this argument, `tostring` will return a bytes object, and you may need to decode it to a string using the `bytes.decode()` method.
    * The `pretty_print=True` argument is used to format the output with indents and newlines to make it easier to read. If you omit this argument or set it to `False`, the output will be a single line without any extra whitespace.

### [Basic Operators](https://www.tutorialspoint.com/python3/python_basic_operators.htm)

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
* Comparisons
  * 6. Expressions — Python 3.7.4 documentation
    * https://docs.python.org/3/reference/expressions.html#comparisons
    * Unlike C, all comparison operations in Python have the same priority, which is lower than that of any arithmetic, shifting or bitwise operation. Also unlike C, expressions like a < b < c have the interpretation that is conventional in mathematics
    * Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).

### [Decision Making](https://www.tutorialspoint.com/python3/python_decision_making.htm)

* Conditional Expressions
  * 6. Expressions — Python 3.7.0 documentation
    * https://docs.python.org/3/reference/expressions.html?highlight=conditional%20expressions#conditional-expressions
    * x = 1 if y == 1 else 0
    * 注意Python中没有三元运算符 y == 1 ? 1 : 0
  * 1 PEP 308: Conditional Expressions
    * https://docs.python.org/2.5/whatsnew/pep-308.html
* [条件语句的七种写法](https://mp.weixin.qq.com/s?__biz=Mzg4NDQwNTI0OQ==&mid=2247522923&idx=4&sn=04c0072a03765c7741f459cd0807d9b7&source=41#wechat_redirect)

### [Loops](https://www.tutorialspoint.com/python3/python_loops.htm)

* Two types usage of for loop ?
  * python - "for loop" with two variables? - Stack Overflow
    * https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
* [Using else conditional statement with for loop in python - GeeksforGeeks](https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/)
	* In most of the programming languages (C/C++, Java, etc), the use of else statement has been restricted with the if conditional statements. But Python also allows us to use the else condition with for loops.
	* The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

#### Iterator / Generator

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

* The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

A
abs()
aiter()
all()
any()
anext()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()

R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()
_
__import__()

#### [exec](https://docs.python.org/3/library/functions.html?highlight=exec#exec)

* `exec(object, globals=None, locals=None, /, *, closure=None)`
* This function supports dynamic execution of Python code. object must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). 1 If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section File input in the Reference Manual). Be aware that the nonlocal, yield, and return statements may not be used outside of function definitions even within the context of code passed to the exec() function. The return value is None.
* In all cases, if the optional parts are omitted, the code is executed in the current scope. If only globals is provided, it must be a dictionary (and not a subclass of dictionary), which will be used for both the global and the local variables. If globals and locals are given, they are used for the global and local variables, respectively. If provided, locals can be any mapping object. Remember that at the module level, globals and locals are the same dictionary. If exec gets two separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.
* If the globals dictionary does not contain a value for the key __builtins__, a reference to the dictionary of the built-in module builtins is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own __builtins__ dictionary into globals before passing it to exec().
* The closure argument specifies a closure–a tuple of cellvars. It’s only valid when the object is a code object containing free variables. The length of the tuple must exactly match the number of free variables referenced by the code object.
* Raises an auditing event exec with the code object as the argument. Code compilation events may also be raised.
* `Note` The built-in functions globals() and locals() return the current global and local dictionary, respectively, which may be useful to pass around for use as the second and third argument to exec().
* `Note` The default locals act as described for function locals() below: modifications to the default locals dictionary should not be attempted. Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns.
* Changed in version 3.11: Added the closure parameter.
* How to use exec()?
    * In Python, the `exec()` function is used to execute dynamically created program, which is either a string or object code. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). If it is an object code, it is simply executed. Here is a simple example of its usage:
    ```python
    program = 'a = 5\nb=10\nprint("Sum =", a+b)'
    exec(program)
    ```
    * In this case, the string `program` is a valid Python program, and when passed to `exec()`, it's executed just as if you had typed it into a Python script.
    * Please be aware that the use of `exec()` comes with security considerations, especially if you're executing code from an untrusted source. It can execute arbitrary Python code, which could potentially do harmful things to your system. Therefore, you should be very careful about using it in a secure context, and it's generally best to avoid its use if possible.

#### [globals()](https://docs.python.org/3/library/functions.html?highlight=exec#globals)

* Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.
* How to use globals()?
    * In Python, `globals()` is a built-in function that returns a dictionary representing the current global symbol table, which is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).
    * This dictionary will contain all global variables. Here's a simple example:
    ```python
    x = 10
    y = 20

    def show_globals():
        print(globals())

    show_globals()
    ```
    * In this example, `show_globals()` will print out a dictionary containing all global variables, including `x` and `y`.
    * Keep in mind that `globals()` gives you access to all global variables, so modifying this dictionary will affect those variables. For example:
    ```python
    globals()['x'] = 25
    print(x)  # This will print 25
    ```
    * Again, as with `exec()`, be aware that modifying global variables can have far-reaching effects, and should be done with care. Modifying the output of `globals()` should be done sparingly and cautiously, if at all.

#### [locals()](https://docs.python.org/3/library/functions.html?highlight=exec#locals)

* Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary.
* `Note` The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.

#### [open](https://docs.python.org/3/library/functions.html#open)

* `open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
* Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. See Reading and Writing Files for more examples of how to use this function.

#### [ord](https://docs.python.org/3/library/functions.html#ord)

* `ord(c)`
* Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of [chr()](https://docs.python.org/3/library/functions.html#chr).

#### [reversed](https://docs.python.org/3/library/functions.html?highlight=reversed#reversed)

* `reversed(seq)`
* Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

#### [zip](https://docs.python.org/3/library/2to3.html?highlight=zip#2to3fixer-zip)

* `zip(*iterables, strict=False)`
* Iterate over several iterables in parallel, producing tuples with an item from each one.
* Wraps zip() usage in a list call. This is disabled when from future_builtins import zip appears.

#### MISC

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
* [Python高阶函数使用总结](https://mp.weixin.qq.com/s/xtO8NDq3lVacsT5Z7eQXmw)
  * 本文结合各种实际的例子详细讲解了Python5个内建高阶函数的使用，能够帮助理解Python的数据结构和提高数据处理的效率，这5个函数分别是：
    * map
    * reduce
    * filter
    * sorted/sort
    * zip
* [Python | fabs() vs abs() - GeeksforGeeks](https://www.geeksforgeeks.org/python-fabs-vs-abs/)
  * Both the abs() and the fabs() function is used to find the absolute value of a number, i.e., remove the negative sign of a number.
  * Both will return the absolute value of a number.
  * The difference is that math.fabs(number) will always return a floating-point number even if the argument is an integer, whereas abs() will return a floating-point or an integer depending upon the argument.
  * In case the argument is a complex number, abs() will return the magnitude part whereas fabs() will return an error.
  * To use the fabs() function we need to import the library “math” while the abs() function comes with the standard library of Python.
* [class complex([real[, imag]])](https://docs.python.org/3/library/functions.html?highlight=complex#complex)
	* Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.
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
* [len(x) 击败 x.len()，从内置函数看 Python 的设计思想 (qq.com)](https://mp.weixin.qq.com/s/IRMplJCoWtH98uNtAeFKxg)

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

#### [Constants added by the site module](https://docs.python.org/3/library/constants.html#constants-added-by-the-site-module)

* The site module (which is imported automatically during startup, except if the -S command-line option is given) adds several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be used in programs.
* quit(code=None)
* exit(code=None)
	* Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when called, raise SystemExit with the specified exit code.
* [Python exit commands: quit(), exit(), sys.exit() and os._exit() - GeeksforGeeks](https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/)
	* The functions quit(), exit(), sys.exit() and os._exit() have almost the same functionality as they raise the SystemExit exception by which the Python interpreter exits and no stack traceback is printed. We can catch the exception to intercept early exits and perform cleanup activities; if uncaught, the interpreter exits as usual.
* copyright
* credits
	* Objects that when printed or called, print the text of copyright or credits, respectively.
* license
	* Object that when printed, prints the message “Type license() to see the full license text”, and when called, displays the full license text in a pager-like fashion (one screen at a time).

### [Built-in Types](https://docs.python.org/3/library/stdtypes.html)

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

#### [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

* [Numbers](https://www.tutorialspoint.com/python3/python_numbers.htm)
* How to display a decimal in scientific notation ?
  * '{:.2e}'.format(0.456) = '4.56e-01'
  * '{:.2f}'.format(0.456) = '0.46'
  * python - Display a decimal in scientific notation - Stack Overflow
    * https://stackoverflow.com/questions/6913532/display-a-decimal-in-scientific-notation
* [Python Scientific Notation With Suppressing And Conversion - Python Pool](https://www.pythonpool.com/python-scientific-notation/#:~:text=Python%20has%20a%20defined%20syntax,E%20is%20the%20exponent%20symbol.)
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

#### [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

##### [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)

* The operations in the following table are supported by most sequence types, both mutable and immutable. The collections.abc.Sequence ABC is provided to make it easier to correctly implement these operations on custom sequence types.
* This table lists the sequence operations sorted in ascending priority. In the table, s and t are sequences of the same type, n, i, j and k are integers and x is an arbitrary object that meets any type and value restrictions imposed by s.
* The in and not in operations have the same priorities as the comparison operations. The + (concatenation) and * (repetition) operations have the same priority as the corresponding numeric operations.

Operation|Result
-|-
x in s|True if an item of s is equal to x, else False
x not in s|False if an item of s is equal to x, else True
s + t|the concatenation of s and t
s * n or n * s|equivalent to adding s to itself n times
s[i]|ith item of s, origin 0
s[i:j]|slice of s from i to j
s[i:j:k]|slice of s from i to j with step k
len(s)|length of s
min(s)|smallest item of s
max(s)|largest item of s
s.index(x[, i[, j]])|index of the first occurrence of x in s (at or after index i and before index j)
s.count(x)|total number of occurrences of x in s

* Sequences of the same type also support comparisons. In particular, tuples and lists are compared lexicographically by comparing corresponding elements. This means that to compare equal, every element must compare equal and the two sequences must be of the same type and have the same length. (For full details see Comparisons in the language reference.)
* Forward and reversed iterators over mutable sequences access values using an index. That index will continue to march forward (or backward) even if the underlying sequence is mutated. The iterator terminates only when an IndexError or a StopIteration is encountered (or when the index drops below zero).

##### [Immutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#immutable-sequence-types)

* The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the hash() built-in.
* This support allows immutable sequences, such as tuple instances, to be used as dict keys and stored in set and frozenset instances.
* Attempting to hash an immutable sequence that contains unhashable values will result in TypeError.

##### [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)

* The operations in the following table are defined on mutable sequence types. The collections.abc.MutableSequence ABC is provided to make it easier to correctly implement these operations on custom sequence types.
* In the table s is an instance of a mutable sequence type, t is any iterable object and x is an arbitrary object that meets any type and value restrictions imposed by s (for example, bytearray only accepts integers that meet the value restriction 0 <= x <= 255).

Operation|Result|Notes
-|-|-
s[i] = x|item i of s is replaced by x
s[i:j] = t|slice of s from i to j is replaced by the contents of the iterable t
del s[i:j]|same as s[i:j] = []
s[i:j:k] = t|the elements of s[i:j:k] are replaced by those of t|(1)
del s[i:j:k]|removes the elements of s[i:j:k] from the list
s.append(x)|appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
s.clear()|removes all items from s (same as del s[:])|(5)
s.copy()|creates a shallow copy of s (same as s[:])|(5)
s.extend(t) or s += t|extends s with the contents of t (for the most part the same as s[len(s):len(s)] = t)
s *= n|updates s with its contents repeated n times|(6)
s.insert(i, x)|inserts x into s at the index given by i (same as s[i:i] = [x])
s.pop() or s.pop(i)|retrieves the item at i and also removes it from s|(2)
s.remove(x)|remove the first item from s where s[i] is equal to x|(3)
s.reverse()|reverses the items of s in place|(4)

* Notes:
1. t must have the same length as the slice it is replacing.
2. The optional argument i defaults to -1, so that by default the last item is removed and returned.
3. remove() raises ValueError when x is not found in s.
4. The reverse() method modifies the sequence in place for economy of space when reversing a large sequence. To remind users that it operates by side effect, it does not return the reversed sequence.
5. clear() and copy() are included for consistency with the interfaces of mutable containers that don’t support slicing operations (such as dict and set). copy() is not part of the collections.abc.MutableSequence ABC, but most concrete mutable sequence classes provide it.
6. The value n is an integer, or an object implementing __index__(). Zero and negative values of n clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for s * n under Common Sequence Operations.

* [干货|理解Python列表和元组](https://mp.weixin.qq.com/s/U-ctO-brjwxpm0LbLTB-dw)

##### [Lists](https://www.tutorialspoint.com/python3/python_lists.htm)

* Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).
* [class list([iterable])](https://docs.python.org/3/library/stdtypes.html#list)
	* Lists may be constructed in several ways:
		* Using a pair of square brackets to denote the empty list: []
		* Using square brackets, separating items with commas: [a], [a, b, c]
		* Using a list comprehension: [x for x in iterable]
		* Using the type constructor: list() or list(iterable)
	* The constructor builds a list whose items are the same and in the same order as iterable’s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a list, a copy is made and returned, similar to iterable[:]. For example, list('abc') returns ['a', 'b', 'c'] and list( (1, 2, 3) ) returns [1, 2, 3]. If no argument is given, the constructor creates a new empty list, [].
	* Many other operations also produce lists, including the sorted() built-in.
	* Lists implement all of the common and mutable sequence operations. Lists also provide the following additional method:
		* [sort(*, key=None, reverse=False)](https://docs.python.org/3/library/stdtypes.html#list.sort)
			* This method sorts the list in place, using only < comparisons between items. Exceptions are not suppressed - if any comparison operations fail, the entire sort operation will fail (and the list will likely be left in a partially modified state).
			* sort() accepts two arguments that can only be passed by keyword (keyword-only arguments):
			* key specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of None means that list items are sorted directly without calculating a separate key value.
			* The functools.cmp_to_key() utility is available to convert a 2.x style cmp function to a key function.
			* reverse is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.
			* This method modifies the sequence in place for economy of space when sorting a large sequence. To remind users that it operates by side effect, it does not return the sorted sequence (use sorted() to explicitly request a new sorted list instance).
			* The sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
			* For sorting examples and a brief sorting tutorial, see [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html#sortinghowto).
			* CPython implementation detail: While a list is being sorted, the effect of attempting to mutate, or even inspect, the list is undefined. The C implementation of Python makes the list appear empty for the duration, and raises ValueError if it can detect that the list has been mutated during a sort.
			* [Python 列表排序 sort 与 sorted 详解](https://mp.weixin.qq.com/s/R16hyfikRCOEUGhDGOBVcQ)
				* https://maida6244.xyz/
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
* How to convert dictionary to list ?
  * Converting Python Dictionary to List - Stack Overflow
    * https://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
  * 4. Built-in Types — Python 3.6.6rc1 documentation
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dict.items
    * https://docs.python.org/3/library/stdtypes.html?highlight=items#dictionary-view-objects
  * 5. Data Structures — Python 3.8.3 documentation
    * https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
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

##### [Tuples](https://www.tutorialspoint.com/python3/python_tuples.htm)

* Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).
* [class tuple([iterable])](https://docs.python.org/3/library/stdtypes.html#tuple)
	* Tuples may be constructed in a number of ways:
		* Using a pair of parentheses to denote the empty tuple: ()
		* Using a trailing comma for a singleton tuple: a, or (a,)
		* Separating items with commas: a, b, c or (a, b, c)
		* Using the tuple() built-in: tuple() or tuple(iterable)
	* The constructor builds a tuple whose items are the same and in the same order as iterable’s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a tuple, it is returned unchanged. For example, tuple('abc') returns ('a', 'b', 'c') and tuple( [1, 2, 3] ) returns (1, 2, 3). If no argument is given, the constructor creates a new empty tuple, ().
	* Note that it is actually the comma which makes a tuple, not the parentheses. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity. For example, f(a, b, c) is a function call with three arguments, while f((a, b, c)) is a function call with a 3-tuple as the sole argument.
	* Tuples implement all of the common sequence operations.
	* For heterogeneous collections of data where access by name is clearer than access by index, collections.namedtuple() may be a more appropriate choice than a simple tuple object.
* How to convert list to tuple ?
  * tuple( list_obj )
  * [Python | Convert a list into a tuple - GeeksforGeeks](https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/)
    * tuple(list)
    * tuple(i for i in list)
    * (*list, )

#### [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

* [Strings](https://www.tutorialspoint.com/python3/python_strings.htm)
	* String Special Operators

Operator|Description|Example
-|-|-
r/R|Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.|print r'\n' prints \n and print R'\n'prints \n

* [Python String - GeeksforGeeks](https://www.geeksforgeeks.org/python-strings/)

##### [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

* Strings implement all of the common sequence operations, along with the additional methods described below.
* str.capitalize()
	* Return a copy of the string with its first character capitalized and the rest lowercased.
* [str.count(sub[, start[, end]])](https://docs.python.org/3/library/stdtypes.html#str.count)
	* Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
* str.find(sub[, start[, end]])
	* Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
	* Note The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator
* [str.format(*args, **kwargs)](https://docs.python.org/3/library/stdtypes.html#str.format)
	* Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
* str.index(sub[, start[, end]])
	* Like find(), but raise ValueError when the substring is not found.
* str.isalnum()
	* Return True if all characters in the string are alphanumeric and there is at least one character, False otherwise. A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
* str.isalpha()
	* Return True if all characters in the string are alphabetic and there is at least one character, False otherwise. Alphabetic characters are those characters defined in the Unicode character database as “Letter”, i.e., those with general category property being one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”. Note that this is different from the “Alphabetic” property defined in the Unicode Standard.
* str.isascii()
	* Return True if the string is empty or all characters in the string are ASCII, False otherwise. ASCII characters have code points in the range U+0000-U+007F.
* str.isdecimal()
	* Return True if all characters in the string are decimal characters and there is at least one character, False otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category “Nd”.
* str.isdigit()
	* Return True if all characters in the string are digits and there is at least one character, False otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.
* str.islower()
	* Return True if all cased characters 4 in the string are lowercase and there is at least one cased character, False otherwise.
* str.isnumeric()
	* Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.
* str.isspace()
	* Return True if there are only whitespace characters in the string and there is at least one character, False otherwise.
	* A character is whitespace if in the Unicode character database (see unicodedata), either its general category is Zs (“Separator, space”), or its bidirectional class is one of WS, B, or S.
* str.istitle()
	* Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.
* str.isupper()
	* Return True if all cased characters 4 in the string are uppercase and there is at least one cased character, False otherwise.
* str.join(iterable)
	* Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.
* str.lower()
	* Return a copy of the string with all the cased characters 4 converted to lowercase.
	* The lowercasing algorithm used is described in section 3.13 of the Unicode Standard.
* str.lstrip([chars])
	* Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped
* str.replace(old, new[, count])
	* Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
* str.removeprefix(prefix, /)
	* If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string
* str.removesuffix(suffix, /)
	* If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string
* str.rfind(sub[, start[, end]])
	* Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
* str.rindex(sub[, start[, end]])
	* Like rfind() but raises ValueError when the substring sub is not found.
* str.rsplit(sep=None, maxsplit=- 1)
	* Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.
* str.rstrip([chars])
	* Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped
* str.split(sep=None, maxsplit=-1)
	* Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
	* If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
	* If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
* str.splitlines(keepends=False)
	* Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
	* This method splits on the following line boundaries. In particular, the boundaries are a superset of universal newlines.
	* Unlike split() when a delimiter string sep is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line
* str.startswith(prefix[, start[, end]])
	* Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
* str.strip([chars])
	* Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped
* str.swapcase()
	* Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that s.swapcase().swapcase() == s.
* str.title()
	* Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
* str.upper()
	* Return a copy of the string with all the cased characters 4 converted to uppercase. Note that s.upper().isupper() might be False if s contains uncased characters or if the Unicode category of the resulting character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter, titlecase).
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
* How to convert list to string ?
  * stest = str(['test1', 'test2', 'test3']).strip('[]')
  * 4. Built-in Types — Python 3.6.6rc1 documentation
    * https://docs.python.org/3/library/stdtypes.html?highlight=str#text-sequence-type-str
    * https://docs.python.org/3/library/stdtypes.html?highlight=str#str.strip
  * python - TypeError: cannot concatenate 'str' and 'list' objects in email - Stack Overflow
    * https://stackoverflow.com/questions/26521899/typeerror-cannot-concatenate-str-and-list-objects-in-email
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

#### [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

* A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built-in dict, list, and tuple classes, and the collections module.)
* Like other collections, sets support x in set, len(set), and for x in set. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
* There are currently two built-in set types, set and frozenset. The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. The frozenset type is immutable and hashable — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.
* Non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: {'jack', 'sjoerd'}, in addition to the set constructor.

#### [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

* A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. (For other containers see the built-in list, set, and tuple classes, and the collections module.)
* A dictionary’s keys are almost arbitrary values. Values that are not hashable, that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)
* Dictionaries can be created by placing a comma-separated list of key: value pairs within braces, for example: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}, or by the dict constructor.
* [Dictionary](https://www.tutorialspoint.com/python3/python_dictionary.htm)
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
* How to sort dict ?
	* `sorted(mydict.items(), key=lambda x : x[1], reverse=True)`
	* [python - How do I sort a dictionary by value? - Stack Overflow](https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value)
	* [Python | Sort Python Dictionaries by Key or Value - GeeksforGeeks](https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/)

### [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

### [Exceptions Handling](https://www.tutorialspoint.com/python/python_exceptions.htm)

* How to use try ... except ... finally statement for exception ?
  * 8.4. The try statement - 8. Compound statements — Python 3.7.4 documentation
    * https://docs.python.org/3/reference/compound_stmts.html#the-try-statement
  * Manually raising (throwing) an exception in Python - Stack Overflow
    * https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python　　
* How to define custom exception ?
  * How to Define Custom Exceptions in Python? (With Examples)
    * https://www.programiz.com/python-programming/user-defined-exception
* [学习笔记之Python Debug ( pdb ) - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/10437091.html)
* [盘一盘 Python 系列特别篇 - 错误类型](https://mp.weixin.qq.com/s/PBaDdLcYxDso2V4aZcFXpA)
* [盘一盘 Python 系列特别篇 - 异常处理](https://mp.weixin.qq.com/s/94O3Kz__8UQZoZtQ-WyOcQ)
* [一文教你读懂 Python 中的异常信息](https://realpython.com/python-traceback/)
* [Python 常见的17个错误分析](https://www.oschina.net/question/89964_62779)
  * https://inventwithpython.com/blog/2012/07/09/16-common-python-runtime-errors-beginners-find/

### [Modules](https://www.tutorialspoint.com/python/python_modules.htm)

* How to import module from parent directory ?
  * import sys
  * sys.path.append('..')
  * from A import B
  * python - Importing modules from parent folder - Stack Overflow
    * https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
  * [学了半天，import 到底在干啥？](https://mp.weixin.qq.com/s/FN__-XO_-htH36jPLiiTZg)
* `import lib` vs `from lib import *`
    * These two Python import statements are used to import modules, but they do so in slightly different ways:
        * `import lib`: This imports the module `lib`, and creates a reference to that module in the current namespace. After this statement is executed, you can use `lib.name` to refer to things defined in the module.
        * `from lib import *`: This imports all items from the `lib` module directly into the current namespace. This means you can refer to them directly without the `lib.` prefix. However, if there are any naming conflicts between identifiers in the current namespace and in the module, the module's identifiers will overwrite the ones in the current namespace.
        * Here's a simple example to illustrate the difference:
        ```python
        # Suppose lib has a function named foo

        # using import
        import lib
        lib.foo()  # correct
        foo()  # NameError: name 'foo' is not defined

        # using from import
        from lib import *
        foo()  # correct
        lib.foo()  # NameError: name 'lib' is not defined, because 'lib' itself is not imported
        ```
        * As a best practice, it is generally better to use `import lib` or `from lib import specific_item` rather than `from lib import *`, because the latter can cause naming conflicts and make it unclear where certain functions or attributes are coming from, which can make the code harder to read and debug.
* [深入探讨Python的import机制：实现远程导入模块 | CSDN博文精选](https://mp.weixin.qq.com/s/Sx_WyKUpoZrnFtV9epAfpg)
* 你常常看到的 \_\_init\_\_.py 到底是个啥？
  * 综上，\_\_init\_\_.py 会在 import 的时候被执行，而空的 \_\_init\_\_.py 在 Python 新版本中已经不需要你额外去定义了，因为就算你不定义 init， Python 也知道你导入的包路径，但是如果你想要做一些初始化操作，或者像我们刚刚说的预先导入相关的模块，那么定义 \_\_init\_\_.py 还是很有必要的哟。
* [Python编程中的if \_\_name\_\_ == 'main' 的作用和原理](https://mp.weixin.qq.com/s/SXTo0h2ExujAQdWnLWggdg)
  * https://zhuanlan.zhihu.com/p/34112508
  * \_\_name\_\_ 是当前模块名，当模块被直接运行时模块名为 \_\_main\_\_ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。

### [Text Processing Services](https://docs.python.org/3/library/text.html)

#### [string — Common string operations](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#module-string)

* [String constants](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#string-constants)
	* [string.ascii_lowercase](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#string.ascii_lowercase)
		* The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.
* [Custom String Formatting](https://docs.python.org/3/library/string.html?highlight=ascii_lowercase#custom-string-formatting)
* [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
* [Helper functions](https://docs.python.org/3/library/string.html?#helper-functions)
	* [string.capwords(s, sep=None)](https://docs.python.org/3/library/string.html?#string.capwords)
		* Split the argument into words using str.split(), capitalize each word using str.capitalize(), and join the capitalized words using str.join(). If the optional second argument sep is absent or None, runs of whitespace characters are replaced by a single space and leading and trailing whitespace are removed, otherwise sep is used to split and join the words.
* [7.1. Fancier Output Formatting](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
	* 7.1.1. Formatted String Literals
		* Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.
```python
An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The
following example rounds pi to three places after the decimal:
>>>
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making
columns line up.
>>>
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r'
applies repr():
>>>
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

For a reference on these format specifications, see the reference guide for the Format Specification Mini-Language.
```

### [Data Types](https://docs.python.org/3/library/datatypes.html)

#### [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)

* [Date & Time](https://www.tutorialspoint.com/python3/python_date_time.htm)
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

#### [collections — Container datatypes](https://docs.python.org/3/library/collections.html)

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
    * collections — Container datatypes — Python 3.8.5 documentation
    * https://docs.python.org/3/library/collections.html?highlight=defaultdict#collections.defaultdict
    * class collections.defaultdict([default_factory[, ...]])
    * Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not documented here.
    * The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
  * OrderedDict：字典的子类，保留了他们被添加的顺序。
  * namedtuple：创建命名元组子类的工厂函数。
    * collections — Container datatypes — Python 3.8.0 documentation
      * https://docs.python.org/3/library/collections.html#collections.namedtuple
      * collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
      * Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.
      * collections — Container datatypes — Python 3.8.2 documentation
        * https://docs.python.org/3.8/library/collections.html?highlight=namedtuple#collections.somenamedtuple._replace
        * somenamedtuple._replace(**kwargs)
        * Return a new instance of the named tuple replacing specified fields with new values
  * deque：类似列表容器，实现了在两端快速添加(append)和弹出(pop)。
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

##### [enum — Support for enumerations](https://docs.python.org/3/library/enum.html)

* An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
* How to use enumerations ?
  * Design and History FAQ — Python 3.8.1 documentation
    * https://docs.python.org/3/faq/design.html?highlight=switch%20case#why-isn-t-there-a-switch-or-case-statement-in-python

### [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)

#### [cmath — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)

* [cmath.polar(x)](https://docs.python.org/3/library/cmath.html#cmath.polar)
	* Return the representation of x in polar coordinates. Returns a pair (r, phi) where r is the modulus of x and phi is the phase of x. polar(x) is equivalent to (abs(x), phase(x)).

### [Functional Programming Modules](https://docs.python.org/3/library/functional.html)

#### [itertools — Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)

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

### [File and Directory Access](https://docs.python.org/3/library/filesys.html)

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

### [Generic Operating System Services](https://docs.python.org/3/library/allos.html)

#### [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

* This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.

##### [Files and Directories](https://docs.python.org/3/library/os.html#files-and-directories)

* [os.walk(top, topdown=True, onerror=None, followlinks=False)](https://docs.python.org/3/library/os.html#os.walk)
	* Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
* How to iterate directory for files ?
	* [Python3 OS 文件/目录方法 | 菜鸟教程](http://www.runoob.com/python3/python3-os-file-methods.html)
	* [Python list directory, subdirectory, and files - Stack Overflow](https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files)
```python
import os

root = '.'

for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith('.json'):
            filename = os.path.join(path, name)
            print(filename) # '.\path\test.json'
```
* [python - In what order does os.walk iterates iterate? - Stack Overflow](https://stackoverflow.com/questions/18282370/in-what-order-does-os-walk-iterates-iterate)
	* os.walk uses os.listdir. Here is the docstring for os.listdir:
		* listdir(path) -> list_of_strings
		* Return a list containing the names of the entries in the directory.
		* path: path of directory to list
		* The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.
	* You could, however, use sort to ensure the order you desire.
* [How to sort os.walk list?](https://python-forum.io/thread-30142.html)
	* `for filename in sorted(files):`

#### [io — Core tools for working with streams](https://docs.python.org/3/library/io.html)

* The io module provides Python’s main facilities for dealing with various types of I/O. There are three main types of I/O: text I/O, binary I/O and raw I/O. These are generic categories, and various backing stores can be used for each of them. A concrete object belonging to any of these categories is called a file object. Other common terms are stream and file-like object.
* Independent of its category, each concrete stream object will also have various capabilities: it can be read-only, write-only, or read-write. It can also allow arbitrary random access (seeking forwards or backwards to any location), or only sequential access (for example in the case of a socket or pipe).
* All streams are careful about the type of data you give to them. For example giving a str object to the write() method of a binary stream will raise a TypeError. So will giving a bytes object to the write() method of a text stream.
* [Files I/O](https://www.tutorialspoint.com/python/python_files_io.htm)
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

#### [argparse — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)

* The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
* How to parse arguments for command-line options ?
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

#### [logging — Logging facility for Python](https://docs.python.org/3/library/logging.html)

* This module defines functions and classes which implement a flexible event logging system for applications and libraries.
* The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.
* The basic classes defined by the module, together with their functions, are listed below.
	* Loggers expose the interface that application code directly uses.
	* Handlers send the log records (created by loggers) to the appropriate destination.
	* Filters provide a finer grained facility for determining which log records to output.
	* Formatters specify the layout of log records in the final output.
* How to use logging ?
  * Logging HOWTO — Python 3.7.0 documentation
    * https://docs.python.org/3.7/howto/logging.html#basic-logging-tutorial
  * 16.6. logging — Logging facility for Python — Python 3.7.0 documentation
    * https://docs.python.org/3.7/library/logging.html#logging.debug
    * https://docs.python.org/3.7/library/logging.html#logging.info
    * https://docs.python.org/3.7/library/logging.html#logging.warning
    * [logging.error(msg, *args, **kwargs)](https://docs.python.org/3.7/library/logging.html#logging.error)
	    * Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug().
    * [logging.exception(msg, *args, **kwargs)](https://docs.python.org/3.7/library/logging.html#logging.exception)
    	* Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug(). Exception info is added to the logging message. This function should only be called from an exception handler.
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
```python
import logging

logging.basicConfig(filename='test.log',
                    format='[%(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO
                    )

logger = logging.getLogger('test')

logger.info('Start logging')
```
* [Python Logging 模块完全解读](https://mp.weixin.qq.com/s/iZEjyEoxVUQ5cner2VY1kg)
* [Python Logging — logger.error versus logger.exception | by Rahul Kumar | Medium](https://medium.com/@rahulkumar_33287/logger-error-versus-logger-exception-4113b39beb4b)
	* logger.error(e) will give you this as an output
	* Notice that while this gives a nicely formatter ERROR log, it suppresses the traceback information since we have set our log formatter to output log message on stdout in the format ‘%(asctime)-15s %(levelname)-2s %(message)s’.
	* logger.error(e, stack_info=True, exc_info=True) will give you that nicely formatted ERROR message in addition to the Traceback and Stack.
	* and finally logger.exception(e) will give that ERROR line and traceback information without having to set any flags. It does not give Stack though unless you set the stack_info=True in the argument.
```python
import logging

# create an instance of the logger
logger = logging.getLogger()

# logging set up
log_format = logging.Formatter('%(asctime)-15s %(levelname)-2s %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(log_format)

# add the handler
logger.addHandler(sh)
logger.setLevel(logging.INFO)


def do_something():
    return None


def call_do_something():
    # This will obviously throw and exception
    return do_something() + 4


# logging exception with logger.error()
try:
    call_do_something()
except Exception as e:
    logger.error(e)


# logging exception with logger.error() with full traceback
try:
    call_do_something()
except Exception as e:
    logger.error(e, stack_info=True, exc_info=True)


# logging exception with logger.exception() with full traceback
try:
    call_do_something()
except Exception as e:
    logger.exception(e)
```

### [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)

#### [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html)

* The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions:
	* os.system
	* os.spawn*
* [How to Execute Shell Commands With Python?](https://www.the-analytics.club/python-shell-commands#:~:text=If%20you%20need%20to%20execute,arguments%20or%20producing%20text%20output.)
	* If you need to execute a shell command with Python, there are two ways. You can either use the subprocess module or the command.run() function.

##### [Using the subprocess Module](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)

* The recommended approach to invoking subprocesses is to use the run() function for all use cases it can handle. For more advanced use cases, the underlying Popen interface can be used directly.

###### [subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)](https://docs.python.org/3/library/subprocess.html#subprocess.run)

* Run the command described by args. Wait for command to complete, then return a [CompletedProcess](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess) instance.
* The arguments shown above are merely the most common ones, described below in Frequently Used Arguments (hence the use of keyword-only notation in the abbreviated signature). The full function signature is largely the same as that of the Popen constructor - most of the arguments to this function are passed through to that interface. (timeout, input, check, and capture_output are not.)
* If `capture_output` is true, stdout and stderr will be captured. When used, the internal Popen object is automatically created with stdout=PIPE and stderr=PIPE. The stdout and stderr arguments may not be supplied at the same time as capture_output. If you wish to capture and combine both streams into one, use stdout=PIPE and stderr=STDOUT instead of capture_output.
* The `timeout` argument is passed to Popen.communicate(). If the timeout expires, the child process will be killed and waited for. The TimeoutExpired exception will be re-raised after the child process has terminated.
* The `input` argument is passed to Popen.communicate() and thus to the subprocess’s stdin. If used it must be a byte sequence, or a string if encoding or errors is specified or text is true. When used, the internal Popen object is automatically created with stdin=PIPE, and the stdin argument may not be used as well.
* If `check` is true, and the process exits with a non-zero exit code, a CalledProcessError exception will be raised. Attributes of that exception hold the arguments, the exit code, and stdout and stderr if they were captured.
* If `encoding` or `errors` are specified, or text is true, file objects for stdin, stdout and stderr are opened in text mode using the specified encoding and errors or the io.TextIOWrapper default. The universal_newlines argument is equivalent to text and is provided for backwards compatibility. By default, file objects are opened in binary mode.
* If `env` is not None, it must be a mapping that defines the environment variables for the new process; these are used instead of the default behavior of inheriting the current process’ environment. It is passed directly to Popen. This mapping can be str to str on any platform or bytes to bytes on POSIX platforms much like os.environ or os.environb.
* Examples:
```py
subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')
```

###### [class subprocess.CompletedProcess](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess)

* The return value from [run()](https://docs.python.org/3/library/subprocess.html#subprocess.run), representing a process that has finished.

### [Development Tools](https://docs.python.org/3/library/development.html)

* The modules described in this chapter help you write software. For example, the pydoc module takes a module and generates documentation based on the module’s contents. The doctest and unittest modules contains frameworks for writing unit tests that automatically exercise code and verify that the expected output is produced. 2to3 can translate Python 2.x source code into valid Python 3.x code.

#### [typing — Support for type hints](https://docs.python.org/3/library/typing.html)

* Note: The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
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
* [Using Python's Type Annotations - DEV](https://dev.to/dstarner/using-pythons-type-annotations-4cfe#:~:text=Type%20Annotations%20are%20a%20new,of%20a%20variable%20should%20be.&text=It%20is%20important%20to%20note,the%20program%20in%20any%20way)
* [python - How to annotate types of multiple return values? - Stack Overflow](https://stackoverflow.com/questions/40181344/how-to-annotate-types-of-multiple-return-values)
	* support for type hinting notation [has been added to most standard-library container types](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections) (see [PEP 585](https://www.python.org/dev/peps/pep-0585/#implementation) for the complete list). In fact, you can use this as of Python 3.7 too provided you use the from __future__ import annotations compiler switch for your modules and a type checker that supports the syntax.
```python
-> tuple[bool, str]
```

### [Debugging and Profiling](https://docs.python.org/3/library/debug.html)

* These libraries help you with Python development: the debugger enables you to step through code, analyze stack frames and set breakpoints etc., and the profilers run code and give you a detailed breakdown of execution times, allowing you to identify bottlenecks in your programs. Auditing events provide visibility into runtime behaviors that would otherwise require intrusive debugging or patching.

#### [timeit — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)

* This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one. It avoids a number of common traps for measuring execution times. See also Tim Peters’ introduction to the “Algorithms” chapter in the second edition of Python Cookbook, published by O’Reilly.

### [Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html)

#### [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

* The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.
* See [PEP 405](https://www.python.org/dev/peps/pep-0405) for more information about Python virtual environments.
* See also [Python Packaging User Guide: Creating and using virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
* [Python Virtual Environments Explained with Examples](https://www.freecodecamp.org/news/python-virtual-environments-explained-with-examples/)
	* Virtual environments can be described as isolated installation directories. This isolation allows you to localized the installation of your project’s dependencies, without forcing you to install them system-wide.

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
* [Python垃圾回收和GC模块](https://mp.weixin.qq.com/s/RG3ik-T2AbOYmylJevnSlA)
	* https://www.infoworld.com/article/3671673/python-garbage-collection-and-the-gc-module.html
	* 在这篇文章中，我们将看看Python内存管理是如何工作的，它的垃圾回收系统如何帮助优化Python程序中的内存，以及如何使用标准库和第三方模块来控制内存使用和垃圾回收。
	* Python如何管理内存
		* 什么是作用域
	* Python循环引用
	* Python垃圾回收器(GC)
	* 如何使用GC模块
	* 使用GC调试垃圾回收
	* 避免Python内存管理中的陷阱
		* 注意对象作用域
		* 使用weakref避免循环引用
		* 手动中断循环引用
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

### [Multithreaded Programming](https://www.tutorialspoint.com/python3/python_multithreading.htm)

* [Concurrent Execution — Python 3.10.2 documentation](https://docs.python.org/3/library/concurrency.html)
	* The modules described in this chapter provide support for concurrent execution of code. The appropriate choice of tool will depend on the task to be executed (CPU bound vs IO bound) and preferred style of development (event driven cooperative multitasking vs preemptive multitasking).
	* [threading — Thread-based parallelism — Python 3.10.2 documentation](https://docs.python.org/3/library/threading.html)
		* This module constructs higher-level threading interfaces on top of the lower level \_thread module. See also the queue module.
		* CPython implementation detail: In CPython, due to the Global Interpreter Lock, only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use multiprocessing or concurrent.futures.ProcessPoolExecutor. However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.
	* [multiprocessing — Process-based parallelism — Python 3.9.5 documentation](https://docs.python.org/3/library/multiprocessing.html)
		* multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows.
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
	* 一、多线程与多进程
	* 二、Python多进程编程
		* Process
			* 多进程的实现与你的操作系统有关。例如Unix/Linux操作系统提供了一个fork()系统调用来创建进程。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
			* 而Python的os模块里正好封装了该系统调用，所以在Unix/Linux操作系统可以通过os.fork()创建子进程。
			* 但是Window系统是没有这个系统调用的，因此没办法用fork()实现多进程。Python提供了一个multiprocessing模块来供跨平台版本的Python使用多进程，这个模块提供了一个Process类来代表一个进程对象。
		* Pool
			* 如果我们要创建大量的子进程，可以利用进程池的方式来批量创建子进程。
	* 三、进程间通信
		* Python模块multiprcess提供Queue和Pipe类来进行进程间的通信，另外还有很多方式，这里我们先介绍提出的这两种。
		* Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。Queue通过put()方法把数据插入到队尾，get()方法用于从队头取出数据。并且它们都有两个参数分别为blocked和timeout。当队列已满且blocked为True的时候，如果timeout为正值，则会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常，同理当队列为空且blocked为True的时候，如果timeout为正值，则会等待timeout时间直到有数据插入再取走。若等待时间内没有型数据插入则会抛出Queue.Empty异常。（创建Queue对象时接受一个maxsize参数来限制队列里的对象个数）
		* Pipe是方法是实现两个进程通信的另一种方法。Pipe对象分两种，一种为单向管道，一种为双向管道，可以通过构造方法Pipe ( duplex = False ) 来创建单向管道（默认为双向管道）。
		* Pipe执行任务的方式是，一个进程从Pipe的一端输入对象，然后一个进程从Pipe的另一端接收对象，单向管道只允许管道一端的进程输入，而双向管道则允许从两端输入
	* 四、小结
		* 掌握Python多进程编程技术可以充分利用多核CPU，极大的提高计算机的执行效率，例如在生成随机森林的时候，使用多进程可以提高CART的生成速率等等。
* [深入理解python多线程和多进程](https://mp.weixin.qq.com/s/w0dZrtv8ogdtxO8FT2LrEg)
	* 一、Python多线程
		* threading
			* 要启动一个线程，我们只需要把一个函数传入Thread实例，然后调用start()运行，这个我们之前操作进程调用Process实例的方式如出一辙。
			* current_thread()函数用于返回当前线程的实例，主线程实例的名字为MainThread，子线程的名字可以在创建时给予，或者被默认给予Thread-1，Thread-2这样的名字。
	* 二、Lock线程锁
		* 多进程和多线程最大的区别就在于，对于多进程，同一个变量各自有一份拷贝存在于每个进程，互不影响，而多线程不然，所有的线程共用所有的变量，因此，任何一个变量都可以被任意的一个线程修改。为了避免多个线程同时修改同一个变量这种危险情况的出现。首先我们需要理解，多个线程同时修改一个变量这种情况是怎么出现的。
		* 为了避免这种情况的发生，我们就需要提供线程锁来确保：当一个线程获得了change()的调用权时，另一个线程就不能在同时执行change()方法，直到锁被释放之后，获得了该锁才能继续进行修改。
		* 我们用threading.lock()方法创建一个线程锁
		* 当多个线程同时执行lock.acquire()时，只有一个线程能够成功地获得线程锁，然后继续执行代码，其它线程只能等待锁的释放。同时获得锁的线程一定要记得释放，否则会成为死线程。因此我们会用try...finally...来确保锁的释放。然而，锁的问题就是一方面让原本多线程的任务实际上又变成了单线程的运行方式（尽管对于Python的伪多线程而言，这并不会造成什么性能的下降），另外，又由于可以存在多个锁，对于不同的线程可能会持有不同的锁并且试图获取对方的锁时，可能会造成死锁，导致多个线程全部挂起，这时只能通过操作系统来强行终止。
	* 三、Python的GIL锁
		* 对于一个多核CPU，它可以同时执行多个线程。我们可以通过Windows提供的任务管理器看见CPU的资源占用率，因此，当我们提供一个无限循环的死线程时，CPU一核的占用率就会提升到100%，若是提供两个，就又会有一核的占用率到100%。如果在java或者C中这么做，那么确实会发生这种情况，但是，如果我们在Python中这样尝试的话
		* 可以看到，从 multiprocessing.cpu_count()得知我们有4个CPU，然后打印了4行说明已经执行了4个线程，这个时候我们的CPU占用率应该是满的，但实际上
		* 我们从红框中看到，情况并非如此。实际上哪怕我们启用再多的线程，CPU的占用率也不会提高多少。这是因为尽管Python使用的是真正的线程，但Python的解释器在执行代码时有一个GIL锁（Gloabal Interpreter Lock），不论是什么Python代码，一旦执行必然会获得GIL锁，然后每执行100行代码就会释放GIL锁使得其它线程有机会执行。GIL锁实际上就给一个Python进程的所有线程都上了锁，因此哪怕是再多的线程，在一个Python进程中也只能交替执行，也即是只能使用一个核。
	* 四、ThreadLocal
		* 既然我们已经知道，一个全局变量会受到所有线程的影响，那么，我们应该如何构建一个独属于这个线程的“全局变量”？换言之，我们既希望这个变量在这个线程中拥有类似于全局变量的功能，又不希望其它线程能够调用它，以防止出现上面所述的问题，该怎么做？
		* 使用ThreadLocal对象便是用于解决这个问题的方法而免于繁琐的操作，它由threading.local()方法创建：
		* 我们可以认为ThreadLocal的原理类似于创建了一个词典，当我们创建一个变量local_varient.a的时候实际上是在local_varient这个词典里面创建了数个以threading.current_thread()为关键字（当前线程），不同线程中的a为值的键值对组成的dict
		* 当然，我在这里只是试图简单的描述一下ThreadLocal的工作原理，因为实际上它的工作原理和我们上面利用dict的例程并不是完全一样的，因为ThreadLocal对象可供传给的变量完全不只一个
	* 五、进程和线程的比较
		* 在初步了解进程和线程以及它们在Python中的运用方式之后，我们现在来讨论一下二者的区别与利弊。
		* 执行特点
			* 首先，我们简单了解一下多任务的工作模式：通常我们会将其设计为Master-Worker 模式，Master负责分配任务，Worker负责执行任务，多任务环境下通常是一个Master对应多个Worker。那么多进程任务实现Master-Worker，主进程就是Master，其它进程是Worker。而多线程任务，主线程Master，子线程Worker。
			* 先来说说多进程，多进程的优点就在于，它的稳定性高。因为一个子进程的崩溃不会影响到其它子进程和主进程（主进程挂了还是会全崩的）。但多进程的问题就在于，其创建进程的开销过大，特别是Windows系统，其多进程的开销要比使用fork()的Unix/Linux系统大的多得多。并且，对于一个操作系统本身而言，它能够同时运行的进程数也是有限的。
			* 多线程模式占用的资源消耗没有多进程那么大，因此它也往往会更快一些（但似乎也不会快太多？但至少在Windows下多线程的效率往往要比多进程要高），而且，多线程模式与多进程模式正好相反，一个线程挂掉会直接让进程内包括主线程的所有的线程都崩溃，因为所有线程共享进程的内存。在Windows系统中，如果我们看到了这样的提示“该程序执行了非法操作，即将关闭”，那往往就是因为某个线程出现问题导致整个进程的崩溃。
		* 切换
			* 在使用多进程或多线程的时候都应该考虑线程数或者进程数切换的开销。无论是进程还是线程，如果数量太多，那么效率是肯定上不去的。
			* 因为操作系统在切换进程和线程时，需要先保存当前执行的现场环境（包括CPU寄存器的状态，内存页等），然后再准备另一个任务的执行环境（恢复上次的寄存器状态，切换内存页等），才能开始执行新任务。这个过程虽然很快，但再快也是需要耗时的，因此一旦任务数量过于庞大，那么浪费在准备环境的时间就也会非常巨大。
		* 计算密集型和IO密集型
			* 考虑多任务的类型也是我们判断如何构建工作模式的一个重要点。我们可以将任务简单的分为两类：计算密集型和IO密集型。
			* 计算密集型任务的特点是要进行大量的运算，消耗CPU资源，例如一些复杂的数学运算，或者是一些视频的高清解码运算等等，纯靠CPU的计算能力来执行的任务。这种任务虽然也可以用多任务模式来完成，但任务之间切换的消耗往往比较大，因此若是要高效的进行这类任务的运算，计算密集型任务同时进行的数量最好不要超过CPU的核心数。
			* 而对于语言而言，代码运行的效率对于计算密集型任务也是至关重要，因此，类似于Python这样的高级语言往往不适合，而像C这样的底层语言的效率就会更高。好在Python处理这类任务时用的往往是用C编写的库，但若是要自己实现这类任务的底层计算功能，还是以C为主比较好。
			* IO密集型的特点则是要进行大量的输入输出，涉及到网络、磁盘IO的任务往往都是IO密集型任务，这类任务消耗CPU的资源并不高，往往时间都是花在等待IO操作完成，因为IO操作的速度往往都比CPU和内存运行的速度要慢很多。对于IO密集型任务，多任务执行提升的效率就会很高，但当然，任务数量还是有一个限度的。
			* 而对于这类任务使用的编程语言，Python这类开发效率高的语言就会更适合，因为能减少代码量，而C语言效果就很差，因为写起来很麻烦。
			* 现代操作系统对IO操作进行了巨大的改进，其提供了异步IO的操作来实现单进程单线程执行多任务的方式，它在单核CPU上采用单进程模型可以高效地支持多任务。而在多核CPU上也可以运行多个进程（数量与CPU核心数相同）来充分地利用多核CPU。通过异步IO编程模型来实现多任务是目前的主流趋势。而在Python中，单进程的异步编程模型称为协程。
* [入门 | 三行Python代码，让数据预处理速度提高2到6倍](https://mp.weixin.qq.com/s/DgKuNIa_m-CsXWgHIz_3rQ)
  * https://towardsdatascience.com/heres-how-you-can-get-a-2-6x-speed-up-on-your-data-pre-processing-with-python-847887e63be5
* [Python 线程为什么要搞个 setDaemon ？](https://mp.weixin.qq.com/s/tRaQftWQNzE2a_ZKDLGE4w)
* [为什么 GIL 让多线程变得如此鸡肋？](https://mp.weixin.qq.com/s/QP4h36qqTWUKchrxN56v9A)
	* 这篇文章我们主要讲了 Python [GIL](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) 相关的问题。
	* 首先，我们了解到 GIL 属于 Python 解释器层面的，它并不是 Python 语言的特性，这一点我们一定不要搞混了。GIL 的存在会让 Python 在执行代码时，只允许同一时刻只有一个线程在执行，其目的是为了保证在执行过程中内存管理的安全性。
	* 之后我们通过一个例子，观察到 Python 在多线程运行 CPU 密集型任务时，执行效率比单线程还要低，其原因是因为在多核 CPU 环境下，GIL 的存在会导致多线程切换时无效的资源消耗，因此会降低程序运行的效率。
	* 但如果使用多线程运行 IO 密集型的任务，由于线程更多地是在等待 IO，所以并不会消耗 CPU 资源，这种情况下，使用多线程是可以提高程序运行效率的。
	* 最后，我们分析了 GIL 存在的原因，更多是因为历史问题导致，也正因为 GIL 的存在，很多 Python 开发者默认 Python 是线程安全的，这也间接增加了去除 GIL 的困难性。
	* 基于这些前提，我们平时在部署 Python 程序时，一般更倾向于使用多进程的方式去部署，就是为了避免 GIL 的影响。
	* 任何一种编程语言，都有其优势和劣势，我们需要理解它的实现机制，发挥其长处，才能更好地服务于我们的需求。

### [GUI Programming](https://www.tutorialspoint.com/python3/python_gui_programming.htm)

* [Top 10 Python GUI Frameworks for Developers | by Claire D. Costa | Towards Data Science](https://towardsdatascience.com/top-10-python-gui-frameworks-for-developers-adca32fbe6fc)
1. PyQt5
2. Tkinter
3. Kivy
4. wxPython
5. Libavg
6. PySimpleGUI
7. PyForms
8. Wax
9. PySide2
10. PyGUI
* [Python 图形界面框架 PyQt5 使用指南](https://mp.weixin.qq.com/s/ZWGKAYmIPxm2bJr0J3YpiA)
	* https://www.biaodianfu.com/pyqt5.html
	* 常见GUI框架
	* PyQt5[1]：Qt[2]是一个跨平台的 C++图形用户界面库。QT一度被诺基亚拥，后出售给芬兰的软件公司Digia Oyj。PyQt5是基于Digia公司Qt5的Python接口，由一组Python模块构成。PyQt5本身拥有超过620个类和6000函数及方法。在可以运行于多个平台，包括：Unix, Windows, and Mac OS。
	* Pyside6[3]：Pyside是QT公司官方提供的Python包，上一版本为Pyside2，对应的是QT5，最新版命名规则进行了调整，更改为Pyside6，对应的是QT6版本。由于官方出品的比较看好，缺点是发布比较晚，网上的资料没有PyQt5多。
	* Tkinter[4]：Python内置的GUI框架，使用TCL实现，Python中内嵌了TCL解释器，使用它的时候不用安装额外的扩展包，直接import，跨平台。不足之处在于UI布局全靠代码实现，只有15种常用部件，显示效果简陋。
	* PySimpleGUI[5]：PySimpleGUI 是 Tkinter 一层包装。使用 PySimpleGUI 实现自定义 GUI 所需的代码量要比使用 Tkinter 直接编写相同的 GUI 要少得多。
	* WxPython[6]：wxPython是Python语言对流行的wxWidgets跨平台GUI工具库的绑定。用得比较广泛，跨平台，C++编写，文档少，用户可能就需要根据编程内容对不同平台中的GUI代码做一些调整。遇到问题不好解决，代码布局控件，不直观。
	* Wax[7]：基于wxPython ，为克服wxPython的问题而制作的一个包。
	* Kivy[8]：主要针对多点触控程序，智能手机平板等，也可以在没有触屏功能的系统上，全平台支持（Windows, Linux, Mac OS X, Android and iOS.）使用Python和cython编写，中文支持差，需要自己下载中文库并且制定路径。
	* BeeWare[9]：Write once. Deploy everywhere.需要与Kivy配合使用。
	* Toga[10]：一个使用Python开发原生APP的GUI工具包。Toga由一个具有共享接口的基础组件库组成，以简化与平台无关的GUI开发。Toga适用于Mac OS、Windows、Linux（GTK）以及Android和iOS等移动平台。
	* Eel[11]：一个轻量的 Python 库，用于制作简单的类似于 Electron（但是比它更轻量） 的离线 HTML/JS GUI 应用程序，并具有对 Python 功能（capabilities）和库的完全访问权限。
	* Flexx[12]：一个纯 Python 工具包，用来创建图形化界面应用程序。其使用 Web 技术进行界面的渲染。你可以用 Flexx 来创建桌面应用，同时也可以导出一个应用到独立的 HTML 文档。因为使用纯 Python 开发，所以 Flexx 是跨平台的。只需要有 Python 和浏览器就可以运行。
	* pywebview[13]是围绕 webview 组件的轻量型跨平台包装器（wrapper），它允许在其自己的本机 GUI 窗口中显示 HTML 内容。它使您可以在桌面应用程序中使用 Web 技术，同时尽最大可能隐藏使用浏览器构建GUI的事实。
	* enaml[14]：一种能够让你用最小的努力就可以实现高质量GUI界面的的Python框架，也是一种独特的编程语言。enaml将声明性语言与基于约束的布局系统结合在一起，使用户可以轻松地定义灵活布局的UI。enaml应用程序可以在任何支持Python和Qt的平台上运行。
	* 个人想法：太多学不完，先学PyQt5，原因是资料多，学有余力再学pyside6，最后看下PySimpleGUI，看能否解决一些简单问题。
* [wxPython：Python首选的GUI库 | CSDN博文精选](https://mp.weixin.qq.com/s?__biz=Mzg4NDQwNTI0OQ==&mid=2247523070&idx=5&sn=7a5c7617864b6b876a3fb5a93a91af9d&source=41#wechat_redirect)
	* 跨平台的GUI工具库，较为有名的当属GTK+、Qt 和 wxWidgets 了。GTK+是C实现的，由于C语言本身不支持OOP，因而GTK+上手相当困难，写起来也较为复杂艰涩。Qt 和 wxWidgets 则是C++实现的，各自拥有庞大的用户群体。虽然我喜欢wxWidgets，但还是尽可能客观地搜集了关于Qt 和 wxWidgets 的对比评价。
* [PySimpleGUI/PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
	* PySimpleGUI/PySimpleGUI: Launched in 2018. It's 2022 and PySimpleGUI is actively developed & supported. Create complex windows simply. Supports tkinter, Qt, WxPython, Remi (in browser). Create GUI applications trivially with a full set of widgets. Multi-Window applications are also simple. 3.4 to 3.11 supported. 325+ Demo programs & Cookbook for rapid start. Extensive documentation. Examples for Machine Learning(OpenCV Integration, Chatterbot), Rainmeter-like Desktop Widgets, Matplotlib + Pyplot integration, add GUI to command line scripts, PDF & Image Viewer. For both beginning and advanced programmers. docs - PySimpleGUI.org GitHub - PySimpleGUI.com. The Minecraft of GUIs - simple to complex... does them all.
* [用 Python 制作可视化 GUI 界面，一键实现多种风格的照片处理](https://mp.weixin.qq.com/s/zF_VILOzWLVwWiRVqxeGTg)
	* 当我们点击“动漫风格”时，程序会针对先前的步骤将上传的图片变成动漫风格的头像，当我们点击“老照片修复”时，会针对上传的照片进行修复，对应的代码是Github上面一个名叫DeOldify的项目，在Github上面获得了15.2K的小星星，可谓是非常的火爆，该作者给我们提供了一个多语言版本的接口，调用这个接口我们可以快速的使用该项目的能力，为老照片上色

### UnitTest

* [Python中的两个测试工具](https://mp.weixin.qq.com/s/IUCoUkws923ojK__HPe3kA)
    * unittest: 一个通用的测试框架
    * doctest: 一个更简单的模块，是为检查文档而设计的，但也非常适合用来编写单元测试
    * unittest
        * unittest类似于流行的Java测试框架JUnit，它比doctest更灵活，更强大，能够帮助你以结构化的方式来编写庞大而详尽的测试集。
```py
import unittest, my_math

class ProductTestcase(unittest.TestCase):

    def setUp(self):
        print('begin test')

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math.product(x, y)
                self.assertEqual(p, x*y, 'integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10
                y = y/10
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'integer multiplication failed')

if __name__ == '__main__':
    unittest.main()
```
* [用 coverage 模块提高 Python 开发效率](https://mp.weixin.qq.com/s/fP_mQtQnrssdzOOw6yPzQA)
    * Test with Coverage
    * Mock　

#### [unittest](https://docs.python.org/3/library/unittest.html)

* The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.
* To achieve this, unittest supports some important concepts in an object-oriented way:
* test fixture
    * A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
* test case
    * A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, [TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase), which may be used to create new test cases.
* test suite
    * A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
* test runner
    * A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

##### Command-Line Interface

* How to use ?
    * Discovery: By default, unittest will discover tests (search for test files) in the current directory and its subdirectories.
        * `python -m unittest discover`
    * Run Specific Test Case or Test Method: You can specify a particular test case or test method to run.
        * `python -m unittest test_module.TestCaseName`
        * `python -m unittest test_module.TestCaseName.test_method`
    * Verbose Mode: If you want more detailed output, you can use the -v or --verbose option.
        * `python -m unittest -v test_module`
    * Fail Fast: Using the --failfast option will stop the test run on the first failed test.
        * `python -m unittest --failfast test_module`
    * Catch Breakpoints: With the --pdb option, the test run will enter the post-mortem debugger on test failures or errors.
        * `python -m unittest --pdb test_module`
    * Buffer Output: By using the --buffer option, the output from passing tests will be discarded, and only the output from failing tests will be shown.
        * `python -m unittest --buffer test_module`

##### [Test Discovery](https://docs.python.org/3/library/unittest.html#test-discovery)

* Unittest supports simple test discovery. In order to be compatible with test discovery, all of the test files must be modules or packages importable from the top-level directory of the project (this means that their filenames must be valid identifiers).
* Test discovery is implemented in `TestLoader.discover()`, but can also be used from the command line. The basic command-line usage is:
```py
cd project_directory
python -m unittest discover
```
* `Note As a shortcut, python -m unittest is the equivalent of python -m unittest discover. If you want to pass arguments to test discovery the discover sub-command must be used explicitly.`
* The discover sub-command has the following options:
    * `-v, --verbose`
        * Verbose output
    * `-s, --start-directory directory`
        * Directory to start discovery (. default)
    * `-p, --pattern pattern`
        * Pattern to match test files (`test*.py` default)
    * `-t, --top-level-directory directory`
        * Top level directory of project (defaults to start directory)

##### [Classes and functions](https://docs.python.org/3/library/unittest.html#classes-and-functions)

* This section describes in depth the API of unittest.

###### [Test cases](https://docs.python.org/3/library/unittest.html#test-cases)

* `class unittest.TestCase(methodName='runTest')`
    * Instances of the TestCase class represent the logical test units in the unittest universe. This class is intended to be used as a base class, with specific tests being implemented by concrete subclasses. This class implements the interface needed by the test runner to allow it to drive the tests, and methods that the test code can use to check for and report various kinds of failure.
    * Each instance of TestCase will run a single base method: the method named methodName. In most uses of TestCase, you will neither change the methodName nor reimplement the default runTest() method.
    * Changed in version 3.2: TestCase can be instantiated successfully without providing a methodName. This makes it easier to experiment with TestCase from the interactive interpreter.
    * TestCase instances provide three groups of methods: one group used to run the test, another used by the test implementation to check conditions and report failures, and some inquiry methods allowing information about the test itself to be gathered.
    * Methods in the first group (running the test) are:
    * `setUp()`
        * Method called to prepare the test fixture. This is called immediately before calling the test method; other than AssertionError or SkipTest, any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.
    * `tearDown()`
        * Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than AssertionError or SkipTest, raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the setUp() succeeds, regardless of the outcome of the test method. The default implementation does nothing.
    * `setUpClass()`
        * A class method called before tests in an individual class are run. setUpClass is called with the class as the only argument and must be decorated as a classmethod():
        ```py
        @classmethod
        def setUpClass(cls):
            ...
        ```
    * `tearDownClass()`
        * A class method called after tests in an individual class have run. tearDownClass is called with the class as the only argument and must be decorated as a classmethod():
        ```py
        @classmethod
        def tearDownClass(cls):
            ...
        ```
* The TestCase class provides several assert methods to check for and report failures. The following table lists the most commonly used methods (see the tables below for more assert methods):
* All the assert methods accept a `msg` argument that, if specified, is used as the error message on failure (see also [longMessage](https://docs.python.org/3/library/unittest.html#unittest.TestCase.longMessage)). Note that the msg keyword argument can be passed to assertRaises(), assertRaisesRegex(), assertWarns(), assertWarnsRegex() only when they are used as a context manager.
    * `assertTrue(expr, msg=None)`
    * `assertFalse(expr, msg=None)`
        * Test that expr is true (or false).
        * Note that this is equivalent to `bool(expr) is True` and not to `expr is True` (use `assertIs(expr, True)` for the latter). This method should also be avoided when more specific methods are available (e.g. `assertEqual(a, b)` instead of `assertTrue(a == b)`), because they provide a better error message in case of failure.
* It is also possible to check the production of exceptions, warnings, and log messages using the following methods:
* There are also other methods used to perform more specific checks, such as:
    * `assertGreater(first, second, msg=None)`
    * `assertGreaterEqual(first, second, msg=None)`
    * `assertLess(first, second, msg=None)`
    * `assertLessEqual(first, second, msg=None)`
        * Test that first is respectively >, >=, < or <= than second depending on the method name. If not, the test will fail:
        ```py
        self.assertGreaterEqual(3, 4)
        AssertionError: "3" unexpectedly not greater than or equal to "4"
        ```

##### [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures)

* Class and module level fixtures are implemented in [TestSuite](https://docs.python.org/3/library/unittest.html#unittest.TestSuite). When the test suite encounters a test from a new class then tearDownClass() from the previous class (if there is one) is called, followed by setUpClass() from the new class.
* Similarly if a test is from a different module from the previous test then tearDownModule from the previous module is run, followed by setUpModule from the new module.
* After all the tests have run the final tearDownClass and tearDownModule are run.
* Note that shared fixtures do not play well with `[potential]` features like test parallelization and they break test isolation. They should be used with care.
* The default ordering of tests created by the unittest test loaders is to group all tests from the same modules and classes together. This will lead to setUpClass / setUpModule (etc) being called exactly once per class and module. If you randomize the order, so that tests from different modules and classes are adjacent to each other, then these shared fixture functions may be called multiple times in a single test run.
* Shared fixtures are not intended to work with suites with non-standard ordering. A BaseTestSuite still exists for frameworks that don’t want to support shared fixtures.
* If there are any exceptions raised during one of the shared fixture functions the test is reported as an error. Because there is no corresponding test instance an _ErrorHolder object (that has the same interface as a [TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)) is created to represent the error. If you are just using the standard unittest test runner then this detail doesn’t matter, but if you are a framework author it may be relevant.

###### [setUpClass and tearDownClass](https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass)

* These must be implemented as class methods:
```py
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()
```
* If you want the setUpClass and tearDownClass on base classes called then you must call up to them yourself. The implementations in TestCase are empty.
* If an exception is raised during a setUpClass then the tests in the class are not run and the tearDownClass is not run. Skipped classes will not have setUpClass or tearDownClass run. If the exception is a [SkipTest](https://docs.python.org/3/library/unittest.html#unittest.SkipTest) exception then the class will be reported as having been skipped instead of as an error.

###### [setUpModule and tearDownModule](https://docs.python.org/3/library/unittest.html#setupmodule-and-teardownmodule)

* These should be implemented as functions:
```py
def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()
```
* If an exception is raised in a setUpModule then none of the tests in the module will be run and the tearDownModule will not be run. If the exception is a SkipTest exception then the module will be reported as having been skipped instead of as an error.
* To add cleanup code that must be run even in the case of an exception, use addModuleCleanup:
    * [`unittest.addModuleCleanup(function, /, *args, **kwargs)`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup)
        * Add a function to be called after tearDownModule() to cleanup resources used during the test class. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into addModuleCleanup() when they are added.
        * If setUpModule() fails, meaning that tearDownModule() is not called, then any cleanup functions added will still be called.
        * New in version 3.8.

#### [pytest](https://docs.pytest.org/en/stable/)

* [学习笔记之pytest - 浩然119 - 博客园](https://www.cnblogs.com/pegasus923/p/13769672.html)
	* [5 分钟快速上手 pytest 测试框架](https://mp.weixin.qq.com/s/uOUG5fqHqPWMckCa5WOC4Q)
```python
import pytest

raw_data = read_data(...)

def test_myfunc(*args, **kwargs):
    do_something()
    data = ...
    assert data == raw_data

if __name__ == '__main__':
    pytest.main()
```
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

* [Python 3.11 的速度大幅超越 3.8！](https://mp.weixin.qq.com/s/TULl6EGK708oPbDlf-SkQw)
	* 而 Python 3.11 只用了 31.98 秒，意味着 3 倍的速度提升！
	* Bun 的模拟耗时为 0.768 秒，比 Python 3.11 快 41 倍。相信对于任何熟悉 JavaScript 的人来说，这个结果都在意料之中。JavaScript 是一种 JIT 编译语言，拥有多个出色的运行时。
	* C++ 的模拟耗时为 0.423 秒，比 JavaScript 快 1.8 倍。在我看来，这个数字代表了 Python 之类的语言可以达到的性能“峰值”。
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
* [PyAutoGUI，轻松搞定图片上传！](https://mp.weixin.qq.com/s/-STFI0ajuJiG9fCkmN-srw)
* [用 Python 处理 B 站下载视频](https://mp.weixin.qq.com/s/dCTIUNeDQ_HeZqWQr0hesA)
* [如何用 Python 快速抓取 Google 搜索？](https://mp.weixin.qq.com/s/-GUgWH06Wy7pCzNbMjinXg)
  * https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal
  * https://github.com/getlinksc/scrape_google
* [用 Python 编写一个天气查询应用](https://mp.weixin.qq.com/s/iciMycq-HpwZj-LSE60NQQ)
* [大象装进冰箱要几步？Python 来解答](https://mp.weixin.qq.com/s/S5OWsuY1hT1qATadZ0v_kA)
* [用 Python 制作家用防盗工具](https://mp.weixin.qq.com/s/6RE1fwKF8gndI3Bnhb8UgA)
* [用 Python 制作“除夕夜倒计时”海报](https://mp.weixin.qq.com/s/MIhViQrYOca8QlQ7QEfoZw)
  * https://github.com/wwtm/gitpython_examples
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
* [超实用！整理了34个Python自动化办公库！](https://mp.weixin.qq.com/s/pOqkZ3u39wMxvd6vECZINg)

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
* [一行代码获取股票、基金数据，并绘制K线图](https://mp.weixin.qq.com/s/X_qsurX_DHeOjNWRuy9UQw)
	* 今天这篇文章和大家分享一下如何利用Python获取股票、基金数据，并进行可视化，为金融分析&可视化先导篇
	* 2.3 模块基本介绍与使用
		* 2.3.1 mplfinance
			* 基本介绍：用于金融数据可视化和可视化分析的 matplotlib 实用程序（接口），基于matplotlibe开发，并且与pandas的DataFrame数据有很好的结合。
			* 项目地址：https://github.com/matplotlib/mplfinance
		* 2.3.2 akshare
			* 基本介绍：AKShare 是一个优雅简单的 Python 金融数据接口库，你可以利用这个库轻松获取到金融财经数据。
			* 项目地址：https://github.com/jindaxiang/akshare/
* [如何应用Python助你在股票中获利？](https://mp.weixin.qq.com/s/_EX69-gjN5GHCd0agRIIJA)

#### QUANT

* [Python量化金融都需要用到哪些库？最全汇总](https://mp.weixin.qq.com/s/dZqAroiNV7vIEqtDaIRc0w)
	* [wilsonfreitas/awesome-quant: A curated list of insanely awesome libraries, packages and resources for Quants (Quantitative Finance)](https://github.com/wilsonfreitas/awesome-quant)

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
* What's `.pyd` file ?
    * A `.pyd` file is a compiled binary extension module for Python on Windows. It is equivalent to a `.so` or `.dll` file on other platforms.
    * The `.pyd` extension stands for `Python Dynamic-link Library`. It contains compiled Python code that can be imported into a Python program using the import statement. The `.pyd` file is essentially a shared library that is loaded by the Python interpreter at runtime.
    * To create a `.pyd` file, you typically need to use a C or C++ compiler and link against the Python library. You can use a variety of tools and libraries to help with this, including distutils, setuptools, and Cython.
    * Once you have compiled your extension module into a `.pyd` file, you can distribute it to other users who can then import it into their own Python programs. When your module is imported, Python will automatically load the .pyd file and make its functions and classes available for use.
    * In summary, a `.pyd` file is a compiled binary extension module for Python on Windows, used to provide additional functionality to Python programs.
* How to install and update python ?
	* [How to Install Updated Python 3 on Mac](https://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/)
	* [Download Python | Python.org](https://www.python.org/downloads/)
* How to set pip install package index ?
    * Edit ~/.pip/pip.conf to set index-url / extra-index-url
    * [User Guide — pip 20.2.4 documentation (pypa.io)](https://pip.pypa.io/en/stable/user_guide/#configuration)

### ERROR FIX

* How to fix error `cannot find PyString_Check` in python 3 ?
    * Use `PyUnicode_Check` in Python 3 to replace deprecated `PyString_Check`
    * [py3c reference — py3c 1.4 documentation](https://py3c.readthedocs.io/en/latest/reference.html)
    * [changes for python3 · caqtdm/caqtdm@ba63473](https://github.com/caqtdm/caqtdm/commit/ba634736325789cf3e1408fa679113da7e7c6a33)
* How to fix AttributeError: MyBokeh instance has no attribute 'plot_all' ?
  * Check the indentation for other class member functions prior to plot_all()
* How to fix `ImportError: dynamic module does not define module export function`?
    * [python - Unable to solve "ImportError: dynamic module does not define module export function" - Stack Overflow](https://stackoverflow.com/questions/55277328/unable-to-solve-importerror-dynamic-module-does-not-define-module-export-funct)
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
  * For python2, check if there is /_/_init.py/_/_ under /a
  * Or
  * [python - Relative imports - ModuleNotFoundError: No module named x - Stack Overflow](https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x)
  * [ModuleNotFoundError: No module named x | Towards Data Science](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)
  * first make sure you are using absolute imports
  * export the project’s root directory to PYTHONPATH
```sh
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
```
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

## THIRD PARTY LIBRARIES

* [Python算法实现资源汇总](https://mp.weixin.qq.com/s/1ODoGvRXQ0quk58rVPj4yQ)
  * https://github.com/TheAlgorithms/Python
* [那些有趣/用的 Python 库](https://mp.weixin.qq.com/s/gj6Dn5TLBoz_rqTeqYGduw)
* [140种Python标准库、第三方库和外部工具都有了](https://mp.weixin.qq.com/s/Qp12DRURa2I9AVjQ7gpxVw)
* [介绍几款 Python 类型检查工具](https://mp.weixin.qq.com/s/IvYJkpAmWJ-3ZEHtZzRiCQ)
  * pyright
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

### [Django](https://www.djangoproject.com/)

* Django makes it easier to build better web apps more quickly and with less code.
* [Getting started with Django | Django](https://www.djangoproject.com/start/)
    * [Quick install guide | Django documentation | Django](https://docs.djangoproject.com/en/4.2/intro/install/)
* [Django (web framework) - Wikipedia](https://en.wikipedia.org/wiki/Django_(web_framework))
    * Django (/ˈdʒæŋɡoʊ/ JANG-goh; stylised as django)[4] is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern.[5][6] It is maintained by the Django Software Foundation (DSF), an independent organization established as a 501(c)(3) non-profit.
    * Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself.[7] Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.
    * Some well-known sites that use Django include the Public Broadcasting Service,[8] Instagram,[9] Mozilla,[10] The Washington Times,[11] Disqus,[12] Bitbucket,[13] and Nextdoor.[14] It was used on Pinterest,[15] but later the site moved to a framework built over Flask.
* [学习笔记之Django - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/11556233.html)
* [Python for Web Development – Crash Course [API, SQL Databases, Virtual Environment, Flask, Django] - YouTube](https://www.youtube.com/watch?v=WNvxR8RFzBg&list=WL&index=16)
* [Python Backend Web Development Course (with Django) - YouTube](https://www.youtube.com/watch?v=jBzwzrDvZ18)
    * [Bootstrap Templates | Premium & Free Download | BootstrapMade](https://bootstrapmade.com/)
* [CRM App Development with Django, Python, and MySQL](https://www.freecodecamp.org/news/crm-app-development-with-django-python-and-mysql/)
    * [Django Project – Code a CRM App Tutorial - YouTube](https://www.youtube.com/watch?v=t10QcFx7d5k)
        * [Get started with Bootstrap · Bootstrap v5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
        * [MySQL :: Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
    * https://github.com/flatplanet/Django-CRM
* [Getting Started With Django Tutorial // Build a CRM - YouTube](https://www.youtube.com/watch?v=fOukA4Qh9QA)
    * https://github.com/justdjango/getting-started-with-django
    * [Courses | JustDjango](https://justdjango.com/courses)
    * https://github.com/github/gitignore/blob/main/Python.gitignore
    * [Django - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
        * Beautiful syntax and scoped snippets for perfectionists with deadlines
    * [Django - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=bigonesystems.django)
        * Django Templates and Backend snippets
    * [Django Template - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-html)
        * Django template language support for Visual Studio Code
    * [SQLite - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
        * Explore and query SQLite databases.
    * [Bootstrap · The most popular HTML, CSS, and JS library in the world.](https://getbootstrap.com/)
    * [Tailwind CSS - Rapidly build modern websites without ever leaving your HTML.](https://tailwindcss.com/)
        * [aniftyco/awesome-tailwindcss: 😎 Awesome things related to Tailwind CSS](https://github.com/aniftyco/awesome-tailwindcss)
    * Getting Started
        * To run this project you will need to set your environment variables.
            * Create a new file named `.env` inside the `djcrm` folder
            * Copy all of the variables inside `djcrm/.template.env` and assign your own values to them
            * Run `export READ_DOT_ENV_FILE=True` inside your terminal so that your environment variables file will be read.
```py
$ python3 -m pip install --user virtualenv
$ python3 -m venv env
$ source env/bin/activate
(env) $ which python3
(env) $ pip install django==3.1.4
(env) $ pip freeze > requirements.txt
(env) $ pip install -r requirements.txt
(env) $ django-admin startproject djcrm .
(env) $ python manage.py runserver
(env) $ python manage.py migrate
(env) $ python manage.py makemigrations
(env) $ python manage.py shell
>>> from leads.models import Lead
>>> Lead.objects.all()
(env) $ python manage.py createsuperuser
(env) $ python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.all()
(env) $ deactivate
```

#### [Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)

* [Installation — Django Debug Toolbar 4.1.0 documentation](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

#### [Django documentation](https://docs.djangoproject.com/en/4.2/)

#### MISC

* [网易公开课-上好人生每一课](https://open.163.com/newview/search/%20Django)
    * [Django从入门到实战-.快速创建一个网页-网易公开课](https://open.163.com/newview/movie/free?pid=HEV171PR4&mid=JEV171Q0S)
* [如何轻松了解 Python 必学的 django 框架？](https://mp.weixin.qq.com/s/FpYeYUoED7ii4VJ8F2YzPw)
    * https://docs.djangoproject.com/zh-hans/2.2/ref/contrib/admin/actions/
* [Django 模板语言基础来啦](https://mp.weixin.qq.com/s/aJYsloNye78TZVYzRcFN0A)
* [轻松搞定 Django 模板语言进阶！](https://mp.weixin.qq.com/s/UrQJoGKnrHqRUY238IqdNg)
* [Flask 和 requests 搭建一个简单的API服务](https://mp.weixin.qq.com/s/OAyJ7UdeS-aFWkHWvVUISA)
* [Python 四大主流 Web 编程框架](https://blog.csdn.net/chenqiuge1984/article/details/80127498)
* [用 Django 开发一个 Python Web API](https://mp.weixin.qq.com/s/3-RkHGsl_bPcNKqjXYJyhw)
    * Django 是 Python 编程语言驱动的一个开源模型-视图-控制器（MVC）风格的 Web 应用程序框架。它是Python API开发中最受欢迎的名称之一，自2005年成立以来，其知名度迅速提升。
    * Django由Django软件基金会（Django Software Foundation）维护，并获得了社区的大力支持，在全球拥有11,600多个成员。在Stack Overflow上，Django大约有191,000个带标签的问题。Spotify，YouTube和Instagram等网站都依赖Django进行应用程序和数据管理。
    * 本文演示了使用HTTP协议的GET方法从服务器获取数据的简单API。
    * 建立一个项目
    * 安装Django和Django REST框架
    * 实例化一个新的Django项目
    * 在Django中创建用户
    * 在Django中实现序列化组件和视图层
    * 使用Django生成URL
    * 调整您的Django项目设置
    * 测试您的Django API

### [FastAPI](https://fastapi.tiangolo.com/)

* FastAPI framework, high performance, easy to learn, fast to code, ready for production
* Documentation: https://fastapi.tiangolo.com
* Source Code: https://github.com/fastapi/fastapi
* FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
* The key features are:
    * Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
    * Fast to code: Increase the speed to develop features by about 200% to 300%. *
    * Fewer bugs: Reduce about 40% of human (developer) induced errors. *
    * Intuitive: Great editor support. Completion everywhere. Less time debugging.
    * Easy: Designed to be easy to use and learn. Less time reading docs.
    * Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
    * Robust: Get production-ready code. With automatic interactive documentation.
    * Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.
```shell
$ py -m venv .venv
$ source .venv/Scripts/activate
$ which python
$ pip install "fastapi[standard]"
$ pip list
$ fastapi dev main.py

   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from C:\hao\Documents\GitHub\fastapi

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories: ['C:\\hao\\Documents\\GitHub\\fastapi']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [29064] using WatchFiles
      INFO   Started server process [30044]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
$ uvicorn main:app --reload
```

#### [Learn - FastAPI](https://fastapi.tiangolo.com/learn/)

##### [Python Types Intro](https://fastapi.tiangolo.com/python-types/)

* [Type hints cheat sheet - mypy](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

##### [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)

##### [Advanced User Guide](https://fastapi.tiangolo.com/advanced/)

##### [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/)

##### [Deployment](https://fastapi.tiangolo.com/deployment/)

##### [How To - Recipes](https://fastapi.tiangolo.com/how-to/)

#### [Reference - FastAPI](https://fastapi.tiangolo.com/reference/)

#### [Resources - FastAPI](https://fastapi.tiangolo.com/resources/)

##### [Full Stack FastAPI Template](https://fastapi.tiangolo.com/project-generation/)

* Templates, while typically come with a specific setup, are designed to be flexible and customizable. This allows you to modify and adapt them to your project's requirements, making them an excellent starting point. 🏁
* You can use this template to get started, as it includes a lot of the initial set up, security, database and some API endpoints already done for you.
* GitHub Repository: [Full Stack FastAPI Template](https://github.com/tiangolo/full-stack-fastapi-template)
* Full Stack FastAPI Template - Technology Stack and Features¶
* ⚡ FastAPI for the Python backend API.
* 🧰 SQLModel for the Python SQL database interactions (ORM).
* 🔍 Pydantic, used by FastAPI, for the data validation and settings management.
* 💾 PostgreSQL as the SQL database.
* 🚀 React for the frontend.
* 💃 Using TypeScript, hooks, Vite, and other parts of a modern frontend stack.
* 🎨 Chakra UI for the frontend components.
* 🤖 An automatically generated frontend client.
* 🧪 Playwright for End-to-End testing.
* 🦇 Dark mode support.
* 🐋 Docker Compose for development and production.
* 🔒 Secure password hashing by default.
* 🔑 JWT token authentication.
* 📫 Email based password recovery.
* ✅ Tests with Pytest.
* 📞 Traefik as a reverse proxy / load balancer.
* 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.
* 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.

### [NumPy](http://www.numpy.org/)

* NumPy is the fundamental package for scientific computing with Python.
* [Test Support (numpy.testing) — NumPy v1.20 Manual](https://numpy.org/doc/stable/reference/routines.testing.html)
* [NumPy - Wikipedia](https://en.wikipedia.org/wiki/NumPy)
	* NumPy (pronounced /ˈnʌmpaɪ/ (NUM-py) or sometimes /ˈnʌmpi/[1][2] (NUM-pee)) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. The ancestor of NumPy, Numeric, was originally created by Jim Hugunin with contributions from several other developers. In 2005, Travis Oliphant created NumPy by incorporating features of the competing Numarray into Numeric, with extensive modifications. NumPy is open-source software and has many contributors.
* [NumPy - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/NumPy)
	* NumPy是Python语言的一个扩充程序库。支持高阶大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。NumPy的前身Numeric最早是由Jim Hugunin与其它协作者共同开发，2005年，Travis Oliphant在Numeric中结合了另一个同性质的程序库Numarray的特色，并加入了其它扩展而开发了NumPy。NumPy为开放源代码并且由许多协作者共同维护开发。
* [Numpy详细教程](https://mp.weixin.qq.com/s/MtwGkIhHvcaU-vmC89FfGA)
	* NumPy 是一个 Python 包。 它代表 “Numeric Python”。 它是一个由多维数组对象和用于处理数组的例程集合组成的库。
	* Numeric，即 NumPy 的前身，是由 Jim Hugunin 开发的。 也开发了另一个包 Numarray ，它拥有一些额外的功能。 2005年，Travis Oliphant 通过将 Numarray 的功能集成到 Numeric 包中来创建 NumPy 包。 这个开源项目有很多贡献者。
	* Numpy基础
		* 创建数组
		* 打印数组
		* 基本运算
		* 通用函数(ufunc)
		* 索引，切片和迭代
		* 形状操作
		* 组合(stack)不同的数组
		* 将一个数组分割(split)成几个小数组
		* 视图(view)和浅复制
		* 深复制
		* 函数和方法(method)总览
	* 进阶
		* 广播法则(rule)
		* 花哨的索引和索引技巧
		* 通过数组索引
		* 通过布尔数组索引
		* ix_()函数
		* 线性代数
		* 矩阵类
		* 索引：比较矩阵和二维数组
	* 技巧和提示
		* 向量组合(stacking)
		* 直方图(histogram)
* 盘一盘 Python 系列 2 - NumPy
	* https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247486527&idx=1&sn=6364869cab8d474943a211bd54a828c6&chksm=e8908f36dfe706206fc51c5dd35b9bad6d34f2ce4b4fcf9c188edcb48d093bbf236578342263&scene=21#wechat_redirect
	* https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247486547&idx=1&sn=b3e8816663938f55df8603990c5d42db&chksm=e8908f5adfe7064c8500716ac77e5579077ef186ce9721110cc06c26b11ba7a10b65ea82862a&scene=21#wechat_redirect
* [图解NumPy](https://mp.weixin.qq.com/s/62dmLB-PaVpxregSv7bwTA)
* [NumPy能力大评估：这里有70道测试题](https://mp.weixin.qq.com/s/yKC1_58NP2eMf6gtU6gyrw)
	* https://www.machinelearningplus.com/python/101-numpy-exercises-python/
* [Numpy多维数组基础及运算详解](https://mp.weixin.qq.com/s/iS33g_li_s2kLNqGxS4elg)
* [5个高效&简洁的Numpy函数](https://mp.weixin.qq.com/s/0zxsG0KJqYTMBGRZkz1yMQ)
	* https://towardsdatascience.com/5-smart-python-numpy-functions-dfd1072d2cb4
* [CuPy | 教你一招将Numpy加速700倍？](https://mp.weixin.qq.com/s/lWqJwgWqDoyFsOCkeek8ew)
	* https://towardsdatascience.com/heres-how-to-use-cupy-to-make-numpy-700x-faster-4b920dda1f56
* [快速掌握TensorFlow中张量运算的广播机制](https://mp.weixin.qq.com/s/89DlydoGoiq6x_sFDRfXyA)
* [12 个 Numpy 和 Pandas 函数，提高效率](https://mp.weixin.qq.com/s/kUzvvYcw8qK80R-ASWsIpQ)
	* [12 Amazing Pandas & NumPy Functions | by Kunal Dhariwal | Towards Data Science](https://towardsdatascience.com/12-amazing-pandas-numpy-functions-22e5671a45b8)
	* https://github.com/kunaldhariwal/12-Amazing-Pandas-NumPy-Functions
	* Numpy 的 6 种高效函数
		* argpartition()
		* allclose()
		* clip()
		* extract()
		* where()
		* percentile()
	* Pandas 数据统计包的 6 种高效函数
		* read_csv(nrows=n)
		* map()
		* apply()
		* isin()
		* copy()
		* select_dtypes()

#### [API Reference](https://numpy.org/doc/stable/reference/index.html)

##### [Routines](https://numpy.org/doc/stable/reference/routines.html)

###### [Logic functions](https://numpy.org/doc/stable/reference/routines.logic.html)

* [numpy.isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html)
	* `numpy.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)`
	* Returns a boolean array where two arrays are element-wise equal within a tolerance.
	* The tolerance values are positive, typically very small numbers. The relative difference (rtol * abs(b)) and the absolute difference atol are added together to compare against the absolute difference between a and b.
* [numpy.equal](https://numpy.org/doc/stable/reference/generated/numpy.equal.html)
	* `numpy.equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'equal'>`
	* Return (x1 == x2) element-wise.
* [numpy.not_equal](https://numpy.org/doc/stable/reference/generated/numpy.not_equal.html)
	* `numpy.not_equal(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'not_equal'>`
	* Return (x1 != x2) element-wise.

#### FAQ

* How to calculate distance between two points ?
	* dist = numpy.linalg.norm(a-b)
	* [python - How can the euclidean distance be calculated with numpy? - Stack Overflow](https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy)
	* [numpy.linalg.norm — NumPy v1.9 Manual](https://docs.scipy.org/doc/numpy-1.9.3/reference/generated/numpy.linalg.norm.html)
* How to calculate angle from velocity ?
	* [2d - Calculating the angular direction from velocity - Game Development Stack Exchange](https://gamedev.stackexchange.com/questions/17340/calculating-the-angular-direction-from-velocity)
		* angle = atan2 (vy,vx)
	* [Radian - Wikipedia](https://en.wikipedia.org/wiki/Radian)
		* The radian (SI symbol rad) is the SI unit for measuring angles, and is the standard unit of angular measure used in many areas of mathematics. The length of an arc of a unit circle is numerically equal to the measurement in radians of the angle that it subtends; one radian is just under 57.3 degrees (expansion at OEIS A072097). The unit was formerly an SI supplementary unit, but this category was abolished in 1995 and the radian is now considered an SI derived unit.
	* [numpy.arctan2 — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html#numpy.arctan2)
		* Element-wise arc tangent of x1/x2 choosing the quadrant correctly.
		* The quadrant (i.e., branch) is chosen so that arctan2(x1, x2) is the signed angle in radians between the ray ending at the origin and passing through the point (1,0), and the ray ending at the origin and passing through the point (x2, x1). (Note the role reversal: the “y-coordinate” is the first function parameter, the “x-coordinate” is the second.) By IEEE convention, this function is defined for x2 = +/-0 and for either or both of x1 and x2 = +/-inf (see Notes for specific values).
		* This function is not defined for complex-valued arguments; for the so-called argument of complex values, use angle.
		* angle = np.arctan2(vy, vx) * 180 / np.pi
* How to use conditional statement on array ?
	* [(Python) How to use conditional statements on every element of array using [:] syntax? - Stack Overflow](https://stackoverflow.com/questions/45848612/python-how-to-use-conditional-statements-on-every-element-of-array-using-s))
	```python
	all(i == 0 for i in a)
	a[a > 1] = 1
	map(lambda x: 1 if x==0 else x, a)
	a = np.where(a == 0, 1, a)
	```
	* [python - Function of Numpy Array with if-statement - Stack Overflow](https://stackoverflow.com/questions/8036878/function-of-numpy-array-with-if-statement)
		* vfunc = vectorize(func)
	* [numpy.array — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html?highlight=array#numpy.array)
		* numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
	* [numpy.where — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html?highlight=numpy%20where#numpy.where)
		* Return elements, either from x or y, depending on condition.
		* If only condition is given, return condition.nonzero().
	* [numpy.vectorize — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html)
		* class numpy.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)
		* Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs and returns an single or tuple of numpy array as output. The vectorized function evaluates pyfunc over successive tuples of the input arrays like the python map function, except it uses the broadcasting rules of numpy.
		* The data type of the output of vectorized is determined by calling the function with the first element of the input. This can be avoided by specifying the otypes argument.
* How to convert array into string ?
	* [numpy.array_str — NumPy v1.9 Manual](http://memobio2015.u-strasbg.fr/conference/FICHIERS/Documentation/doc-numpy-html/reference/generated/numpy.array_str.html)
* How to compare ?
	* [numpy.maximum — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.maximum.html)
		* numpy.maximum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'maximum'>
	* [numpy.minimum — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.minimum.html)
		* numpy.minimum(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'minimum'>
	* [numpy.nanmax — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.nanmax.html)
		* numpy.nanmax(a, axis=None, out=None, keepdims=</no value>)
	* [numpy.nanmin — NumPy v1.15 Manual](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.nanmin.html)
		* numpy.nanmin(a, axis=None, out=None, keepdims=</no value>)
	* Constants — NumPy v1.15 Manual
		* [numpy.inf](https://docs.scipy.org/doc/numpy-1.15.1/reference/constants.html?highlight=numpy%20nan#numpy.inf)
		* [numpy.nan](https://docs.scipy.org/doc/numpy-1.15.1/reference/constants.html?highlight=numpy%20nan#numpy.nan)
* How to compare list of numpy arrays ?
	* [How to compare list of arrays in python? - Stack Overflow](https://stackoverflow.com/questions/30773670/how-to-compare-list-of-arrays-in-python)
	```python
	a = [np.array([1, 2, 3]), np.array([1, 2, 3])]
	b = [np.array([1, 2, 3]), np.array([1, 2, 3])]
	all([np.allclose(x, y) for x, y in zip(a, b)]) #True
	```
	* [numpy.all — NumPy v1.20 Manual](https://numpy.org/doc/stable/reference/generated/numpy.all.html)
		* numpy.all(a, axis=None, out=None, keepdims=</no value>, *, where=</no value>)
		* Test whether all array elements along a given axis evaluate to True.
	* [numpy.allclose — NumPy v1.20 Manual](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)
		* numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
		* Returns True if two arrays are element-wise equal within a tolerance.
* How to collapse array into one dimension ?
	```python
	a.reshape(-1)
	a.flatten()
	```
	* [numpy.reshape — NumPy v1.20 Manual](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
	* [numpy.ndarray.flatten — NumPy v1.20 Manual](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)

### [pandas](https://pandas.pydata.org/)

* `Python Data Analysis Library`
* pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* [pandas: powerful Python data analysis toolkit — pandas 0.22.0 documentation](http://pandas.pydata.org/pandas-docs/stable/index.html)
* [10 Minutes to pandas — pandas 0.22.0 documentation](http://pandas.pydata.org/pandas-docs/stable/10min.html#)
	* This is a short introduction to pandas, geared mainly for new users. You can see more complex recipes in the Cookbook
* [pandas · GitHub](https://github.com/pandas-dev)
	* Powerful data manipulation tools for Python
* [pandas (software) - Wikipedia](https://en.wikipedia.org/wiki/Pandas_(software))
	* In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. It is free software released under the three-clause BSD license. The name is derived from the term "panel data", an econometrics term for data sets that include observations over multiple time periods for the same individuals.
* [pandas_百度百科](https://baike.baidu.com/item/pandas)
	* Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。
* [学习笔记之pandas Foundations | DataCamp - Pegasus923 - 博客园](https://www.cnblogs.com/pegasus923/p/9017799.html)
* [资源 | 23种Pandas核心操作，你需要过一遍吗？ - 机器学习算法与Python学习](https://mp.weixin.qq.com/s/klGFyKngYnwZYfhhLne8Sg)
	* https://towardsdatascience.com/23-great-pandas-codes-for-data-scientists-cca5ed9d8a38
	* Pandas 是一个 Python 软件库，它提供了大量能使我们快速便捷地处理数据的函数和方法。一般而言，Pandas 是使 Python 成为强大而高效的数据分析环境的重要因素之一。在本文中，作者从基本数据集读写、数据处理和 DataFrame 操作三个角度展示了 23 个 Pandas 核心方法。
* [Python 数据处理库 pandas 入门教程 - 数据分析与开发](https://mp.weixin.qq.com/s/Qd9lqngAiD2AYVLvV54Xwg)
	* pandas是一个Python语言的软件包，在我们使用Python语言进行机器学习编程的时候，这是一个非常常用的基础编程库。本文是对它的一个入门教程。
	* pandas提供了快速，灵活和富有表现力的数据结构，目的是使“关系”或“标记”数据的工作既简单又直观。它旨在成为在Python中进行实际数据分析的高级构建块。
	* 入门介绍
	* 核心数据结构
	* Series
	* DataFrame
	* Index对象与数据访问
	* 文件操作
	* 读取Excel文件
	* 读取CSV文件
	* 处理无效值
	* 忽略无效值
	* 替换无效值
	* 处理字符串
* [Python 数据处理库 pandas 进阶教程 - 数据分析与开发](https://mp.weixin.qq.com/s/_8b5sdvpMVR_M0XuEezrOQ)
	* 数据访问
		* 基础方法：[]和.
		* loc与iloc
		* at与iat
	* Index对象
		* MultiIndex
	* 数据整合
		* Concat与Append
		* Merge与Join
	* 数据集合和分组操作
	* 时间相关
	* 图形展示
* [Python Pandas Functions in Parallel - Data and Stuff by Jay](http://www.racketracer.com/2016/07/06/pandas-in-parallel/)
	* I’m always on the lookout for quick hacks and code snippets that might help improve efficiency. Most of the time that’s through stackoverflow but here’s one that deals with parallelization and efficiency that I thought would be helpful.
	* Since Pandas doesn’t have an internal parallelism feature yet, it makes doing apply functions with huge datasets a pain if the functions have expensive computation times. One way to shorten that amount of time is to split the dataset into separate pieces, perform the apply function, and then re-concatenate the pandas dataframes.
* [Pandas核心操作](https://mp.weixin.qq.com/s/2a_xS-BuPOpNCw3ZNZuYnQ)
* [【精选】Pandas一站式教程！](https://mp.weixin.qq.com/s/c02KHqLsI5i1xKE_DnwVVw)
	* https://towardsdatascience.com/be-a-more-efficient-data-scientist-today-master-pandas-with-this-guide-ea362d27386
* 盘一盘 Python 系列 4 - Pandas
	* https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247486680&idx=1&sn=ee79e798cb2c00ff4dd02609ca9c494d&chksm=e8908fd1dfe706c71f998ceec4e8c6a44a76778b8382313a5f773319765e8b1116bf3dbbeeec&scene=21#wechat_redirect
	* https://mp.weixin.qq.com/s?__biz=MzIzMjY0MjE1MA==&mid=2247486784&idx=1&sn=50a54067e9d596d4a03beb2b281167fb&chksm=e8908e49dfe7075f3cb3b1d5ef9b6ad149c63d3e33a8a42e503717ed09d82df7aa71e87c1eb1&scene=21#wechat_redirect

#### [API reference](https://pandas.pydata.org/docs/reference/index.html)

##### [Input/output](https://pandas.pydata.org/pandas-docs/stable/reference/io.html#input-output)

* [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv)
	* `pandas.read_csv(filepath_or_buffer, sep=NoDefault.no_default, delimiter=None, header='infer', names=NoDefault.no_default, index_col=None, usecols=None, squeeze=None, prefix=NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)`
	* Read a comma-separated values (csv) file into DataFrame.
	* Also supports optionally iterating or breaking of the file into chunks.
	* Additional help can be found in the online docs for IO Tools.
* [pandas.ExcelWriter](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter)
	* `class pandas.ExcelWriter(path, engine=None, date_format=None, datetime_format=None, mode='w', storage_options=None, if_sheet_exists=None, engine_kwargs=None, **kwargs)`
	* Class for writing DataFrame objects into excel sheets.

##### [General functions](https://pandas.pydata.org/pandas-docs/stable/reference/general_functions.html)

* [pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat)
	* `pandas.concat(objs, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=True)`
	* Concatenate pandas objects along a particular axis with optional set logic along the other axes.
	* Can also add a layer of hierarchical indexing on the concatenation axis, which may be useful if the labels are the same (or overlapping) on the passed axis number.
* How to concat dataframe without duplicates ?
	* [Pandas/Python: How to concatenate two dataframes without duplicates? - Stack Overflow](https://stackoverflow.com/questions/21317384/pandas-python-how-to-concatenate-two-dataframes-without-duplicates)
```python
pandas.concat([df1,df2]).drop_duplicates().reset_index(drop=True)
```
* [pandas.unique](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.unique.html#pandas.unique)
	* Return unique values based on a hash table.
	* Uniques are returned in order of appearance. This does NOT sort.
	* Significantly faster than numpy.unique for long enough sequences. Includes NA values.
	* How to find unique value in a column of dataframe ?
		* List Unique Values In A pandas Column
			* https://chrisalbon.com/python/data_wrangling/pandas_list_unique_values_in_column/
* [pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
	* `pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=True)`
	* Convert argument to datetime.
	* This function converts a scalar, array-like, Series or DataFrame/dict-like to a pandas datetime object.
* How to calculate time differences in seconds ?
	* [Time Deltas](https://pandas.pydata.org/pandas-docs/stable/timedeltas.html#attributes)
		* Timedeltas are differences in times, expressed in difference units, e.g. days, hours, minutes, seconds. They can be both positive and negative.
		* Timedelta is a subclass of datetime.timedelta, and behaves in a similar manner, but allows compatibility with np.timedelta64 types as well as a host of custom representation, parsing, and attributes.
		* You can access various components of the Timedelta or TimedeltaIndex directly using the attributes days,seconds,microseconds,nanoseconds. These are identical to the values returned by datetime.timedelta, in that, for example, the .seconds attribute represents the number of seconds >= 0 and < 1 day. These are signed according to whether the Timedelta is signed.
	* [pandas.Timedelta.total_seconds](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Timedelta.total_seconds.html)
		* Total duration of timedelta in seconds (to ns precision)
	* [Time Series / Date functionality](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#)
	* [python - Calculate Pandas DataFrame Time Difference Between Two Columns in Hours and Minutes - Stack Overflow](https://stackoverflow.com/questions/22923775/calculate-pandas-dataframe-time-difference-between-two-columns-in-hours-and-minu)
		* `.total_seconds()`
	* [pandas.Series.dt.second](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.second.html)
		* The seconds of the datetime
```python
value = pd.to_datetime(end_timestamp) - pd.to_datetime(start_timestamp)).total_seconds()
df['duration'] = (df['end_timestamp'] - df['start_timestamp']).dt.seconds
```

##### [Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

###### [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

* `class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)`
* One-dimensional ndarray with axis labels (including time series).
* Labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).
* Operations between Series (+, -, /, *, \**) align values based on their associated index values– they need not be the same length. The result index will be the sorted union of the two indexes.
* [pandas.Series.tolist](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.tolist.html)
	* Return a list of the values.
	* These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)
	* Returns
		* list
* [How to Convert Pandas DataFrame into a List - Data to Fish](https://datatofish.com/convert-pandas-dataframe-to-list/)
	* `df.values.tolist()`

###### [Attributes](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#attributes)

* [pandas.Series.values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.values.html)
	* Return Series as ndarray or ndarray-like depending on the dtype.

###### [Computations / descriptive stats](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#computations-descriptive-stats)

* [pandas.Series.unique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html#pandas.Series.unique)
	* Return unique values of Series object.
	* Uniques are returned in order of appearance. Hash table-based unique, therefore does NOT sort.
	* Returns
		* ndarray or ExtensionArray
			* The unique values returned as a NumPy array. See Notes.
	* Notes
		* Returns the unique values as a NumPy array. In case of an extension-array backed Series, a new ExtensionArray of that type with just the unique values is returned. This includes
			* Categorical
			* Period
			* Datetime with Timezone
			* Interval
			* Sparse
			* IntegerNA
* How to merge two pandas.Series.unique() ?
	* [numpy.append](https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html)
		* Append values to the end of an array.
		* `np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])`

###### [Missing data handling](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#missing-data-handling)

* [pandas.Series.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.fillna.html#pandas.Series.fillna)
	* `Series.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)`
	* Fill NA/NaN values using the specified method.

###### [Reshaping, sorting](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#reshaping-sorting)

* [pandas.Series.searchsorted](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.searchsorted.html#pandas.Series.searchsorted)
	* `Series.searchsorted(value, side='left', sorter=None)`
	* Find indices where elements should be inserted to maintain order.
	* Find the indices into a sorted Series self such that, if the corresponding elements in value were inserted before the indices, the order of self would be preserved.
* How to find index where elements should be inserted to maintain order ?
	* [pandas.Index.searchsorted](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.searchsorted.html?highlight=searchsorted#pandas.Index.searchsorted)
		* `Index.searchsorted(value, side='left', sorter=None)`
	* Essential Basic Functionality — pandas 0.23.3 documentation
		* http://pandas.pydata.org/pandas-docs/stable/basics.html#searchsorted
	* Cookbook — pandas 0.23.3 documentation
		* http://pandas.pydata.org/pandas-docs/stable/cookbook.html?highlight=searchsorted#merge
	* python - Pandas merge with logic - Stack Overflow
		* https://stackoverflow.com/questions/25125626/pandas-merge-with-logic/2512764

##### [DataFrame](https://pandas.pydata.org/docs/reference/frame.html)

###### [Constructor](https://pandas.pydata.org/docs/reference/frame.html#constructor)

* [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)
	* Two-dimensional, size-mutable, potentially heterogeneous tabular data.
	* `class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)`
* [How to create an empty DataFrame and append rows & columns to it in Pandas? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-create-an-empty-dataframe-and-append-rows-columns-to-it-in-pandas/)
	* `df = pd.DataFrame()`

###### [Attributes and underlying data](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#attributes-and-underlying-data)

* [pandas.DataFrame.index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index)
	* The index (row labels) of the DataFrame.
	* How to get count of rows in dataframe ?
		* [len - Built-in Functions — Python 3.7.2 documentation](https://docs.python.org/3/library/functions.html#len)
			* Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
		* [pandas python how to count the number of records or rows in a dataframe - Stack Overflow](https://stackoverflow.com/questions/17468878/pandas-python-how-to-count-the-number-of-records-or-rows-in-a-dataframe/41968240)
			* To get the number of rows in a dataframe use:
			* df.shape[0]
			* (and df.shape[1] to get the number of columns).
			* As an alternative you can use
			* len(df)
			* or
			* len(df.index)
			* (and len(df.columns) for the columns)
			* shape is more versatile and more convenient than len(), especially for interactive work (just needs to be added at the end), but len is a bit
			faster
			* To avoid: count() because it returns the number of non-NA/null observations over requested axis
			* len(df.index) is faster
```python
len( df )
```
* [pandas.DataFrame.columns](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html)
	* How to check if a dataframe column exists ?
		* [python - How to check if a column exists in Pandas - Stack Overflow](https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas)
```python
if 'A' in df.columns:
```
* How to get all column names of a dataframe?
```python
list( df )
```
* How to get a specific column as series / dataframe ?
```python
# series
df[ 'col1' ] / df.col1
df[ [c for c in df.columns if c.startswith('a')][0] ]
# dataframe
df[ [ 'col1' ] ]
df[ [c for c in df.columns if c.startswith('a')] ]
# Choosing columns in pandas DataFrame – Kasia Rachuta – Medium
# https://medium.com/@kasiarachuta/choosing-columns-in-pandas-dataframe-d0677b34a6ca
df[ 'col1' ]
# This command picks a column and returns it as a Series
df[ [ 'col1' ] ]
# Here, I chose the column and I get a DataFrame
```
* [pandas.DataFrame.info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info)
	* `DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None, null_counts=None)`
	* Print a concise summary of a DataFrame.
	* This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.
* Dataframe information ?
	* [pandas.DataFrame.describe](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html#pandas.DataFrame.describe)
		* `DataFrame.describe(percentiles=None, include=None, exclude=None)`
* [pandas.DataFrame.empty](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html)
	* How to check if a dataframe column / serie is empty ?
		* [python - How to check if pandas Series is empty? - Stack Overflow](https://stackoverflow.com/questions/24652417/how-to-check-if-pandas-series-is-empty)
```python
df.empty
df.dropna().empty
```

###### [Conversion](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#conversion)

* [pandas.DataFrame.astype](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html)
	* `DataFrame.astype(dtype, copy=True, errors='raise')`
	* Cast a pandas object to a specified dtype dtype.
* How to convert series to int ?
	* [python - Cannot convert the series to <class 'int'> - Stack Overflow](https://stackoverflow.com/questions/51865367/cannot-convert-the-series-to-class-int)
		* `df['intage'] = df['age'].astype(int)`
	* [python - convert pandas float series to int - Stack Overflow](https://stackoverflow.com/questions/34145190/convert-pandas-float-series-to-int)
* [pandas.DataFrame.copy](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy)
	* `DataFrame.copy(deep=True)`
	* Make a copy of this object’s indices and data.
	* When deep=True (default), a new object will be created with a copy of the calling object’s data and indices. Modifications to the data or indices of the copy will not be reflected in the original object (see notes below).
	* When deep=False, a new object will be created without copying the calling object’s data or index (only references to the data and index are copied). Any changes to the data of the original will be reflected in the shallow copy (and vice versa).
	* Parameters
		* deep : bool, default True
			* Make a deep copy, including a copy of the data and the indices. With deep=False neither the indices nor the data are copied.
	* Returns
		* copy : Series or DataFrame
			* Object type matches caller.
	* Notes
		* When deep=True, data is copied but actual Python objects will not be copied recursively, only the reference to the object. This is in contrast to copy.deepcopy in the Standard Library, which recursively copies object data (see examples below).
		* While Index objects are copied when deep=True, the underlying numpy array is not copied for performance reasons. Since Index is immutable, the underlying data can be safely shared and a copy is not needed.
* How to create / copy a dataframe without data ?
	* `df_others = pd.DataFrame(data=None, columns=df_source.columns, index=df_source.index)`
		* It preserves columns, index, and replace all data with NaN, but with object dtypes
	* `df_others = pd.DataFrame().reindex_like(df)`
		* It preserves columns, index, and replace all data with NaN, but with float64 dtypes
	* `df_others = df.copy()[:0]`
		* It preserves columns and dtypes, but without index and data
	* python - Is there a way to copy only the structure (not the data) of a Pandas DataFrame? - Stack Overflow
		* https://stackoverflow.com/questions/27467730/is-there-a-way-to-copy-only-the-structure-not-the-data-of-a-pandas-dataframe
	* pandas.DataFrame — pandas 0.23.4 documentation
		* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame
	* pandas.DataFrame.copy — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.copy.html
	* pandas.DataFrame.reindex_like — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex_like.html
	* Indexing and Selecting Data — pandas 0.23.4 documentation
		*	https://pandas.pydata.org/pandas-docs/stable/indexing.html#slicing-ranges

###### [Indexing, iteration](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#indexing-iteration)

* [pandas.DataFrame.iat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat)
	* Access a single value for a row/column pair by integer position.
	* Similar to iloc, in that both provide integer-based lookups. Use iat if you only need to get or set a single value in a DataFrame or Series.
* How to get scalar value of a panel with condition ?
	* [python - How to get scalar value on a cell using conditional indexing - Stack Overflow](https://stackoverflow.com/questions/30813088/how-to-get-scalar-value-on-a-cell-using-conditional-indexing)
		* get at the underlying numpy matrix using .values on a series or dataframe
```python
id = df.loc[a==b, 'id'].values[0]
id = df[a==b]['id'].iat[0]
```
* [pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
	* Access a group of rows and columns by label(s) or a boolean array.
	* .loc[] is primarily label based, but may also be used with a boolean array.
	* Allowed inputs are:
		* A single label, e.g. 5 or 'a', (note that 5 is interpreted as a label of the index, and never as an integer position along the index).
		* A list or array of labels, e.g. ['a', 'b', 'c'].
		* A slice object with labels, e.g. 'a':'f'.
			* Warning
				* Note that contrary to usual python slices, both the start and the stop are included
		* A boolean array of the same length as the axis being sliced, e.g. [True, False, True].
		* An alignable boolean Series. The index of the key will be aligned before masking.
		* An alignable Index. The Index of the returned selection will be the input.
		* A callable function with one argument (the calling Series or DataFrame) and that returns valid output for indexing (one of the above)
	* How to query a specified column / panel ?
		* [Indexing and Selecting Data](http://pandas.pydata.org/pandas-docs/stable/indexing.html#different-choices-for-indexing)
```python
# Slice with labels for row and single label for column.
# As mentioned above, note that both the start and stop of the slice are included.
df.loc['cobra':'viper', 'max_speed']
```
* How to look up the first match element ?
	* python - lookup first match in Pandas dataframe - Stack Overflow
		* https://stackoverflow.com/questions/46371391/lookup-first-match-in-pandas-dataframe
	* pandas.Series.item — pandas 0.23.1 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.item.html
	* pandas.DataFrame.iat — pandas 0.23.1 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iat.html
	* pandas.DataFrame.empty — pandas 0.23.1 documentation
		* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.empty.html?highlight=pandas%20dataframe%20empty#pandas-dataframe-empty
```python
westcoast.loc[westcoast.state=='Oregon', 'capital'].item()
s = westcoast.loc[westcoast.state=='Oregon', 'capital']
s = np.nan if s.empty else s.iat[0]
```

###### [Function application, GroupBy & window](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#function-application-groupby-window)

* [pandas.DataFrame.apply](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)
	* `DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)`
	* Apply a function along an axis of the DataFrame.
	* Objects passed to the function are Series objects whose index is either the DataFrame’s index (axis=0) or the DataFrame’s columns (axis=1). By default (result_type=None), the final return type is inferred from the return type of the applied function. Otherwise, it depends on the result_type argument.
	* How to create a new column with applying function on the existing columns ?
```python
df['new'] = df.apply(lambda x : myfunc(x['old']), axis='columns')
```
* [pandas.DataFrame.groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby)
	* `DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=NoDefault.no_default, observed=False, dropna=True)`
	* Group DataFrame using a mapper or by a Series of columns.
	* A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.
	* Parameters
		* by : mapping, function, label, or list of labels
			* Used to determine the groups for the groupby. If by is a function, it’s called on each value of the object’s index. If a dict or Series is passed, the Series or dict VALUES will be used to determine the groups (the Series’ values are first aligned; see .align() method). If a list or ndarray of length equal to the selected axis is passed (see the groupby user guide), the values are used as-is to determine the groups. A label or list of labels may be passed to group by the columns in self. Notice that a tuple is interpreted as a (single) key.
		* axis : {0 or ‘index’, 1 or ‘columns’}, default 0
			* Split along rows (0) or columns (1).
		* level : int, level name, or sequence of such, default None
			* If the axis is a MultiIndex (hierarchical), group by a particular level or levels.
		* as_index : bool, default True
			* For aggregated output, return object with group labels as the index. Only relevant for DataFrame input. as_index=False is effectively “SQL-style” grouped output.
		* sort : bool, default True
			* Sort group keys. Get better performance by turning this off. Note this does not influence the order of observations within each group. Groupby preserves the order of rows within each group.
		* group_keys : bool, default True
			* When calling apply, add group keys to index to identify pieces.
		* observed : bool, default False
			* This only applies if any of the groupers are Categoricals. If True: only show observed values for categorical groupers. If False: show all values for categorical groupers.
		* dropna : bool, default True
			* If True, and if group keys contain NA values, NA values together with row/column will be dropped. If False, NA values will also be treated as the key in groups.
			* New in version 1.1.0.
	* Returns
		* DataFrameGroupBy
			* Returns a groupby object that contains information about the groups.
* How to group by ?
	* Group By: split-apply-combine — pandas 0.23.0 documentation
		* https://pandas.pydata.org/pandas-docs/stable/groupby.html
* How to extract features by grouping columns ?
	* 19 Essential Snippets in Pandas - 16. Extracting Features by Grouping Columns
		* https://jeffdelaney.me/blog/useful-snippets-in-pandas/
		* `df.groupby('topping')['discount'].apply(lambda x: np.mean(x))`
	* pandas.Series.rename — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.rename.html
		* `Series.rename(index=None, **kwargs)`
```python
df_mean = (df.groupby('id').col.mean().rename('mean_col'))
```
* How to groupby and sum ?
	* python - Pandas group-by and sum - Stack Overflow
	* https://stackoverflow.com/questions/39922986/pandas-group-by-and-sum
```python
df.groupby(['Name']).sum()
```
* [pandas.DataFrame.rolling](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling)
	* `DataFrame.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None, method='single')`
	* Provides rolling window calculations.
	* Parameters
		* window : int, offset, or BaseIndexer subclass
			* Size of the moving window.
			* If an integer, the fixed number of observations used for each window.
			* If an offset, the time period of each window. Each window will be a variable sized based on the observations included in the time-period. This is only valid for datetimelike indexes. To learn more about the offsets & frequency strings, please see this link.
			* If a BaseIndexer subclass, the window boundaries based on the defined get_window_bounds method. Additional rolling keyword arguments, namely min_periods, center, and closed will be passed to get_window_bounds.
* How to calculate average value in the last minutes ?
	* pandas.DatetimeIndex — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DatetimeIndex.html
	* pandas.DataFrame.set_index — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html
		* `DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)`
		* Set the DataFrame index (row labels) using one or more existing columns. By default yields a new object.
	* pandas.Series.mean — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.mean.html#pandas-series-mean
		* `Series.mean(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)`
		* Return the mean of the values for the requested axis
	* python - Pandas Set DatetimeIndex - Stack Overflow
		* https://stackoverflow.com/questions/17328655/pandas-set-datetimeindex
```python
df.set_index(pd.DatetimeIndex(df['timestamp']), inplace=True)
df['average'] = df_sub_speed['num'].rolling('5min').mean()
df.reset_index(drop=True, inplace=True)
```

###### [Computations / descriptive stats](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats)

* [pandas.DataFrame.cumsum](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)
	* `DataFrame.cumsum(axis=None, skipna=True, *args, **kwargs)`
	* Return cumulative sum over a DataFrame or Series axis.
	* Returns a DataFrame or Series of the same size containing the cumulative sum.
* [pandas.DataFrame.max](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html)
	* `DataFrame.max(axis=_NoDefault.no_default, skipna=True, level=None, numeric_only=None, **kwargs)`
	* Return the maximum of the values over the requested axis.

###### [Reindexing / selection / label manipulation](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#reindexing-selection-label-manipulation)

* [pandas.DataFrame.drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)
	* `DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')`
	* Drop specified labels from rows or columns.
	* Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level. See the user guide <advanced.shown_levels> for more information about the now unused levels.
* How to delete rows from dataframe permanently ?
	* [How to Delete a Row from a Pandas Dataframe Object in Python ?](http://www.learningaboutelectronics.com/Articles/How-to-delete-a-row-from-a-pandas-dataframe-object-in-Python.php)
		* `dataframe1.drop('D', inplace=True)`
* How to drop columns with specified names / list ?
	* pandas.DataFrame.rename — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html
		* `DataFrame.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None)`
	* Built-in Types — Python 3.7.1 documentation - str.startswith(prefix[, start[, end]])
		* https://docs.python.org/3/library/stdtypes.html#str.startswith
		* Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
	* python - Pandas dataframe: drop columns whose name contains a specific string - Stack Overflow
		* https://stackoverflow.com/questions/19071199/pandas-dataframe-drop-columns-whose-name-contains-a-specific-string
	* python - Check if multiple strings exist in another string - Stack Overflow
		* https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
		* You can use any: if any(x in str for x in a):
		* Similarly to check if all the strings from the list are found, use all instead of any.
```python
cols = [c for c in df.columns if not c.startswith( ('col1', 'col2') ) ]
cols = [c for c in df.columns if not any( f in c for f in list_f ) ]
df = df[cols]
```
* [pandas.DataFrame.drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates)
	* `DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)`
	* Return DataFrame with duplicate rows removed.
	* Considering certain columns is optional. Indexes, including time indexes are ignored.
	* `grouped = grouped.drop_duplicates(['A', 'B'])`
* How to drop duplicates ?
	* [Drop all duplicate rows in Python Pandas - Stack Overflow](https://stackoverflow.com/questions/23667369/drop-all-duplicate-rows-in-python-pandas)
		* Note that it will drop all duplicates. So an issue will occur if you just want to drop consecutive duplicates.
* [pandas.DataFrame.reset_index](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html)
	* `DataFrame.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')`
	* Reset the index, or a level of it.
	* Reset the index of the DataFrame, and use the default one instead. If the DataFrame has a MultiIndex, this method can remove one or more levels.
	* Parameters
		* level : int, str, tuple, or list, default None
			* Only remove the given levels from the index. Removes all levels by default.
		* drop : bool, default False
			* Do not try to insert index into dataframe columns. This resets the index to the default integer index.
		* inplace : bool, default False
			* Modify the DataFrame in place (do not create a new object).
		* col_level : int or str, default 0
			* If the columns have multiple levels, determines which level the labels are inserted into. By default it is inserted into the first level.
		* col_fill : object, default ‘’
			* If the columns have multiple levels, determines how the other levels are named. If None then the index name is repeated.
	* Returns
		* DataFrame or None
		* DataFrame with the new index or None if inplace=True.
* [pandas.DataFrame.tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail)
	* `DataFrame.tail(n=5)`
	* Return the last n rows.
	* This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.
	* For negative values of n, this function returns all rows except the first n rows, equivalent to df[n:].
* How to get the last row / value of dataframe ?
	* How to get the last n row of pandas dataframe? - Stack Overflow
		* https://stackoverflow.com/questions/14663004/how-to-get-the-last-n-row-of-pandas-dataframe
	```python
	df.iloc[ -1 ]
	df.tail( 1 )
	```
	* pandas.DataFrame.iloc — pandas 0.23.3 documentation
		* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc
	* [python - obtaining last value of dataframe column without index - Stack Overflow](https://stackoverflow.com/questions/34166030/obtaining-last-value-of-dataframe-column-without-index)
		* `df.column.iat[ -1 ]`
	* Indexing and Selecting Data — pandas 0.23.3 documentation
		* http://pandas.pydata.org/pandas-docs/stable/indexing.html#fast-scalar-value-getting-and-setting
	* python - Loc vs. iloc vs. ix vs. at vs. iat? - Stack Overflow
		* https://stackoverflow.com/questions/28757389/loc-vs-iloc-vs-ix-vs-at-vs-iat
		* loc - label based
		* iloc - position based
		* at: get scalar values. It's a very fast loc
		* iat: Get scalar values. It's a very fast iloc

###### [Missing data handling](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#missing-data-handling)

* [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html#pandas-dataframe-dropna)
	* `DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)`
	* Remove missing values.
* [pandas.DataFrame.fillna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna)
	* `DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)`
	* Fill NA/NaN values using the specified method.
* How to work with missing data ?
	* Working with missing data — pandas 0.23.4 documentation
		* http://pandas.pydata.org/pandas-docs/stable/missing_data.html?highlight=fill#working-with-missing-data
	* pandas.Timestamp.min — pandas 0.23.4 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Timestamp.min.html
		* `Timestamp.min = Timestamp('1677-09-21 00:12:43.145225')`
```python
df['col'].fillna(pandas.Timestamp.min)
cols = [c for c in df.columns if 'a' in c]
df[cols] = df[cols].fillna( df[cols].mean() )
```
* [pandas.DataFrame.isna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna)
	* Detect missing values.
	* Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, gets mapped to True values. Everything else gets mapped to False values. Characters such as empty strings '' or numpy.inf are not considered NA values (unless you set pandas.options.mode.use_inf_as_na = True).
	* Returns
		* DataFrame
			* Mask of bool values for each element in DataFrame that indicates whether an element is an NA value.
* [python - How to check if any value is NaN in a Pandas DataFrame - Stack Overflow](https://stackoverflow.com/questions/29530232/how-to-check-if-any-value-is-nan-in-a-pandas-dataframe)
	* `df.isnull().values.any()`
* [pandas.DataFrame.notna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html)
	* Detect existing (non-missing) values.
	* Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings '' or numpy.inf are not considered NA values (unless you set pandas.options.mode.use_inf_as_na = True). NA values, such as None or numpy.NaN, get mapped to False values.
	* Returns
		* DataFrame
			* Mask of bool values for each element in DataFrame that indicates whether an element is not an NA value.

###### [Reshaping, sorting, transposing](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#reshaping-sorting-transposing)

* [pandas.DataFrame.sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values)
	* `DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)`
	* Sort by the values along either axis.
	* Parameters
		* by : str or list of str
			* Name or list of names to sort by.
			* if axis is 0 or ‘index’ then by may contain index levels and/or column labels.
			* if axis is 1 or ‘columns’ then by may contain column levels and/or index labels.
		* axis : {0 or ‘index’, 1 or ‘columns’}, default 0
			* Axis to be sorted.
		* ascending : bool or list of bool, default True
			* Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.
		* inplace : bool, default False
			* If True, perform operation in-place.
		* kind : {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’
			* Choice of sorting algorithm. See also numpy.sort() for more information. mergesort and stable are the only stable algorithms. For DataFrames, this option is only applied when sorting on a single column or label.
		* na_position : {‘first’, ‘last’}, default ‘last’
			* Puts NaNs at the beginning if first; last puts NaNs at the end.
		* ignore_index : bool, default False
			* If True, the resulting axis will be labeled 0, 1, …, n - 1.
			* New in version 1.0.0.
		* key : callable, optional
			* Apply the key function to the values before sorting. This is similar to the key argument in the builtin sorted() function, with the notable difference that this key function should be vectorized. It should expect a Series and return a Series with the same shape as the input. It will be applied to each column in by independently.
			* New in version 1.1.0.
	* Returns
		* DataFrame or None
			* DataFrame with sorted values or None if inplace=True.

###### [Combining / comparing / joining / merging](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#combining-comparing-joining-merging)

* [pandas.DataFrame.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)
	* `DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)`
	* Merge DataFrame or named Series objects with a database-style join.
	* A named Series object is treated as a DataFrame with a single named column.
	* The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored. Otherwise if joining indexes on indexes or indexes on a column or columns, the index will be passed on. When performing a cross merge, no column specifications to merge on are allowed.
	* Warning
		* If both key columns contain rows where the key is a null value, those rows will be matched against each other. This is different from usual SQL join behaviour and can lead to unexpected results.
	* Parameters
		* how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
			* left: use only keys from left frame, similar to a SQL left outer join; preserve key order
			* right: use only keys from right frame, similar to a SQL right outer join; preserve key order
			* outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically
			* inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys
		* sort : boolean, default False
			* Sort the join keys lexicographically in the result DataFrame. If False, the order of the join keys depends on the join type (how keyword)
* [Merge, join, and concatenate — pandas 0.23.1 documentation](https://pandas.pydata.org/pandas-docs/stable/merging.html#merge-join-and-concatenate)
	* [python - Pandas: join DataFrames on field with different names? - Stack Overflow](https://stackoverflow.com/questions/25888207/pandas-join-dataframes-on-field-with-different-names)
		* `pandas.merge(df1, df2, how='left', left_on=['id_key'], right_on=['fk_key'])`
	*	pandas.concat — pandas 0.23.4 documentation
		*	https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html#pandas.concat
		*	`pandas.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)`

###### [Time Series-related](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#time-series-related)

* [pandas.DataFrame.shift](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift)
	* `DataFrame.shift(periods=1, freq=None, axis=0, fill_value=NoDefault.no_default)`
	* Shift index by desired number of periods with an optional time freq.
	* When freq is not passed, shift the index without realigning the data. If freq is passed (in this case, the index must be date or datetime, or it will raise a NotImplementedError), the index will be increased using the periods and the freq. freq can be inferred when specified as “infer” as long as either freq or inferred_freq attribute is set in the index.
* How to drop consecutive duplicates ?
	* python - Pandas: Drop consecutive duplicates - Stack Overflow
		* https://stackoverflow.com/questions/19463985/pandas-drop-consecutive-duplicates
```python
a.loc[a.shift() != a]
de_dup = a[cols].loc[(a[cols].shift() != a[cols]).any(axis=1)]
```
* How to shift column in dataframe ?
	* python - Shift column in pandas dataframe up by one? - Stack Overflow
	* https://stackoverflow.com/questions/20095673/shift-column-in-pandas-dataframe-up-by-one
```python
df.gdp = df.gdp.shift(-1)
df[:-1]
```

###### [Serialization / IO / conversion](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#serialization-io-conversion)

* [pandas.DataFrame.from_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict)
	* `classmethod DataFrame.from_dict(data, orient='columns', dtype=None, columns=None)`
	* Construct DataFrame from dict of array-like or dicts.
	* Creates DataFrame object from dictionary by columns or by index allowing dtype specification.
	* Parameters
		* data : dict
			* Of the form {field : array-like} or {field : dict}.
		* orient : {‘columns’, ‘index’, ‘tight’}, default ‘columns’
			* The “orientation” of the data. If the keys of the passed dict should be the columns of the resulting DataFrame, pass ‘columns’ (default). Otherwise if the keys should be rows, pass ‘index’. If ‘tight’, assume a dict with keys [‘index’, ‘columns’, ‘data’, ‘index_names’, ‘column_names’].
			* New in version 1.4.0: ‘tight’ as an allowed value for the orient argument
		* dtype : dtype, default None
			* Data type to force, otherwise infer.
		* columns : list, default None
			* Column labels to use when orient='index'. Raises a ValueError if used with orient='columns' or orient='tight'.
	* Returns
		* DataFrame
* [pandas.DataFrame.from_records](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records)
	* `classmethod DataFrame.from_records(data, index=None, exclude=None, columns=None, coerce_float=False, nrows=None)`
	* Convert structured or record ndarray to DataFrame.
	* Creates a DataFrame object from a structured ndarray, sequence of tuples or dicts, or DataFrame.
	* Parameters
		* data : structured ndarray, sequence of tuples or dicts, or DataFrame
			* Structured input data.
		* index : str, list of fields, array-like
			* Field of array to use as the index, alternately a specific set of input labels to use.
		* exclude : sequence, default None
			* Columns or fields to exclude.
		* columns : sequence, default None
			* Column names to use. If the passed data do not have names associated with them, this argument provides names for the columns. Otherwise this argument indicates the order of the columns in the result (any names not found in the data will become all-NA columns).
		* coerce_float : bool, default False
			* Attempt to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point, useful for SQL result sets.
		* nrows : int, default None
			* Number of rows to read if data is an iterator.
	* Returns
		* DataFrame
* [pandas.DataFrame.to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv)
	* `DataFrame.to_csv(path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)`
	* Write object to a comma-separated values (csv) file.
* How to add pandas data to an existing csv file? - Stack Overflow
	* https://stackoverflow.com/questions/17530542/how-to-add-pandas-data-to-an-existing-csv-file
	```python
	with open(filename, 'a') as f:
	df.to_csv(f, header=False)
	```
* [How to Append Pandas DataFrame to Existing CSV File? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/)
	* `df.to_csv('GFG.csv', mode='a', index=False, header=False)`
* How to stop appending a blank line in csv ?
	* `pandas.DataFrame.to_csv( line_terminator='\n' )`
	* pandas.DataFrame.to_csv — pandas 0.24.2 documentation
		* http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
		* line_terminator : string, optional
		* The newline character or character sequence to use in the output file. Defaults to os.linesep, which depends on the OS in which this method is called (‘n’ for linux, ‘rn’ for Windows, i.e.).
		* Changed in version 0.24.0.
* [pandas.DataFrame.to_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html)
	* Write object to an Excel sheet.
	* `DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=_NoDefault.no_default, inf_rep='inf', verbose=_NoDefault.no_default, freeze_panes=None, storage_options=None)`
* [How to Write Pandas DataFrames to Multiple Excel Sheets? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-write-pandas-dataframes-to-multiple-excel-sheets/)
```python
# import the python pandas package
import pandas as pd

# create data_frame1 by creating a dictionary
# in which values are stored as list
data_frame1 = pd.DataFrame({'Fruits': ['Appple', 'Banana', 'Mango',
									'Dragon Fruit', 'Musk melon', 'grapes'],
							'Sales in kg': [20, 30, 15, 10, 50, 40]})

# create data_frame2 by creating a dictionary
# in which values are stored as list
data_frame2 = pd.DataFrame({'Vegetables': ['tomato', 'Onion', 'ladies finger',
										'beans', 'bedroot', 'carrot'],
							'Sales in kg': [200, 310, 115, 110, 55, 45]})

# create data_frame3 by creating a dictionary
# in which values are stored as list
data_frame3 = pd.DataFrame({'Baked Items': ['Cakes', 'biscuits', 'muffins',
											'Rusk', 'puffs', 'cupcakes'],
							'Sales in kg': [120, 130, 159, 310, 150, 140]})

print(data_frame1)
print(data_frame2)
print(data_frame3)

# create a excel writer object
with pd.ExcelWriter("path to file\filename.xlsx") as writer:

	# use to_excel function and specify the sheet_name and index
	# to store the dataframe in specified sheet
	data_frame1.to_excel(writer, sheet_name="Fruits", index=False)
	data_frame2.to_excel(writer, sheet_name="Vegetables", index=False)
	data_frame3.to_excel(writer, sheet_name="Baked Items", index=False)
```
* [No module named 'openpyxl' - Python 3.4 - Ubuntu - Stack Overflow](https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu)
	* pip refers to Python 2 as a default in Ubuntu, this means that pip install x will install the module for Python 2 and not for 3
	* pip3 refers to Python 3, it will install the module for Python 3
	* `pip3 install openpyxl`
* How to clear existing excel sheets and append new sheets ?
```python
import pandas as pd

with pd.ExcelWriter(output_file) as writer:
	df = pd.DataFrame()
	df.to_excel(writer, sheet_name='Sheet1', index=False)

...

with pd.ExcelWriter(output_file,
					mode='a',
					if_sheet_exists='replace'
) as writer:
	df_new.to_excel(writer, sheet_name='Sheet2', index=False)
```
* [pandas.DataFrame.to_string](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas-dataframe-to-string)
	* `DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None, min_rows=None, max_colwidth=None, encoding=None)`
	* How to print all elements in a dataframe ?
		* [python - Is there a way to pretty print an entire Pandas Series / DataFrame? - Stack Overflow](https://stackoverflow.com/questions/19124601/is-there-a-way-to-pretty-print-an-entire-pandas-series-dataframe)
```python
print(df.to_string())
```

##### [General utility functions](https://pandas.pydata.org/pandas-docs/stable/reference/general_utility_functions.html)

* [pandas.set_option — pandas 1.4.3 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html)
	* [Options and settings — pandas 1.4.3 documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#options-and-settings)
	* [pandas 8 个常用的 option 设置](https://mp.weixin.qq.com/s/0-i7xwJnPsIOCJewSl1NUA)
```python
pd.set_option('display.max_rows',xxx) # 最大行数
pd.set_option('display.min_rows',xxx) # 最小显示行数
pd.set_option('display.max_columns',xxx) # 最大显示列数
pd.set_option ('display.max_colwidth',xxx) #最大列字符数
pd.set_option( 'display.precision',2) # 浮点型精度
pd.set_option('display.float_format','{:,}'.format) #逗号分隔数字
pd.set_option('display.float_format',  '{:,.2f}'.format) #设置浮点精度
pd.set_option('display.float_format', '{:.2f}%'.format) #百分号格式化
pd.set_option('plotting.backend', 'altair') # 更改后端绘图方式
pd.set_option('display.max_info_columns', 200) # info输出最大列数
pd.set_option('display.max_info_rows', 5) # info计数null时的阈值
pd.describe_option() #展示所有设置和描述
pd.reset_option('all') #重置所有设置选项
```

#### BEST PRACTICE

* [常用的46个Pandas方法](https://mp.weixin.qq.com/s/-pazqu03A4ejRvFRCfHoZw)
* [Pandas 中第二好用的函数是？](https://mp.weixin.qq.com/s/xc3kpVXeYcKu9Xxn5B1gxg)
* [Pandas数据处理——盘点那些常用的函数（上）](https://mp.weixin.qq.com/s/IVUrb97GN3QvgYsBFdpc2w)
* [Pandas0.25来了，别错过这10大好用的新功能](https://mp.weixin.qq.com/s/YaVipYsRYBF2eIBq9ps5VA)
* [一文掌握 Series 和 DataFrame 的基础功能](https://mp.weixin.qq.com/s/5rLI5Vol67tjMeE-YVfBbw)
	* https://www.zhihu.com/people/zarten/activities
* [一文详解 merge 数据拼接方法](https://mp.weixin.qq.com/s/-P2dE_gXhbjrlFTC7VSGjA)
* [一文完全掌握Pandas中的groupby操作](https://mp.weixin.qq.com/s/_H-jEBx_o4qUnruAHqSbOg)
* [用 Style 方法提高 Pandas 数据的颜值](https://mp.weixin.qq.com/s/Ws09pBW5P2HzapmsxfbMwA)
	* https://pbpython.com/styling-pandas.html
	* Pandas的style用法在大多数教程中见的比较少，它主要是用来美化DataFrame和Series的输出，能够更加直观地显示数据结果。
* [利用 Pandas 分析日志数据](https://mp.weixin.qq.com/s/A3lteYWeM2gM8qH75M8rXQ)
* [【技巧】Pandas循环提速7万多倍](https://mp.weixin.qq.com/s/VavtPcBtVzLw_k8KxSdKqw)
	* https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06
* [【技巧】11 个 Python Pandas 小技巧让你更高效](https://mp.weixin.qq.com/s?__biz=MzIxODM4MjA5MA==&mid=2247490794&idx=2&sn=0f92cd1f274534f77f722f48f1e38023&chksm=97ea368fa09dbf99370385244a6e0828bedac23b3f1aa88bb36671d0102dfb3e1f663216858d&mpshare=1&scene=24&srcid=&sharer_sharetime=1568072412382&sharer_shareid=5ed4a849fa42d9599a974fa8eb45e8fa&key=b1719993cc296ec4a2ee472aa9c64ca953f23c2e1990555a735ef4dc57db63bddc3527235579b4df2fd5f77d61135ae5af57d1a86f8557b1c73712f5bbcfd8707644a485c2bc5fedefe3e564b4c2919a&ascene=14&uin=MTMzMzc3MjY4MQ%3D%3D&devicetype=Windows+10&version=62060833&lang=en&pass_ticket=tT3maEfznKd3xtVT4L8%2Bl%2B2KKdhrJZ3ERaWEoIpqIMB2I2ssKo%2BTfx0v80L7rMTL)
* [不识 Pandas，纵是老手也枉然？](https://mp.weixin.qq.com/s/ZfwITBpt_etOpEfzyXdDAQ)
* [Pandas可视化综合指南：手把手从零教你绘制数据图表](https://mp.weixin.qq.com/s/yO6u7b6zdkE8pGoNsrtKkg)
	* https://kanoki.org/2019/09/16/dataframe-visualization-with-pandas-plot/
	* https://www.kaggle.com/PromptCloudHQ/world-happiness-report-2019/version/1
* [如何在 Python 数据中清洗常用 4 板斧？](https://mp.weixin.qq.com/s/M9vefH0FZeWwEk73SW-aIQ)
* [8 段用于数据清洗 Python 代码](https://towardsdatascience.com/the-simple-yet-practical-data-cleaning-codes-ad27c4ce0a38)
* [如何只用一行代码让Pandas加速四倍？](https://mp.weixin.qq.com/s/Jkx1K7d1ufD2S6s2cOA7Hw)
	* https://www.kdnuggets.com/2019/11/speed-up-pandas-4x.html
* [提升Pandas性能，让你的pandas飞起来](https://mp.weixin.qq.com/s/qwgkGtT9LtaeWnTB-ShfRw)
* [12 个 Numpy 和 Pandas 函数，提高效率](https://mp.weixin.qq.com/s/kUzvvYcw8qK80R-ASWsIpQ)
	* [12 Amazing Pandas & NumPy Functions | by Kunal Dhariwal | Towards Data Science](https://towardsdatascience.com/12-amazing-pandas-numpy-functions-22e5671a45b8)
	* [GitHub - kunaldhariwal/12-Amazing-Pandas-NumPy-Functions: Code linked to the article published on medium.com](https://github.com/kunaldhariwal/12-Amazing-Pandas-NumPy-Functions)
	* Numpy 的 6 种高效函数
		* argpartition()
		* allclose()
		* clip()
		* extract()
		* where()
		* percentile()
	* Pandas 数据统计包的 6 种高效函数
		* read_csv(nrows=n)
		* map()
		* apply()
		* isin()
		* copy()
		* select_dtypes()
* [如何优雅地使用pdpipe与Pandas构建管道？](https://mp.weixin.qq.com/s/URsFRHDwApp3Oj3fwtxnwg)
	* https://towardsdatascience.com/https-medium-com-tirthajyoti-build-pipelines-with-pandas-using-pdpipe-cade6128cd31
* [用 Pandas 玩转时间序列数据](https://mp.weixin.qq.com/s/s2oVfyURx42hGrEIVtppdQ)
	* 进行金融数据分析或量化研究时，总避免不了时间序列数据的处理，时间序列是指在一定时间内按时间顺序测量的某个变量的取值序列。常见的时间序列数据有一天内随着时间变化的温度序列，又或者交易时间内不断波动的股票价格序列。Pandas也因其强大的时序处理能力而被广泛应用于金融数据分析，这篇文章为大家介绍一下Pandas中的时间序列处理，所使用的数据是上证指数2019年的行情数据。
	* 时间相关的数据类型
	* 将时间列转换为时间格式
	* 时间序列的索引
	* 提取出时间/日期的属性
	* resample

#### FAQ

* [Comparison with SQL — pandas 0.23.3 documentation](https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#)
	* [How to rewrite your SQL queries in Pandas, and more ?](https://codeburst.io/how-to-rewrite-your-sql-queries-in-pandas-and-more-149d341fc53e)
* How to Concatenating a single Series into a string ?
	* [Working with Text Data](http://pandas.pydata.org/pandas-docs/stable/text.html#concatenating-a-single-series-into-a-string)

##### ERROR FIX

* How to fix AssertionError: Number of manager items must equal union of block items ?
	* It is caused by duplicated columns names in one dataframe, find it out and remove the duplicates.
	* Pandas Python: Concatenate dataframes having same columns - Stack Overflow
	* https://stackoverflow.com/questions/52204115/pandas-python-concatenate-dataframes-having-same-columns
* How to fix FutureWarning Passing list-likes to .loc or [] with any missing label will raise KeyError in the future, you can use .reindex() as an alternative ?
	* Indexing and Selecting Data — pandas 0.23.4 documentation
		* http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-with-list-with-missing-labels-is-deprecated
	* pandas.DataFrame.reindex — pandas 0.23.4 documentation
		* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html?highlight=reindex#pandas-dataframe-reindex
		* `DataFrame.reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=True, level=None, fill_value=nan, limit=None, tolerance=None)`
```python
a = df.loc[ new_index ]
# change loc[] to reindex(). a = df.reindex( new_index )
```
* How to fix SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead ?
	* Indexing and Selecting Data — pandas 0.23.4 documentation
		* http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
	* python - How to deal with SettingWithCopyWarning in Pandas? - Stack Overflow
		* https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
		* If you explicitly copy then no further warning will happen
	* .loc[...] = value returns SettingWithCopyWarning · Issue #17476 · pandas-dev/pandas · GitHub
		* https://github.com/pandas-dev/pandas/issues/17476
		* Pandas isn't 100% sure if you want to assign values to just your df_c slice, or have it propagate all the way back up to the original df. To avoid this when you first assign df_c make sure you tell pandas that it is its own data frame (and not a slice) by using .copy()
```python
a = df.loc[ new_index]
a[ 'col1' ] = a[ 'col2' ]
# change a = df.loc[ new_index] to a = df.loc[ new_index].copy()
```
* How to fix TypeError: invalid type promotion when plot scatter with timestamp ?
	* python - Pandas type error trying to plot - Stack Overflow
		* https://stackoverflow.com/questions/33676608/pandas-type-error-trying-to-plot
	* pandas.DataFrame.astype — pandas 0.22.0 documentation
		* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.astype.html
* How to fix TypeError: 'instancemethod' object has no attribute '__getitem__' ?
	* You are using square brackets after an object that doesn't know what to do with the square brackets.
```python
a= df.reindex[ new_index ]
change [] to (). a= df.reindex( new_index )
```
* How to fix TypeError: type object argument after * must be an iterable, not itertools.imap ?
	* python - Pandas drop_duplicates - TypeError: type object argument after * must be a sequence, not map - Stack Overflow
		* https://stackoverflow.com/questions/37792999/pandas-drop-duplicates-typeerror-type-object-argument-after-must-be-a-seque
		* it's because the list type isn't hashable and that's messing up the duplicated logic. As a workaround you could cast to tuple.
```python
df.drop_duplicates(subset=['position_xy'], inplace=False)
cast column from type list to tuple
df['position_xy'] = df['position_xy'].apply(lambda x : tuple(x) if type(x) is list else x)
```
* How to fix ValueError: The truth value of a Series is ambiguous ?
	* python - Truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all() - Stack Overflow
		* https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o
		* The or and and python statements require truth-values. For pandas these are considered ambiguous so you should use "bitwise" | (or) or & (and) operations
* How to fix ValueError: ('The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().', u'occurred at index 0') ?
	* 5 ways to apply an IF condition in pandas DataFrame - Data to Fish
		* https://datatofish.com/if-condition-in-pandas-dataframe/
	* python - Applying a conditional statement to all value of a dataframe - Stack Overflow
		* https://stackoverflow.com/questions/43377868/applying-a-conditional-statement-to-all-value-of-a-dataframe
		* `df[df<3]=0`
```python
# Problem
cols = [c for c in df.columns if not c.startswith(('a'))]
df[cols] = df[cols].apply( lambda x : 0 if x < 1e-10 else x, axis=1 )

# It is because list comprehesion is not applicable with Dataframe object.

# Solution 1
for c in df.columns:
if not c.startswith(('a')):
df[c] = df[c].apply( lambda x : 0 if x < 1e-10 else x )

# Solution 2
df1 = df[cols].copy()
df1[df1 < 1e-10] = 0
df[cols] = df1[cols].copy()
```
* How to fix ValueError: can not merge DataFrame with instance of type <class 'pandas.core.series.Series'> ?
	* python - Merging two DataFrames - Stack Overflow
		* https://stackoverflow.com/questions/37968785/merging-two-dataframes
		* `df1.merge(df2.to_frame(), left_on='id', right_index=True)`
	* python - Combining two Series into a DataFrame in pandas - Stack Overflow
		* https://stackoverflow.com/questions/18062135/combining-two-series-into-a-dataframe-in-pandas
		* `pd.concat([s1, s2], axis=1).reset_index()`
```python
df_mean = df.groupby('id').col.mean().rename('mean_col')
df_min = df.groupby('id').col.min().rename('min_col')
df_result = pd.concat([df_mean, df_min], axis=1).reset_index()
```

# END
