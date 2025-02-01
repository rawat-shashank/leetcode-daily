from typing import List
import unittest


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isArraySpecial(nums=[1]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.isArraySpecial(nums=[2, 1, 4]),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.isArraySpecial(nums=[4, 3, 1, 6]),
        )


if __name__ == "__main__":
    unittest.main()
