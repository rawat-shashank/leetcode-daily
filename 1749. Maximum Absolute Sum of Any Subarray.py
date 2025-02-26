import unittest
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefixSum, minPrefixSum,  maxPrefixSum = 0, 0, 0
        for num in nums:
            prefixSum += num
            minPrefixSum = min(minPrefixSum, prefixSum)
            maxPrefixSum = max(maxPrefixSum, prefixSum)
        return maxPrefixSum - minPrefixSum


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.maxAbsoluteSum(nums=[1, -3, 2, 3, -4]),
        )

    def testcase2(self):
        self.assertEqual(
            8,
            self.sol.maxAbsoluteSum(nums=[2, -5, 1, -4, 3, -2]),
        )


if __name__ == "__main__":
    unittest.main()
