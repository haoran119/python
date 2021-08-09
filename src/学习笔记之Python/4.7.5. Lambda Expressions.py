#!/usr/bin/python3

res = {}
with open('demo.txt') as f:
    for ch in f.read().replace(' ', ''):
        res[ch] = res.get(ch, 0) + 1

# lambda x[1] stands for value in dictionary, x[0] stands for key in dictionary
for char, num in sorted(res.items(), key=lambda x: x[1], reverse=True)[:3]:
    print('char %s count is %d' % (char, num))
