import unittest
from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)
        while start < end:
            row = (start + end) // 2
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                break
            if target > matrix[row][-1]:
                start = row + 1
            if target < matrix[row][-1]:
                end = row
        start, end = 0, len(matrix[0])
        while start < end:
            mid = (start + end) // 2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                start = mid + 1
            if target < matrix[row][mid]:
                end = mid
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.searchMatrix(
                matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
            ),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.searchMatrix(
                matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
            ),
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.searchMatrix(matrix=[[1]], target=1),
        )


if __name__ == "__main__":
    unittest.main()
