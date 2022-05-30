# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=false

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    dict_a = defaultdict(list)
    for i in range(1, n + 1):
        dict_a[input()].append(str(i))
    
    for i in range(m):
        word = input()
        print(' '.join(dict_a[word]) if word in dict_a else -1)
