#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/

https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html
"""


class Solution:
    def __init__(self) -> None:
        pass

    def search_in_file(self, input_file: str, output_file: str, key: str) -> None:
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            for line in fin:
                line = line.strip()

                if key in line:
                    fout.write('{}\n'.format(line))
                    print(line, end='\n')

    def search_in_file_w_re(self, input_file: str, output_file: str, key: str) -> None:
        import re

        pattern = re.compile('(.*{}.*)'.format(key))

        with open(input_file, 'r') as fin:
            text = fin.read()
            results = re.findall(pattern, text)

        with open(output_file, 'w') as fout:
            for result in results:
                fout.write('{}\n'.format(result))
                print(result, end='\n')


if __name__ == '__main__':
    mySolution = Solution()
    input = 'input.txt'
    output = 'output.txt'
    search_key = 'file'

    mySolution.search_in_file(input, output, search_key)

    mySolution.search_in_file_w_re(input, output, search_key)
