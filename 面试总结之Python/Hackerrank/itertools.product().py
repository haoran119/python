# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true


from itertools import product


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    # A = map(int, input().split())
    # B = map(int, input().split())
    
    print(*product(A, B))
