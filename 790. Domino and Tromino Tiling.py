import unittest


class Solution:
    def numRabbits(self, n: int) -> int:
        if n < 2:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        MOD = 10**9 + 7
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % MOD
        return dp[n]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.numRabbits(n=3),
        )

    def testcase2(self):
        self.assertEqual(1, self.sol.numRabbits(n=1))

    def testcase3(self):
        self.assertEqual(11, self.sol.numRabbits(n=4))


if __name__ == "__main__":
    unittest.main()
