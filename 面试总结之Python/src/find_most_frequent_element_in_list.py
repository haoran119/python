#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/

Given a list, find the most frequent element in it. If there are multiple
elements that appear maximum number of times, print any one of them.
"""


from collections import Counter
from typing import Any


def find_most_frequent_element_in_list1(list_input: list) -> Any:
    """Using Counter
    """

    if not list_input:
        return None

    return Counter(list_input).most_common(1)[0][0]


def find_most_frequent_element_in_list2(list_input: list) -> Any:
    """Using list.count
    """

    if not list_input:
        return None

    max_frequency = 0
    result = list_input[0]

    for i in list_input:
        current_frequency = list_input.count(i)

        if current_frequency > max_frequency:
            max_frequency = current_frequency
            result = i

    return result


def find_most_frequent_element_in_list3(list_input: list) -> Any:
    """Using set
    Make a set of the list so that the duplicate elements are deleted.
    Then find the highest count of occurrences of each element in the set and thus, we find the maximum out of it.
    """

    if not list_input:
        return None

    return max(set(list_input), key=list_input.count)


if __name__ == '__main__':
    inputs = [2, 1, 2, 2, 1, 3]

    result = find_most_frequent_element_in_list1(inputs)
    print(result)   # 2
    result = find_most_frequent_element_in_list2(inputs)
    print(result)   # 2
    result = find_most_frequent_element_in_list3(inputs)
    print(result)   # 2

    inputs = ['Dog', 'Cat', 'Dog']

    result = find_most_frequent_element_in_list1(inputs)
    print(result)   # Dog
    result = find_most_frequent_element_in_list2(inputs)
    print(result)   # Dog
    result = find_most_frequent_element_in_list3(inputs)
    print(result)   # Dog
