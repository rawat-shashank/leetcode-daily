# 1624. Largest Substring Between Two Equal Characters
import unittest


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dp = {}
        for i, ch in enumerate(s):
            if ch in dp:
                dp[ch].append(i)
            else:
                dp[ch] = [i]
        max_s = -1
        for key in dp.keys():
            if len(dp[key]) > 1:
                max_s = max(max_s, dp[key][-1] - dp[key][0] - 1)
        return max_s


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(0, self.sol.maxLengthBetweenEqualCharacters(s="aa"))

    def testcase2(self):
        self.assertEqual(2, self.sol.maxLengthBetweenEqualCharacters(s="abca"))

    def testcase3(self):
        self.assertEqual(-1,
                         self.sol.maxLengthBetweenEqualCharacters(s="cbzxy"))


if __name__ == "__main__":
    unittest.main()
