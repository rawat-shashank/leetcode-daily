import unittest
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans_sum = 0
        min_abs_val = float("inf")
        ngtv_count = 0
        for row in matrix:
            for num in row:
                ans_sum += abs(num)
                if num < 0:
                    ngtv_count += 1
                min_abs_val = min(min_abs_val, abs(num))
        if ngtv_count % 2 != 0:
            """converting to negative means, reduce sum by twice the number"""
            ans_sum -= 2 * min_abs_val
        return ans_sum


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.maxMatrixSum(matrix=[[1, -1], [-1, 1]]),
        )

    def testcase2(self):
        self.assertEqual(
            16,
            self.sol.maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]),
        )


if __name__ == "__main__":
    unittest.main()
