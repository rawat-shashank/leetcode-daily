import unittest
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """dfs on graph"""
        safe = {}
        res = []

        def dfs(i: int) -> bool:
            if i in safe:
                return safe[i]

            safe[i] = False
            for next in graph[i]:
                if not dfs(next):
                    return safe[i]
            safe[i] = True
            return safe[i]

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [2, 4, 5, 6],
            self.sol.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]),
        )

    def testcase2(self):
        self.assertEqual(
            [4],
            self.sol.eventualSafeNodes(
                graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
            ),
        )


if __name__ == "__main__":
    unittest.main()
