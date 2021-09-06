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
