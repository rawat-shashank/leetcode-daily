import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dp = {}
        res = 0
        start = 0
        max_freq = 0
        for idx, ch in enumerate(s):
            dp[ch] = dp.get(ch, 0) + 1
            max_freq = max(max_freq, dp[ch])
            while (idx - start + 1) - max_freq > k:
                dp[s[start]] -= 1
                start += 1
            res = max(res, idx - start + 1)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.characterReplacement(s="ABAB", k=2),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.characterReplacement(s="AABABBA", k=1),
        )


if __name__ == "__main__":
    unittest.main()
