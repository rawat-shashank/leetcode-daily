# 2125. Number of Laser Beams in a Bank
import unittest
from typing import List


class Solution:
    # def mostPoints(self, questions: List[List[int]]) -> int:
    #     """backtracking with cache"""
    #     cache = [0] * len(questions)
    #
    #     def backtrack(idx):
    #         if idx >= len(questions):
    #             return 0
    #
    #         if cache[idx]:
    #             return cache[idx]
    #
    #         point, brainpower = questions[idx]
    #         # if you skip current index
    #         skip = backtrack(idx + 1)
    #         # else, if we select current index
    #         choose = point + backtrack(idx + 1 + brainpower)
    #         cache[idx] = max(skip, choose)
    #         return cache[idx]
    #
    #     return backtrack(0)

    def mostPoints(self, questions: List[List[int]]) -> int:
        """bottom up approach using dp"""
        N = len(questions)
        cache = [0] * (N + 1)
        for idx in range(N - 1, -1, -1):
            points, brainpower = questions[idx]
            next_idx = idx + 1 + brainpower
            cache[idx] = max(
                # skip current question
                cache[idx + 1],
                # choose current question
                points + (cache[next_idx] if next_idx < N else 0),
            )
        return cache[0]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5, self.sol.mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]])
        )

    def testcase2(self):
        self.assertEqual(
            7, self.sol.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        )


if __name__ == "__main__":
    unittest.main()
