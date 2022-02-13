#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 19:54:40 2022

@author: Hao
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


if __name__ == '__main__':
    mySolution = Solution()
    input = 'input.txt'
    output = 'output.txt'
    search_key = 'file'

    mySolution.search_in_file(input, output, search_key)
