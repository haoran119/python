# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true


import string


def print_rangoli(size):
    # your code goes here
    results = []
    alpha = string.ascii_lowercase

    for i in range(size):
        s = '-'.join(alpha[i:size])
        results.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print('\n'.join(results[::-1] + results[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
