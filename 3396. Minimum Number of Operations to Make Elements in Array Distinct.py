from typing import List
import unittest


class Solution:
    # def minimumOperations(self, nums: list[int]) -> int:
    #     """brute force"""
    #     def checkUnique(start):
    #         seen = set()
    #         for num in nums[start:]:
    #             if num in seen:
    #                 return False
    #             seen.add(num)
    #         return True
    #
    #     res = 0
    #     for i in range(0, len(nums), 3):
    #         if checkUnique(i):
    #             return res
    #         res += 1
    #     return res

    def minimumOperations(self, nums: list[int]) -> int:
        """reverse traversal"""
        dp = {}
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in dp:
                return (i // 3) + 1
            dp[nums[i]] = 1
        return 0

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minimumOperations(nums = [1,2,3,4,2,3,3,5,7]),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.minimumOperations(nums = [4,5,6,4,4]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.minimumOperations(nums = [6,7,8,9]),
        )


if __name__ == "__main__":
    unittest.main()
