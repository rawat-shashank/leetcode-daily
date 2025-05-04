import unittest
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        res = 0
        dp = defaultdict(int)
        for x, y in dominoes:
            val = x * 10 + y if x > y else y * 10 + x
            res += dp[val]
            dp[val] = dp.get(val) + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]),
        )

    def testcase2(self):
        self.assertEqual(
            3,
            self.sol.numEquivDominoPairs(
                dominoes=[[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
