import unittest
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []

        for i, j in intervals:
            start.append(i)
            end.append(j)

        start.sort()
        end.sort()

        i, j = 0, 0
        res = 0

        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            res = max(res, i - j)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3, self.sol.minGroups(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])
        )

    def testcase2(self):
        self.assertEqual(
            1, self.sol.minGroups(intervals=[[1, 3], [5, 6], [8, 10], [11, 13]])
        )


if __name__ == "__main__":
    unittest.main()
