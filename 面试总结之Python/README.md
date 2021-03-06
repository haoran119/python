# 面试总结之Python

* [python/学习笔记之Python at main · haoran119/python](https://github.com/haoran119/python/tree/main/%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0%E4%B9%8BPython)
* [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* [[ZZ]知名互联网公司Python的16道经典面试题及答案 - 浩然119 - 博客园 (cnblogs.com)](https://www.cnblogs.com/pegasus923/p/8674215.html)
* [全面的Python重点](https://mp.weixin.qq.com/s/UN2RNV8LXXlLIZ3G3Zpukw)
  * https://segmentfault.com/a/1190000018737045
  * python变量名的解析机制(LEGB)(Local -> Enclosing -> Global -> Built-in)
    * 本地作用域(Local)(e.g. 函数内部作用域)
    * 当前作用域被嵌入的本地作用域(Enclosing locals)(e.g. 函数内部与内嵌函数之间)
    * 全局/模块作用域(Global)
    * 内置作用域(Built-in)
    * [Python Variable Scope with Local & Non-local Examples - DataCamp](https://www.datacamp.com/community/tutorials/scope-of-variables-python)
  * a in s or b in s or c in s简写
  ```
  any(i in s for i in [a,b,c])
  ```
  * set集合运用
  ```
  {1, 2}.issubset({1, 2, 3}) #判断是否是其子集
  {1, 2, 3}.issuperset({1, 2})
  {1, 2}.isdisjoint({1, 3}) #判断两个set交集是否为空,是空集则为True
  ```
  * 实现从1-100每三个为一组分组
  ```
  print([[x for x in range(1,101)][i:i+3] for i in range(0,100,3)])
  ```
  * yield from与yield的区别：
    * yield from跟的是一个可迭代对象，而yield后面没有限制
    * GeneratorExit生成器停止时触发
    * [In practice, what are the main uses for the new "yield from" syntax in Python 3.3? - Stack Overflow](https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3)
* [百度大牛总结十条Python面试题陷阱，看看你是否会中招 (toutiao.com)](https://www.toutiao.com/i6550223737344492039/?wid=1621651237098)
* [Python面试攻略（coding篇）](https://blog.csdn.net/u013205877/article/details/77542837)
  * [taizilongxu/interview_python: 关于Python的面试题 (github.com)](https://github.com/taizilongxu/interview_python)
  * [24 Python垃圾回收机制](https://github.com/taizilongxu/interview_python#24-python%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6%E6%9C%BA%E5%88%B6)
    * Python GC主要使用引用计数（reference counting）来跟踪和回收垃圾。在引用计数的基础上，通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题，通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率。
    * [python循环引用是什么意思？-Python学习网](https://www.py.cn/jishu/jichu/27568.html)
* [2018年最常见的Python面试题&答案（上篇） (juejin.cn)](https://juejin.cn/post/6844903654143557646)
* [春招苦短，我用百道Python面试题备战 (qq.com)](https://mp.weixin.qq.com/s/qaMiTgRaeDRS59N4DiCYNw)
  * [kenwoodjw/python_interview_question: 关于python的面试题 (github.com)](https://github.com/kenwoodjw/python_interview_question)
* [110道python面试题 (qq.com)](https://mp.weixin.qq.com/s/DlD64oec7P-rNIFoN6DN1g)
  * [110道Python面试题（真题） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/54430650)
* [Python 面试中 8 个必考问题 (qq.com)](https://mp.weixin.qq.com/s/04eZJyvj0TjBnw8_4M9X9A)
* [Python 爬虫面试题 170 道：2019 版 (qq.com)](https://mp.weixin.qq.com/s/W50_dlTH_NRpz9SqTZx80Q)
* 用Python手写十大经典排序算法
  * [hustcc/JS-Sorting-Algorithm: 一本关于排序算法的 GitBook 在线书籍 《十大经典排序算法》，多语言实现。 (github.com)](https://github.com/hustcc/JS-Sorting-Algorithm)
* [53个Python经典面试题详解 (qq.com)](https://mp.weixin.qq.com/s/Ck1tcCez2BwGlOla6tjGWA)
  * [53 Python Interview Questions and Answers | by Chris I. | Towards Data Science](https://towardsdatascience.com/53-python-interview-questions-and-answers-91fa311eec3f)
* [吐血整理的 Python 面试题(qq.com)](https://mp.weixin.qq.com/s/4GUHtSxGhBaBVfMMsX8lOQ)
* [What are .pyc files in Python?](https://www.tutorialspoint.com/What-are-pyc-files-in-Python)
  * .pyc files are created by the Python interpreter when a .py file is imported. They contain the "compiled bytecode" of the imported module/program so that the "translation" from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file, thus speeding startup a little. But it's still interpreted. Once the *.pyc file is generated, there is no need of *.py file, unless you edit it.
* [Difference between continue and pass statements in Python - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-continue-and-pass-statements-in-python/)
  * Continue statement
    * This statement is used to skip over the execution part of the loop on a certain condition. After that, it transfers the control to the beginning of the loop. Basically, it skips its following statements and continues with the next iteration of the loop.
  * Pass statement
    * As the name suggests pass statement simply does nothing. We use pass statement to write empty loops. Pass is also used for empty control statements, functions and classes.
* [Python | Difference Between List and Tuple - GeeksforGeeks](https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/)

| SR.NO. | LIST | TUPLE |
| - | - | - | 
1 | Lists are mutable | Tuples are immutable
2 | Implication of iterations is Time-consuming | The implication of iterations is comparatively Faster
3 | The list is better for performing operations, such as insertion and deletion.	| Tuple data type is appropriate for accessing the elements
4 | Lists consume more memory | Tuple consume less memory as compared to the list
5 | Lists have several built-in methods | Tuple does not have many built-in methods.
6 | The unexpected changes and errors are more likely to occur | In tuple, it is hard to take place.

* [Serializing Python Objects into JSON | Pythontic.com](https://pythontic.com/serialization/json/introduction)
  * Any Python object can be serialized into JSON format and vice versa.
  * [Serializing JSON data in Python - GeeksforGeeks](https://www.geeksforgeeks.org/serializing-json-data-in-python/)
    * Serialization is the process of encoding the from naive datat type to JSON format. The Python module json converts a Python dictionary object into JSON object, and list and tuple are converted into JSON array, and int and float converted as JSON number, None converted as JSON null. 
  * [python - How to make a class JSON serializable - Stack Overflow](https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable)
    * In that case you can merely call json.dumps(f.__dict__).
* [Read a file line by line in Python - GeeksforGeeks](https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/)
  * Reading line by line
    * Using readlines()
      * readlines() is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines. We can iterate over the list and strip the newline ‘\n’ character using strip() function.
    * Using readline()
      * readline() function reads a line of the file and return it in the form of the string. It takes a parameter n, which specifies the maximum number of bytes that will be read. However, does not reads more than one line, even if n exceeds the length of the line. It will be efficient when reading a large file because instead of fetching all the data in one go, it fetches line by line. readline() returns the next line of the file which contains a newline character in the end. Also, if the end of the file is reached, it will return an empty string.
    * Using for loop
      * An iterable object is returned by open() function while opening a file. This final way of reading in a file line-by-line includes iterating over a file object in a for loop. Doing this we are taking advantage of a built-in Python function that allows us to iterate over the file object implicitly using a for loop in a combination with using the iterable object. This approach takes fewer lines of code, which is always the best practice worthy of following.
  * With statement
    * The With statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. 
* [How to multiply two pandas DataFrame columns in Python](https://www.kite.com/python/answers/how-to-multiply-two-pandas-dataframe-columns-in-python#:~:text=Use%20the%20syntax%20df%5Bcol1,result%20to%20a%20new%20column.)
```python
df["a*b"] = df["a"] * df["b"]
```

## CODE

* [Solve Python | HackerRank](https://www.hackerrank.com/domains/python?badge_type=python)
* [100道Python练手题目](https://mp.weixin.qq.com/s/0y19nH3nxkAPmB52EAMvLA)
  * https://github.com/RichardFu123/Python100Cases
* Python练手题
  * [python 题_yang_bingo的博客-CSDN博客](https://blog.csdn.net/yang_bingo/article/details/80285205)
* [100+Python编程题给你练~（附答案） (qq.com)](https://mp.weixin.qq.com/s?__biz=Mzg4NDQwNTI0OQ==&mid=2247523362&idx=4&sn=31ce0678907d603c3ddc92eb4e665f34&source=41#wechat_redirect)
  * [Python-programming-exercises/100+ Python challenging programming exercises.txt at master · zhiwehu/Python-programming-exercises (github.com)](https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt)
* Python如何实现单例模式?
  * 使用装饰器
  ```python
  def singleton(cls):
      instances = {}

      def wrapper(*args, **kwargs):
          if cls not in instances:
              instances[cls] = cls(*args, **kwargs)
          return instances[cls]

      return wrapper


  @singleton
  class Foo(object):
      pass


  foo1 = Foo()
  foo2 = Foo()

  print(foo1 is foo2)     # True
  ```
  * 使用基类
    * New 是真正创建实例对象的方法，所以重写基类的new 方法，以此保证创建对象的时候只生成一个实例
  ```python
  class Singleton:
      def __new__(cls: Any, *args, **kwargs) -> Any:
          if not hasattr(cls, '_instance'):
              cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

          return cls._instance


  class Singleton1:
      _instance = None

      def __new__(cls: Any) -> Any:
          if cls._instance is None:
              cls._instance = super(Singleton1, cls).__new__(cls)
              return cls._instance
          else:
              return cls._instance


  class Foo(Singleton):
      pass


  class Foo1(Singleton1):
      pass


  foo1 = Foo()
  foo2 = Foo()
  foo11 = Foo1()
  foo12 = Foo1()

  print(foo1 is foo2)     # True
  print(foo11 is foo12)   # True
  ```
