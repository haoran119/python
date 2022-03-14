"""
Find the Missing Number - GeeksforGeeks
    https://www.geeksforgeeks.org/find-the-missing-number/

You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list.
Write an efficient code to find the missing integer.

Example:

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
Explanation: The missing number from 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
Explanation: The missing number from 1 to 5 is 4
"""


class Solution:
    # The length of the array is n-1. So the sum of all n elements,
    # i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2.
    # Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers,
    # it will be the value of the missing element.
    # Time O(n) / Space O(1)
    def find_missing_number(self, input_list):
        if not input_list:
            return None

        n = len(input_list) + 1

        expected_sum = n * (n + 1) / 2
        actual_sum = sum(input_list)

        return int(expected_sum - actual_sum)

    # Modification for Overflow although it does not happen in Python3
    # The approach remains the same but there can be overflow if n is large.
    # In order to avoid integer overflow, pick one number from known numbers
    # and subtract one number from given numbers. This way there won’t have Integer Overflow ever.
    def find_missing_number2(self, input_list):
        if not input_list:
            return None

        total = len(input_list) + 1

        for i in range(len(input_list)):
            total += i + 1
            total -= input_list[i]

        return total

    def find_missing_number3(self, input_list):
        if not input_list:
            return None

        input_list.sort()

        for i in range(len(input_list)):
            if input_list[i] != i + 1:
                return i + 1


if __name__ == '__main__':
    my_solution = Solution()

    list_test = [1, 2, 4, 6, 3, 7, 8]

    result = my_solution.find_missing_number(list_test)
    print(result)   # 5
    result = my_solution.find_missing_number2(list_test)
    print(result)   # 5
    result = my_solution.find_missing_number3(list_test)
    print(result)   # 5
