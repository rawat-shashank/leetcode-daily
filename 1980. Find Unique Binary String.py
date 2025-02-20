import unittest
from typing import List


class Solution:
    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     """backtracking - accepted"""
    #     used = {s for s in nums}
    #
    #     def backtrack(curr):
    #         if len(curr) == len(nums):
    #             return None if curr in used else curr
    #
    #         # order won't matter for this problem, but it will go
    #         # from smaller to larger number
    #         for ch in ["0", "1"]:
    #             res = backtrack(curr + ch)
    #             if res:
    #                 return res
    #
    #     return backtrack("")

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """math - clever, fast, Cantor's Diagonal Argument"""
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.findDifferentBinaryString(nums=["01", "10"]) in ["00", "11"]
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.findDifferentBinaryString(nums=["00", "01"]) in ["10", "11"]
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.findDifferentBinaryString(nums=["111", "011", "001"])
            in ["000", "010", "100", "101", "110"]
        )


if __name__ == "__main__":
    unittest.main()
