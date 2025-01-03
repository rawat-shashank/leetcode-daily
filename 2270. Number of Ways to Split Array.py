import unittest
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for idx in range(len(nums) - 1, -1, -1):
            prefix_sum[idx] = nums[idx] + prefix_sum[idx + 1]
        count = 0
        sum = 0
        for idx in range(len(nums) - 1):
            sum = sum + nums[idx]
            if sum >= prefix_sum[idx + 1]:
                count += 1
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.waysToSplitArray(nums=[10, 4, -8, 7]),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.waysToSplitArray(nums=[2, 3, 1, 0]),
        )

    def testcase3(self):
        self.assertEqual(
            1,
            self.sol.waysToSplitArray(nums=[9, 9, 9]),
        )

    def testcase4(self):
        self.assertEqual(
            1,
            self.sol.waysToSplitArray(nums=[1, 1, 1, 2, 3]),
        )


if __name__ == "__main__":
    unittest.main()
