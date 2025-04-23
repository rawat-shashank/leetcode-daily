import unittest


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = {}
        for i in range(n):
            key = sum([int(x) for x in str(i + 1)])
            dp[key] = dp.get(key, 0) + 1
        MAX = max(dp.values())
        res = sum([1 for x in dp.values() if x == MAX])
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.countLargestGroup(n=13),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.countLargestGroup(n=2),
        )


if __name__ == "__main__":
    unittest.main()
