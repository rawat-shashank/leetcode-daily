# 2870. Minimum Number of Operations to Make Array Empty
import unittest
from typing import List
from math import ceil


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dp = {}
        for num in nums:
            dp[num] = dp.get(num, 0) + 1
        count = 0
        for key, value in dp.items():
            if value == 1:
                return -1
            count += ceil(value / 3)
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.minOperations(
            nums=[2, 3, 3, 2, 2, 4, 2, 3, 4]))

    def testcase2(self):
        self.assertEqual(-1, self.sol.minOperations(nums=[2, 1, 2, 2, 3, 3]))


if __name__ == "__main__":
    unittest.main()
