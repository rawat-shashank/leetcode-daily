import unittest
from typing import List
from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {1: [0, 1], 2: [0, -1], 3: [1, 0], 4: [-1, 0]}
        num_rows, num_cols = len(grid), len(grid[0])

        # track minimum cost
        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        q = deque([(0, 0)])

        while q:
            row, col = q.popleft()

            for dir in directions:
                dr, dc = directions[dir]
                nr, nc = row + dr, col + dc

                cost = 0 if grid[row][col] == dir else 1
                if (
                    0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and min_cost[row][col] + cost < min_cost[nr][nc]
                ):
                    min_cost[nr][nc] = min_cost[row][col] + cost

                    if cost == 1:
                        q.append((nr, nc))
                    else:
                        q.appendleft((nr, nc))
        return min_cost[num_rows - 1][num_cols - 1]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.minCost(
                grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]),
        )

    def testcase3(self):
        self.assertEqual(
            1,
            self.sol.minCost(grid=[[1, 2], [4, 3]]),
        )


if __name__ == "__main__":
    unittest.main()
