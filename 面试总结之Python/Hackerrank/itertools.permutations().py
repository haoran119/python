# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


if __name__ == '__main__':
    S, k = input().split()
    
    results = [''.join(i) for i in permutations(sorted(S), int(k))]
    
    print(*results, sep='\n')
