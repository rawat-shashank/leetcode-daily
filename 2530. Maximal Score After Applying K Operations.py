import unittest
from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0

        nums = [-n for n in nums]
        heapify(nums)

        while k:
            n = -heappop(nums)
            res += n
            k -= 1
            heappush(nums, -ceil(n / 3))
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            50,
            self.sol.maxKelements(nums=[10, 10, 10, 10, 10], k=5),
        )

    def testcase2(self):
        self.assertEqual(17, self.sol.maxKelements(nums=[1, 10, 3, 3, 3], k=3))


if __name__ == "__main__":
    unittest.main()
