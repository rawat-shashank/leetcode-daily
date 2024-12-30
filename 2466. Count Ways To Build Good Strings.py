import unittest


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {0: 1}
        for i in range(1, high + 1):
            dp[i] = dp.get(i - one, 0) + dp.get(i - zero, 0)
        return sum([dp[i] for i in range(low, high + 1)]) % mod


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.countGoodStrings(low=3, high=3, zero=1, one=1),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.countGoodStrings(low=2, high=3, zero=1, one=2),
        )


if __name__ == "__main__":
    unittest.main()
