import unittest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = set(nums)
        ans = 0
        # check only the num in set
        for num in dp:
            # make sure one smaller no is not in set
            if num - 1 not in dp:
                curr = 1
                # check if the next no is in dp
                while (num + curr) in dp:
                    curr += 1
                ans = max(ans, curr)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]),
        )

    def testcase2(self):
        self.assertEqual(
            9,
            self.sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]),
        )


if __name__ == "__main__":
    unittest.main()
