import unittest
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low < high:
            mid = (low + high) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8))

    def testcase2(self):
        self.assertEqual(30, self.sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))

    def testcase3(self):
        self.assertEqual(23, self.sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))


if __name__ == "__main__":
    unittest.main()
