from typing import List
import unittest
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        adj_arr = [[i + 1] for i in range(n)]

        def bfs():
            dq = deque()
            # first element with zero distance
            dq.append((0, 0))
            visited = set()
            visited.add((0, 0))
            while dq:
                curr, length = dq.popleft()
                if curr == n - 1:
                    return length
                for next in adj_arr[curr]:
                    if next not in visited:
                        # next element with added length of 1
                        dq.append((next, length + 1))
                        visited.add(next)

        ans = []
        for src, dest in queries:
            # append new query to adjcent element array to find faster path
            adj_arr[src].append(dest)
            ans.append(bfs())

        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [3, 2, 1],
            self.sol.shortestDistanceAfterQueries(
                n=5, queries=[[2, 4], [0, 2], [0, 4]]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 1],
            self.sol.shortestDistanceAfterQueries(n=4, queries=[[0, 3], [0, 2]]),
        )


if __name__ == "__main__":
    unittest.main()
