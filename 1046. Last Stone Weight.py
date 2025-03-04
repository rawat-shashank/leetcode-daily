import unittest
from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            heappush(stones, stone1 - stone2)
        return abs(stones[0])



class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.lastStoneWeight(stones = [2,7,4,1,8,1]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.lastStoneWeight(stones=[1]),
        )


if __name__ == "__main__":
    unittest.main()
