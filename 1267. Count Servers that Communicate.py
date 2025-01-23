import unittest
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        """prefix sum"""
        ROWS = len(grid)
        COLS = len(grid[0])

        rows_cnt = [0] * ROWS
        cols_cnt = [0] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    rows_cnt[row] += 1
                    cols_cnt[col] += 1

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] and max(rows_cnt[row], cols_cnt[col]) > 1:
                    res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            0,
            self.sol.countServers(grid=[[1, 0], [0, 1]]),
        )

    def testcase2(self):
        self.assertEqual(
            3,
            self.sol.countServers(grid=[[1, 0], [1, 1]]),
        )

    def testcase3(self):
        self.assertEqual(
            4,
            self.sol.countServers(
                grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
