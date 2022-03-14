#!/usr/bin/env python3

"""
https://www.geeksforgeeks.org/minimum-number-of-manipulations-required-to-make-two-strings-anagram-without-deletion-of-character/

Given two strings s1 and s2, we need to find the minimum number of manipulations required to make two strings anagram without 
deleting any character. 

Given two non-empty strings, A and B, consisting of N and M letters respectively, returns the minimum number of
letters that Bob has to add to the words specified in A and B to make them anagrams.

for example, give the words "rather" and "harder" your function should return 2 as explained above

for the given words "apple" and "pear" your function should return 3 since you can add the letter 'r' to the first word
and letter 'p' and 'l' to the second word to form anagrams and for the given words "lemon" and "melon" your function
should return 0, since the given words are alredy anagram

assumme that
    n and m are integer within the range [1,100,00]
    string('a','b') consist only of lowercase letters(a-z)
"""


class Solution:
    def calculate_anagram_distance(self, A: str, B: str) -> int:
        char_count = [0] * 26
        result = 0

        for i in range(len(A)):
            char_count[ord(A[i]) - ord('a')] += 1

        for i in range(len(B)):
            char_count[ord(B[i]) - ord('a')] -= 1

        for count in char_count:
            result += abs(count)

        return result


if __name__ == '__main__':
    my_solution = Solution()
    inputs1 = "rather"
    inputs2 = "harder"

    result = my_solution.calculate_anagram_distance(inputs1, inputs2)
    print(result)

    inputs1 = "apple"
    inputs2 = "pear"

    result = my_solution.calculate_anagram_distance(inputs1, inputs2)
    print(result)
