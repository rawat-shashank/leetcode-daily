import unittest
from typing import List
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        res = [[-1] * COLS for _ in range(ROWS)]

        q = deque()

        # set the initial points for water to 0
        for row in range(ROWS):
            for col in range(COLS):
                if isWater[row][col]:
                    res[row][col] = 0
                    q.append((row, col))

        # run a bfs starting from water points
        while q:
            row, col = q.popleft()

            dir = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            # check all neighbour and if it is already visited i.e. height is set
            for nr, nc in dir:
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or res[nr][nc] != -1:
                    continue
                res[nr][nc] = res[row][col] + 1
                q.append((nr, nc))
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [[1, 0], [2, 1]],
            self.sol.highestPeak(isWater=[[0, 1], [0, 0]]),
        )

    def testcase2(self):
        self.assertEqual(
            [[1, 1, 0], [0, 1, 1], [1, 2, 2]],
            self.sol.highestPeak(isWater=[[0, 0, 1], [1, 0, 0], [0, 0, 0]]),
        )


if __name__ == "__main__":
    unittest.main()
