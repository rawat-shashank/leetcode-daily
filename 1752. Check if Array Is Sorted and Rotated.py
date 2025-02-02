import unittest
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        """in a roated sorted array, there could only be one inversion
        of numbers"""
        if len(nums) < 2:
            return True

        inversion = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                inversion += 1

        if nums[0] < nums[-1]:
            inversion += 1

        return inversion < 2


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.check(nums=[3, 4, 5, 1, 2]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.check(nums=[1, 2, 3]),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.check(nums=[2, 1, 3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
