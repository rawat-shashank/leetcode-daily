import unittest
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # recursive top down dfs
        # dp = {len(days): 0}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = float("inf")
        #     j = i
        #     for cost, duration in zip(costs, [1, 7, 30]):
        #         print(cost, duration, i, j)
        #         while j < len(days) and days[j] < days[i] + duration:
        #             j += 1
        #         dp[i] = min(dp[i], cost + dfs(j))
        #     return dp[i]
        # return dfs(0)

        # dynamic bottom up
        dp = [0] * (len(days) + 1)
        for i in range(len(days) - 1, -1, -1):
            j = i
            dp[i] = float("inf")
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            11, self.sol.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15])
        )

    def testcase2(self):
        self.assertEqual(
            17,
            self.sol.mincostTickets(
                days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]
            ),
        )


if __name__ == "__main__":
    unittest.main()
