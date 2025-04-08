import unittest
from typing import List


class Solution:
    # def subsetXORSum(self, nums: List[int]) -> int:
    #     """backtracking"""
    #
    #     def backtrack(index, curr):
    #         if index == len(nums):
    #             return curr
    #
    #         # skip current element
    #         skip = backtrack(index + 1, curr)
    #         # choose current element
    #         choose = backtrack(index + 1, curr ^ nums[index])
    #
    #         return skip + choose
    #
    #     return backtrack(0, 0)

    def subsetXORSum(self, nums: List[int]) -> int:
        """bit manipulation"""
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums) - 1)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            6,
            self.sol.subsetXORSum(nums=[1, 3]),
        )

    def testcase2(self):
        self.assertEqual(
            28,
            self.sol.subsetXORSum(nums=[5, 1, 6]),
        )

    def testcase3(self):
        self.assertEqual(
            480,
            self.sol.subsetXORSum(nums=[3, 4, 5, 6, 7, 8]),
        )


if __name__ == "__main__":
    unittest.main()
