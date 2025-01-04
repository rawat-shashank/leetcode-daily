import unittest
from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isValidSudoku(
                board=[
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.isValidSudoku(
                board=[
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            ),
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.isValidSudoku(
                board=[
                    [".", "8", "7", "6", "5", "4", "3", "2", "1"],
                    ["2", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
                    ["9", ".", ".", ".", ".", ".", ".", ".", "."],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
