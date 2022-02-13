#!/usr/bin/env python3

"""
https://www.geeksforgeeks.org/minimum-number-of-manipulations-required-to-make-two-strings-anagram-without-deletion-of-character/

An anagram is a word that can be obtained by rearranging the letters of another word, using all the constituent letters
exactly once. For example, the words "admirer" and "married" are anagrams of one another. However, the words "rather"
and "harder" are not anagrams, since "rather" does not contain the letter 'a' and "harder" does not contain the letter
't'. Two identical words are anagrams, too. You may also notice that the anagram of any word must be of the same length
as the word itself.

Bob has written two words, A and B, consisting of N and M letters, respectively. He would like them to be anagrams of
each other. Bob has decided to add some letters to these words to achieve his goal.

For example, given the words "rather" and "harder", Bob can add the letter 'a' to the first word and the letter 't' to
the second word. Having done this, the words are now anagrams.

Bob would like to add as few letters as possible. In the example above, Bob added two letters, which is the minimum
possible. Your task is to tell him the minimum number of letters that he needs to add to make the given words anagrams
in this way.

Write a function:

int solution(char *A, char *B) ;

that, given two non-empty strings, A and B, consisting of N and M letters respectively, returns the minimum number of
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
