"""
Remove spaces from a string

https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
"""

import re


def remove(string):
    return string.replace(" ", "")


def remove2(string):
    return "".join(string.split())


def remove3(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)


# Driver Program
string = ' g e e k '
print(remove(string))   # geek
print(remove2(string))   # geek
print(remove3(string))   # geek
