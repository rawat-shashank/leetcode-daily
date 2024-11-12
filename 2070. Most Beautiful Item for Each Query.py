from typing import List
from math import sqrt
import unittest


class Solution:
    # def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    #     # brute force solution, will time limit exceed
    #     res = []
    #
    #     for q in queries:
    #         maxB = 0
    #         for p, b in items:
    #             if p <= q:
    #                 maxB = max(maxB, b)
    #         res.append(maxB)
    #
    #     return res

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [0] * len(queries)
        maxB = 0
        j = 0
        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                maxB = max(maxB, items[j][1])
                j += 1
            res[i] = maxB
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [2, 4, 5, 5, 6, 6],
            self.sol.maximumBeauty(
                items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]],
                queries=[1, 2, 3, 4, 5, 6],
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [4],
            self.sol.maximumBeauty(items=[[1, 2], [1, 2], [1, 3], [1, 4]], queries=[1]),
        )

    def testcase3(self):
        self.assertEqual(
            [0],
            self.sol.maximumBeauty(items=[[10, 1000]], queries=[5]),
        )


if __name__ == "__main__":
    unittest.main()
