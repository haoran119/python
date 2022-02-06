# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    # your code goes here
    max_width = len('{0:b}'.format(number))
    for i in range(1, n + 1):
        print('{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}'.format(i, max_width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
