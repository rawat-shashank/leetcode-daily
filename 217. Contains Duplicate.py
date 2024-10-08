import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == 0: return False
        dp = {}
        for num in nums:
            if num in dp:
                return True
            else:
                dp[num] = 1
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(True, self.sol.containsDuplicate(nums=[1, 2, 3, 1]))

    def testcase2(self):
        self.assertEqual(False, self.sol.containsDuplicate(nums=[1, 2, 3, 4]))

    def testcase3(self):
        self.assertEqual(
            True, self.sol.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        )


if __name__ == "__main__":
    unittest.main()
