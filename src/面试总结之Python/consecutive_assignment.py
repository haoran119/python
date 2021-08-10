'''
Consecutive assignment

Assignment against list is shallow copy.
'''

a = b = 0

a = 1

print(a)  # 1
print(b)  # 0

a = b = []

a.append(0)

print(a)  # [0]
print(b)  # [0]

a = []
b = []

a.append(0)

print(a)  # [0]
print(b)  # []
