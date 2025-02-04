import unittest
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                sum += nums[i]
            else:
                sum = nums[i]
            maxSum = max(maxSum, sum)
        return maxSum


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            65,
            self.sol.maxAscendingSum(nums=[10, 20, 30, 5, 10, 50]),
        )

    def testcase2(self):
        self.assertEqual(
            150,
            self.sol.maxAscendingSum(nums=[10, 20, 30, 40, 50]),
        )

    def testcase3(self):
        self.assertEqual(
            33,
            self.sol.maxAscendingSum(nums=[12, 17, 15, 13, 10, 11, 12]),
        )

    def testcase4(self):
        self.assertEqual(
            100,
            self.sol.maxAscendingSum(nums=[100, 10, 1]),
        )

    def testcase5(self):
        self.assertEqual(
            19,
            self.sol.maxAscendingSum(nums=[3, 6, 10, 1, 8, 9, 9, 8, 9]),
        )


if __name__ == "__main__":
    unittest.main()
