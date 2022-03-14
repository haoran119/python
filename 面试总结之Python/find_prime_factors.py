"""
Efficient program to print all prime factors of a given number
https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

Prime Numbers - GeeksforGeeks
https://www.geeksforgeeks.org/prime-numbers/

Given a number n, write an efficient function to print all prime factors of n.
For example, if the input number is 12, then output should be “2 2 3”.
And if the input number is 315, then output should be “3 3 5 7”.
"""

import math


class Solution:
    def find_prime_factors(self, data: int) -> list:
        """Following are the steps to find all prime factors.
        1) While n is divisible by 2, print 2 and divide n by 2.
        2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n.
        While i divides n, print i and divide n by i. After i fails to divide n, increment i by 2 and continue.
        3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps.
        So print n if it is greater than 2.
        """

        if data < 2:
            return []

        results = []

        while data % 2 == 0:
            data /= 2
            results.append(2)

        for i in range(3, int(math.sqrt(data) + 1), 2):
            while data % i == 0:
                data /= i
                results.append(i)

        if data > 2:
            results.append(int(data))

        return results

    def generate_primes(self, n: int) -> list:
        if n == 2:
            return [2]

        primes = []

        for i in range(2, n + 1):
            is_prime = True

            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(i)

        print('primes = {}'.format(primes))

        return primes

    def find_prime_factors1(self, data: int) -> list:
        primes = self.generate_primes(data)
        results = []
        self.found = False

        def dfs(num):
            if num == 1:
                self.found = True
                return

            for i in primes:
                if num % i == 0:
                    results.append(i)
                    dfs(num / i)
                    if self.found:
                        return
                    results.pop()

            return

        dfs(data)

        return results

    def find_prime_factors2(self, data: int) -> list:
        if data == 2:
            return [2]

        primes = self.generate_primes(data)
        results, temp = [], []

        def dfs(num):
            if num == 1:
                # should not append temp directly as it will be changed due to reference
                results.append(temp[:])
                return

            for i in primes:
                if num % i == 0:
                    temp.append(i)
                    dfs(num / i)
                    temp.pop()

        dfs(data)

        return results[0] if results else results


if __name__ == '__main__':
    my_solution = Solution()

    inputs = [0, 1, 2, 3, 12, 60, 315]

    # 0
    # []
    # primes = []
    # 1
    # []
    # primes = []
    # 2
    # [2]
    # 3
    # [3]
    # primes = [2, 3]
    # 12
    # [2, 2, 3]
    # primes = [2, 3, 5, 7, 11]
    # 60
    # [2, 2, 3, 5]
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    # 315
    # [3, 3, 5, 7]
    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
    for i in inputs:
        print(i)
        results = my_solution.find_prime_factors(i)
        print(results)
        results = my_solution.find_prime_factors1(i)
        print(results)
        results = my_solution.find_prime_factors2(i)
        print(results)
