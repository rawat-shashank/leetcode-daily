import unittest
from heapq import heappop, heappush


class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        N, M = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * M for _ in range(N)]
        q = [(0, 0, 0)]
        while q:
            t, r, c = heappop(q)
            if t >= dp[r][c]:
                continue
            if r == N - 1 and c == M - 1:
                return t
            dp[r][c] = t
            for nr, nc in DIRS:
                nr = r + nr
                nc = c + nc
                if 0 <= nr < N and 0 <= nc < M and dp[nr][nc] == float("inf"):
                    nt = max(moveTime[nr][nc], t) + ((r + c) % 2) + 1
                    heappush(q, (nt, nr, nc))
        return -1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(7, self.sol.minTimeToReach(moveTime=[[0, 4], [4, 4]]))

    def testcase2(self):
        self.assertEqual(
            6, self.sol.minTimeToReach(moveTime=[[0, 0, 0, 0], [0, 0, 0, 0]])
        )

    def testcase3(self):
        self.assertEqual(
            4,
            self.sol.minTimeToReach(moveTime=[[0, 1], [1, 2]]),
        )


if __name__ == "__main__":
    unittest.main()
