# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:05:55 2018

@author: h.tang
"""

# using for loop
a = [1, 2, 3, 4, 5]

# =============================================================================
# 1. Using for loop : Traverse from 0 to len(list) and print all elements of the list one by one uisng a for loop,
# this is the standard practice of doing it.
# =============================================================================
#1
#2
#3
#4
#5
#1 2 3 4 5

# printing the list using loop
for x in range(len(a)):
    print a[x]

for x in range(len(a)):
    print a[x],

# =============================================================================
# 2. Without using loops: * symbol is use to print the list elements in a single line with space.
# To print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively.
# =============================================================================
# Python program to print list
# without using loop

a = [1, 2, 3, 4, 5]

#1 2 3 4 5
#printing lists separated by commas
#1, 2, 3, 4, 5
#printing lists in new line
#1
#2
#3
#4
#5

# printing the list using * operator separated
# by space
print(*a)

# printing the list using * and sep operator
print("printing lists separated by commas")

print(*a, sep = ", ")

# print in new line
print("printing lists in new line")

print(*a, sep = "\n")

# =============================================================================
# 3. Convert a list to a string for display : If it is a list of strings we can simply join them using join() function,
# but if the list contains integers then convert it into string and then use join() function to join them to a string and print the string.
# =============================================================================
# Python program to print list
# by Converting a list to a
# string for display
a =["Geeks", "for", "Geeks"]

#Geeks for Geeks
#1, 2, 3, 4, 5

# print the list using join function()
print(' '.join(a))

# print the list by converting a list of
# integers to string
a = [1, 2, 3, 4, 5]

print str(a)[1:-1]

# =============================================================================
# 4. Using map : Use map() to convert each item in the list to a string if list is not a string, and then join them
# =============================================================================
# Python program to print list
# print the list by converting a list of
# integers to string using map
a = [1, 2, 3, 4, 5]
#1 2 3 4 5
#in new line
#1
#2
#3
#4
#5
print(' '.join(map(str, a)))

print"in new line"
print('\n'.join(map(str, a)))
