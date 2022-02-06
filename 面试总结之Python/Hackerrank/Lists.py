# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true


if __name__ == '__main__':
    N = int(input())
    results = []
    
    for _ in range(N):
        s = input().split()
        command = s[0]
        args = s[1:]
        
        if command != 'print':
            eval('results.{0}{1}'.format(command, tuple(map(int, args))))
        else:
            print(results)
