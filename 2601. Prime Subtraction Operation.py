from typing import List
from math import sqrt
import unittest


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # helper function for primes
        def is_prime(n):
            for factor in range(2, int(sqrt(n)) + 1):
                if n % factor == 0:
                    return False
            return True

        primes = [0, 0]
        for i in range(2, max(nums)):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(primes[i - 1])

        prev = 0
        for n in nums:
            upper_bound = n - prev
            print(upper_bound)
            largest_prime = primes[upper_bound - 1]
            print(largest_prime, n - largest_prime)
            if n - largest_prime <= prev:
                return False
            prev = n - largest_prime
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.primeSubOperation(nums=[4, 9, 6, 10]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.primeSubOperation(nums=[6, 8, 11, 12]),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.primeSubOperation(nums=[5, 8, 3]),
        )

    def testcase4(self):
        self.assertTrue(
            self.sol.primeSubOperation(nums=[998, 2]),
        )


if __name__ == "__main__":
    unittest.main()
