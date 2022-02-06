# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true


from collections import Counter


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    X = int(input())
    shoe_sizes = Counter([int(x) for x in input().split()])
    N = int(input())
    orders = [[int(x) for x in input().split()] for _ in range(N)]

    income = 0
    for order in orders:
        if shoe_sizes[order[0]] > 0:
            income += order[1]
            shoe_sizes[order[0]] -= 1
    
    print(income)          
