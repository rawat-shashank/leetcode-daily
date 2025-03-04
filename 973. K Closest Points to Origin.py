from typing import List
import unittest
from heapq import heappush, heappop


class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     # using min heap
    #     heap = []
    #     for x, y in points:
    #         heappush(heap, ((x**2)+ (y**2), x, y))
    #
    #     res = []
    #     while k:
    #         _, x, y = heappop(heap) 
    #         res.append([x, y])
    #         k-=1
    #     return res

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using sorting based on same parameter
        points.sort(key=lambda k:k[0]**2+k[1]**2)
        return points[:k]

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual([[-2,2]], self.sol.kClosest(points = [[1,3],[-2,2]], k = 1))

    def testcase2(self):
        self.assertEqual(
            [[3,3],[-2,4]],
            self.sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2),
        )


if __name__ == "__main__":
    unittest.main()
