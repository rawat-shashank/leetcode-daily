import unittest
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        for row in range(rows - 1):
            for col in range(1, cols):
                points[row][col] = max(points[row][col], points[row][col-1]-1)
            for col in range(cols-2, -1, -1):
                points[row][col] = max(points[row][col], points[row][col+1]-1)
            for col in range(cols):
                print(points[row][col])
                points[row+1][col] += points[row][col]
        return max(points[-1])


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def testcase1(self):
        self.assertEqual(10, self.sol.maxPoints(points = [[1,3,2],[1,5,1],[3,1,1]]))

    def testcase2(self):
        self.assertEqual(11, self.sol.maxPoints(points = [[1,5],[2,3],[4,2]]))


if __name__ == "__main__":
    unittest.main()
