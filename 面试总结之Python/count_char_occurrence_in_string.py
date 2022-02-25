#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/program-count-occurrence-given-character-string/?ref=gcse

Given a string and a character, task is to make a function which count
occurrence of the given character in the string.
"""


def count_char_occurrence_in_string(s: str, c: str) -> int:
    result = 0

    for i in range(len(s)):
        if s[i] == c:
            result += 1

    return result


if __name__ == '__main__':
    s_input = "geeksforgeeks"
    c_input = 'e'

    result = count_char_occurrence_in_string(s_input, c_input)
    print(result)
