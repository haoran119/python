# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# !/bin/python3

# import math
# import os
# import random
# import re
# import sys
import string


# Complete the solve function below.
def solve(s):
    return string.capwords(s, ' ')
    # return ' '.join([name.capitalize() for name in s.split(' ')])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
