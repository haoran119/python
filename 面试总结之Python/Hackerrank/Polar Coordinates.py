# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true


# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import polar


if __name__ == '__main__':
    result = polar(complex(input()))
    
    print(*result, sep='\n')
    
