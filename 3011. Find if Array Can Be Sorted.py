from typing import List
import unittest


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countBits(n):
            return bin(n).count("1")

        prevMax = float("-inf")
        curMin = curMax = nums[0]

        for n in nums:
            if countBits(n) == countBits(curMin):
                curMin = min(curMin, n)
                curMax = max(curMax, n)
            else:
                if curMin < prevMax:
                    return False
                prevMax = curMax
                curMin = curMax = n

        if curMin < prevMax:
            return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canSortArray(nums=[8, 4, 2, 30, 15]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.canSortArray(nums=[1, 2, 3, 4, 5]),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.canSortArray(nums=[3, 16, 8, 4, 2]),
        )


if __name__ == "__main__":
    unittest.main()
