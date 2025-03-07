import unittest
from math import sqrt

class Solution:
    # def closestPrimes(self, left: int, right: int) -> list[int]:
    #     """TLE"""
    #     isPrime=lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])
    #
    #     res = [-1, -1]
    #     l = 0
    #     for i in range(left, right+1):
    #         if not isPrime(i):
    #             continue
    #         if not l:
    #             l = i
    #         elif res[0] != -1:
    #             if i-l < res[1] - res[0]:
    #                 res[0] = l
    #                 res[1] = i
    #         else:
    #             res[0] = l
    #             res[1] = i
    #         l = i
    #     return res

    def closestPrimes(self, left: int, right: int) -> list[int]:
        def get_primes():
            isPrime = [True] * (right+1)
            isPrime[0] = isPrime[1] = False

            for n in range(2, int(sqrt(right)) + 1):
                if not isPrime[n]:
                    continue
                for m in range(n+n, right+1, n):
                    isPrime[m] = False
            primes = []
            for i in range(left, right+1):
                if isPrime[i]:
                    primes.append(i)
            return primes

        primes= get_primes()
        res = [-1, -1]
        diff = right - left + 1
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < diff:
                diff = primes[i] - primes[i-1]
                res = [primes[i-1], primes[i]]
        return res



class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [11,13],
            self.sol.closestPrimes(left = 10, right = 19),
        )

    def testcase2(self):
        self.assertEqual([-1,-1], self.sol.closestPrimes(left = 4, right = 6))

    def testcase3(self):
        self.assertEqual(
            [29,31],
            self.sol.closestPrimes(left = 19, right = 31),
        )

    def testcase4(self):
        self.assertEqual(
            [1091,1093],
            self.sol.closestPrimes(left = 1087, right = 4441),
        )

if __name__ == "__main__":
    unittest.main()
