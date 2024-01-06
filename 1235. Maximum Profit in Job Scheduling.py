# 1235. Maximum Profit in Job Scheduling
import unittest
from typing import List
from bisect import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(jobs):
                return 0
            if i in cache:
                return cache[i]

            # if we are not choosing the current job
            res = dfs(i + 1)

            # if we are choosing the current job
            # get the value of j
            j = bisect(jobs, (jobs[i][1], -1, -1))
            cache[i] = res = max(res, jobs[i][2] + dfs(j))
            return res

        return dfs(0)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            120,
            self.sol.jobScheduling(
                startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            150,
            self.sol.jobScheduling(
                startTime=[1, 2, 3, 4, 6],
                endTime=[3, 5, 10, 6, 9],
                profit=[20, 20, 100, 70, 60],
            ),
        )

    def testcase3(self):
        self.assertEqual(
            6,
            self.sol.jobScheduling(
                startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]
            ),
        )


if __name__ == "__main__":
    unittest.main()
