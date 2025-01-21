import unittest
from typing import List


class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        min_sum = float("inf")
        for i in range(len(grid[0])):
            first_row_sum -= grid[0][i]
            min_sum = min(min_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][i]
        return min_sum


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.gridGame(grid=[[2, 5, 4], [1, 5, 1]]),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.gridGame(grid=[[3, 3, 1], [8, 5, 2]]),
        )

    def testcase3(self):
        self.assertEqual(
            7,
            self.sol.gridGame(grid=[[1, 3, 1, 15], [1, 3, 3, 1]]),
        )


if __name__ == "__main__":
    unittest.main()
