import unittest
from typing import List
from heapq import heappush, heappop


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """max heap, negative small number"""

        def cal_gains(p_stu, t_stu):
            return (p_stu + 1) / (t_stu + 1) - p_stu / t_stu

        max_heap = []
        for p_stu, t_stu in classes:
            gain = cal_gains(p_stu, t_stu)
            heappush(max_heap, (-gain, p_stu, t_stu))

        while extraStudents:
            extraStudents -= 1
            _, p_stu, t_stu = heappop(max_heap)
            heappush(max_heap, (-cal_gains(p_stu + 1, t_stu + 1), p_stu + 1, t_stu + 1))

        ans = 0
        while max_heap:
            _, t_stu, p_stu = heappop(max_heap)
            ans += t_stu / p_stu
        return ans / len(classes)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertAlmostEqual(
            0.78333,
            self.sol.maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2),
            places=5,
        )

    def testcase2(self):
        self.assertAlmostEqual(
            0.53485,
            self.sol.maxAverageRatio(
                classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4
            ),
            places=5,
        )


if __name__ == "__main__":
    unittest.main()
