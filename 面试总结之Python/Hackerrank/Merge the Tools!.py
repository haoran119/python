# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        u = []
        for c in string[i : i + k]:
            if c not in u:
                u.append(c)

        print(''.join(u))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
