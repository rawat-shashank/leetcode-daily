from typing import List
import unittest
from heapq import heapify, heappop, heappush
from math import isqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        nums = [-num for num in gifts]
        heapify(nums)
        while k:
            num = -heappop(nums)
            heappush(nums, -isqrt(num))
            k -= 1
        return -sum(nums)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            29,
            self.sol.pickGifts(gifts=[25, 64, 9, 4, 100], k=4),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.pickGifts(gifts=[1, 1, 1, 1], k=4),
        )


if __name__ == "__main__":
    unittest.main()
