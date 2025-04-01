"""
A self-descriptive number is an integer n in given base b is b digits long in which each digit at position p (the most significant digit being at position 0 
and the least significant at position b – 1) counts how many times a digit p is in n.

For example in base 10, 6210001000 is a self descriptive number.

Explanation :
It is 10 digit number in base 10.
It has 6 at the position 0 and there are six 0s in 6210001000.
It has 2 at the position 1 and there are two 1s in 6210001000.
It has 1 at the position 2 and there is one 2s in 6210001000.
It has 0 at the position 3 and there are zero 3s in 6210001000.
It has 0 at the position 4 and there are zero 4s in 6210001000.
It has 0 at the position 5 and there are zero 5s in 6210001000.
It has 1 at the position 6 and there is one 6 in 6210001000.
It has 0 at the position 7 and there are zero 7s in 6210001000.
It has 0 at the position 8 and there are zero 8s in 6210001000.
It has 0 at the position 9 and there are zero 9s in 6210001000.

Self-describing numbers - Rosetta Code
    https://rosettacode.org/wiki/Self-describing_numbers#Python
Self Descriptive Number - GeeksforGeeks
    https://www.geeksforgeeks.org/self-descriptive-number/
"""


class Solution:
    def isSelfDescriptiveNumber(self, n):
        s = str(n)

        return all(s.count(str(i)) == int(c) for i, c in enumerate(s))

    def isSelfDescriptiveNumber2(self, n):
        s = str(n)

        for i in range(len(s)):
            c = s[i]

            # digit on position i
            b = ord(c) - ord('0')

            count = 0

            # count the occurrence of i in s
            for j in range(len(s)):
                temp = ord(s[j]) - ord('0')

                if temp == i:
                    count += 1

            if count != b:
                return False

        return True


if __name__ == '__main__':
    my_solution = Solution()

    print([x for x in range(4000000) if my_solution.isSelfDescriptiveNumber(x)])    # [1210, 2020, 21200, 3211000]

    print([x for x in range(4000000) if my_solution.isSelfDescriptiveNumber2(x)])    # [1210, 2020, 21200, 3211000]
