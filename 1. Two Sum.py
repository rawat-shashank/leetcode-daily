import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for idx, num in enumerate(nums):
            if num in dp:
                return [dp[num], idx]
            else:
                dp[target - num] = idx


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual([0, 1], self.sol.twoSum(nums=[2, 7, 11, 15], target=9))

    def testcase2(self):
        self.assertEqual([1, 2], self.sol.twoSum(nums=[3, 2, 4], target=6))

    def testcase3(self):
        self.assertEqual([0, 1], self.sol.twoSum(nums=[3, 3], target=6))


if __name__ == "__main__":
    unittest.main()
