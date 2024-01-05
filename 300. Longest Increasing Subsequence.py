# 300. Longest Increasing Subsequence
import unittest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        num_len = len(nums)
        ans = [1] * num_len
        for i in range(num_len - 1, -1, -1):
            for j in range(i + 1, num_len):
                if nums[j] > nums[i]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return max(ans)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))

    def testcase2(self):
        self.assertEqual(4, self.sol.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))

    def testcase3(self):
        self.assertEqual(1, self.sol.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))


if __name__ == "__main__":
    unittest.main()
