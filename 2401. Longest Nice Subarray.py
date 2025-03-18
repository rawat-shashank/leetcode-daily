import unittest
from typing import List
from collections import deque


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        bitmask = 0
        left = 0
        for right in range(len(nums)):
            while bitmask & nums[right]:
                bitmask = bitmask ^ nums[left]
                left += 1
            res = max(res, right - left + 1)
            bitmask = bitmask ^ nums[right]
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.longestNiceSubarray(nums = [1,3,8,48,10]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.longestNiceSubarray(nums = [3,1,5,11,13]),
        )


if __name__ == "__main__":
    unittest.main()
