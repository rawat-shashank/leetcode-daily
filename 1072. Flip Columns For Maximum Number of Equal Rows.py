import unittest
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """hashmap of row's complement"""
        ans = {}

        for row in matrix:
            pattern = "".join(["0" if n == row[0] else "1" for n in row])

            ans[pattern] = ans.get(pattern, 0) + 1

        return max(ans.values(), default=0)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.maxEqualRowsAfterFlips(matrix=[[0, 1], [1, 1]]),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.maxEqualRowsAfterFlips(matrix=[[0, 1], [1, 0]]),
        )

    def testcase3(self):
        self.assertEqual(
            2,
            self.sol.maxEqualRowsAfterFlips(matrix=[[0, 0, 0], [0, 0, 1], [1, 1, 0]]),
        )


if __name__ == "__main__":
    unittest.main()
