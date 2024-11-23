import unittest
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """row by row, with rotation at last"""
        for row in box:
            right = len(row) - 1
            left = right - 1
            while left >= 0:
                if row[left] == "#" and row[right] == ".":
                    row[left] = "."
                    row[right] = "#"
                    right -= 1
                if row[left] == "*":
                    right = left
                if row[right] == "*" or row[right] == "#":
                    right -= 1
                left -= 1

        return [list(reversed(col)) for col in zip(*box)]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [["."], ["#"], ["#"]],
            self.sol.rotateTheBox(box=[["#", ".", "#"]]),
        )

    def testcase2(self):
        self.assertEqual(
            [["#", "."], ["#", "#"], ["*", "*"], [".", "."]],
            self.sol.rotateTheBox(box=[["#", ".", "*", "."], ["#", "#", "*", "."]]),
        )

    def testcase3(self):
        self.assertEqual(
            [
                [".", "#", "#"],
                [".", "#", "#"],
                ["#", "#", "*"],
                ["#", "*", "."],
                ["#", ".", "*"],
                ["#", ".", "."],
            ],
            self.sol.rotateTheBox(
                box=[
                    ["#", "#", "*", ".", "*", "."],
                    ["#", "#", "#", "*", ".", "."],
                    ["#", "#", "#", ".", "#", "."],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
