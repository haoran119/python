# https://www.hackerrank.com/challenges/designer-door-mat/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    n, m = map(int, input().split())
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    result = '\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])

    print(result)
