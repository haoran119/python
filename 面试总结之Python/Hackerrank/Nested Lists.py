# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true


if __name__ == '__main__':
    results = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        results.append([name, score])
    
    second_highest_score = sorted(list(set(result[1] for result in results)))[1]
    
    second_highest_names = sorted([result[0] for result in results if result[1] == second_highest_score])
    
    
    print('\n'.join(second_highest_names))
