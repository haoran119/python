#!/usr/bin/env python3

"""
https://www.geeksforgeeks.org/stack-in-python/

https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

Stack implementation

The functions associated with stack are:

empty() - Returns whether the stack is empty - Time Complexity: O(1)
size() - Returns the size of the stack - Time Complexity: O(1)
top() - Returns a reference to the topmost element of the stack - Time Complexity: O(1)
push(a) - Inserts the element 'a' at the top of the stack - Time Complexity: O(1)
pop() - Deletes the topmost element of the stack - Time Complexity: O(1)
"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.data = []

    def empty(self) -> None:
        return not self.data

    def size(self) -> None:
        return len(self.data)

    def top(self) -> Any:
        if not self.data:
            return None

        return self.data[-1]

    def push(self, *args) -> None:
        for arg in args:
            self.data.append(arg)

    def pop(self) -> None:
        self.data.pop()

    def __str__(self) -> None:
        return('Stack [{}]'.format(', '.join([str(d) for d in self.data[::-1]])))


if __name__ == '__main__':
    my_stack = Stack()
    print(my_stack.empty())
    print(my_stack.size())
    print(my_stack.top())
    print(my_stack)

    my_stack.push(1, 2, 3)

    print(my_stack.empty())
    print(my_stack.size())
    print(my_stack.top())
    print(my_stack)

    my_stack.push(4)
    my_stack.push(5)

    print(my_stack.empty())
    print(my_stack.size())
    print(my_stack.top())
    print(my_stack)

    my_stack.pop()
    my_stack.pop()

    print(my_stack.empty())
    print(my_stack.size())
    print(my_stack.top())
    print(my_stack)

    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    # my_stack.pop()  # IndexError: pop from empty list

    print(my_stack.empty())
    print(my_stack.size())
    print(my_stack.top())
    print(my_stack)
