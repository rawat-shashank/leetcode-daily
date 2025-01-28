import unittest
from typing import List


class Solution:

    def findMaxFish(self, grid: List[List[int]]) -> int:
        """dfs - easy"""

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # check if grid[r][c] is empty of out of bound or already in visited,
            # don't want to add it res again as we are going depth first

            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            res = grid[r][c]
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dir in dirs:
                nr, nc = dir
                res += dfs(nr, nc)
            return res

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, dfs(row, col))
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            7,
            self.sol.findMaxFish(
                grid=[[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.findMaxFish(
                grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
