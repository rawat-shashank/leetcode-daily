import unittest
from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pairs = [(num, idx) for idx, num in enumerate(nums)]
        heapify(pairs)
        while k:
            k -= 1
            num, idx = heappop(pairs)
            num *= multiplier
            nums[idx] = num
            heappush(pairs, (num, idx))
        return nums


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [8, 4, 6, 5, 6],
            self.sol.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2),
        )

    def testcase2(self):
        self.assertEqual(
            [16, 8],
            self.sol.getFinalState(nums=[1, 2], k=3, multiplier=4),
        )


if __name__ == "__main__":
    unittest.main()
