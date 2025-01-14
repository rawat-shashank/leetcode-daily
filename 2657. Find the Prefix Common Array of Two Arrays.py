import unittest
from typing import List
from collections import defaultdict


class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        dp = defaultdict()
        tmp = 0
        for x, y in zip(A, B):
            dp[x] = dp.get(x, 0) + 1
            if dp[x] == 2:
                tmp += 1
            dp[y] = dp.get(y, 0) + 1
            if dp[y] == 2:
                tmp += 1
            ans.append(tmp)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [0, 2, 3, 4],
            self.sol.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4]),
        )

    def testcase2(self):
        self.assertEqual(
            [0, 1, 3],
            self.sol.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2]),
        )


if __name__ == "__main__":
    unittest.main()
