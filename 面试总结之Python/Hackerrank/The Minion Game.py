# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true


def minion_game(string):
    # your code goes here
    score_Stuart, score_Kevin = 0, 0
    vowels = 'AEIOU'

    for i in range(len(string)):
        if string[i] in vowels:
            score_Kevin += len(string) - i
        else:
            score_Stuart += len(string) - i

    if score_Kevin > score_Stuart:
        print('Kevin {}'.format(score_Kevin))
    elif score_Kevin < score_Stuart:
        print('Stuart {}'.format(score_Stuart))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
