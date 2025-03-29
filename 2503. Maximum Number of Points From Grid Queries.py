import unittest
from heapq import heappop, heappush


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:

        # step 1, setting up sorted queries
        ROWS, COLS = len(grid), len(grid[0])
        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()

        # setting up a new heap with (val, row, col)
        heap = [(grid[0][0], 0, 0)]
        # set it with initial value
        visit = set([(0, 0)])
        res = [0] * len(queries)
        points = 0

        for limit, index in q:
            # current val in heap is smaller than limit of query
            while heap and heap[0][0] < limit:
                val, r, c = heappop(heap)
                points += 1
                neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for nr, nc in neighbors:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                        heappush(heap, (grid[nr][nc], nr, nc))
                        visit.add((nr, nc))
            res[index] = points
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [5, 8, 1],
            self.sol.maxPoints(
                grid=[[1, 2, 3], [2, 5, 7], [3, 5, 1]], queries=[5, 6, 2]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [0],
            self.sol.maxPoints(grid=[[5, 2, 1], [1, 1, 2]], queries=[3]),
        )


if __name__ == "__main__":
    unittest.main()
