import unittest


class Solution:
    def countOfSubstrings(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        for ch in s:
            dp[ord(ch) - ord("a")] += 1
        while t:
            nxt = [0] * 26
            nxt[0] = dp[25]
            nxt[1] = (dp[25] + dp[0]) % MOD
            for i in range(2, 26):
                nxt[i] = dp[i - 1]
            dp = nxt
            t -= 1
        return sum(dp) % MOD


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(7, self.sol.countOfSubstrings(s="abcyy", t=2))

    def testcase2(self):
        self.assertEqual(5, self.sol.countOfSubstrings(s="azbk", t=1))


if __name__ == "__main__":
    unittest.main()
