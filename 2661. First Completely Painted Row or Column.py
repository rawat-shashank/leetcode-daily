import unittest
from typing import List


class Solution:

    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        mat_pos = {}
        for r in range(ROWS):
            for c in range(COLS):
                mat_pos[mat[r][c]] = (r, c)

        row_counts = [0] * ROWS
        col_counts = [0] * COLS

        for i in range(len(arr)):
            r, c = mat_pos[arr[i]]
            row_counts[r] += 1
            col_counts[c] += 1

            if col_counts[c] == ROWS or row_counts[r] == COLS:
                return i


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.firstCompleteIndex(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]]),
        )

    def testcase2(self):
        self.assertEqual(
            3,
            self.sol.firstCompleteIndex(
                arr=[2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
