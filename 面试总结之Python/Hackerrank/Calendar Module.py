# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar


if __name__ == '__main__':
    m, d, y = [int(x) for x in input().split()]
    
    result = calendar.day_name[calendar.weekday(y, m, d)].upper()
    print(result)
    
