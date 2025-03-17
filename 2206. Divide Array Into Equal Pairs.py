import unittest
from typing import List

class Solution:

    def divideArray(self, nums: list[int]) -> bool:
        #brute force
        dp = {}
        for num in nums:
            dp[num] = dp.get(num, 0) + 1
        for _, values in dp.items():
            if values % 2:
                return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            True,
            self.sol.divideArray(nums = [3,2,3,2,2,2]),
        )

    def testcase2(self):
        self.assertEqual(
            False,
            self.sol.divideArray(nums = [1,2,3,4]),
        )

if __name__ == "__main__":
    unittest.main()
