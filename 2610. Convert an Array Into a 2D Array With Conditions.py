# 2610. Convert an Array Into a 2D Array With Conditions
import unittest
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dp = {}
        for num in nums:
            dp[num] = dp.get(num, 0) + 1
        ans = []
        for key in dp.keys():
            i = 0
            while i < dp[key]:
                try:
                    ans[i].append(key)
                except IndexError:
                    ans.append([key])
                i += 1
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        a = {(frozenset(item)) for item in [[1, 3, 4, 2], [1, 3], [1]]}
        b = {
            (frozenset(item))
            for item in self.sol.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1])
        }
        self.assertEqual(a, b)

    def testcase2(self):
        a = {(frozenset(item)) for item in [[4, 3, 2, 1]]}
        b = {(frozenset(item))
             for item in self.sol.findMatrix(nums=[1, 2, 3, 4])}

        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
