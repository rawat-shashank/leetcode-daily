import unittest
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        left, ans = 0, 0
        for idx, ch in enumerate(s):
            if ch in dp and left <= dp[ch]:
                left = dp[ch] + 1
            else:
                ans = max(ans, idx - left + 1)
            dp[ch] = idx
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.lengthOfLongestSubstring(s="abcabcbb"),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.lengthOfLongestSubstring(s="bbbbb"),
        )

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.lengthOfLongestSubstring(s="pwwkew"),
        )

    def testcase4(self):
        self.assertEqual(
            1,
            self.sol.lengthOfLongestSubstring(s=" "),
        )

    def testcase5(self):
        self.assertEqual(
            1,
            self.sol.lengthOfLongestSubstring(s="aa"),
        )

    def testcase6(self):
        self.assertEqual(
            0,
            self.sol.lengthOfLongestSubstring(s=""),
        )

    def testcase7(self):
        self.assertEqual(
            2,
            self.sol.lengthOfLongestSubstring(s="aab"),
        )

    def testcase8(self):
        self.assertEqual(
            3,
            self.sol.lengthOfLongestSubstring(s="dvdf"),
        )


if __name__ == "__main__":
    unittest.main()
