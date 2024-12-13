from typing import List
import unittest
from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: List[int]) -> int:
        """heap for smallest number, and hashmap for marked"""
        pairs = [(num, idx) for idx, num in enumerate(nums)]
        heapify(pairs)
        visited = set()
        score = 0
        while pairs:
            num, idx = heappop(pairs)
            if (num, idx) not in visited:
                visited.add((num, idx))
                score += num
                if idx > 0:
                    visited.add((nums[idx - 1], idx - 1))
                if idx < len(nums) - 1:
                    visited.add((nums[idx + 1], idx + 1))
        return score


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            7,
            self.sol.findScore(nums=[2, 1, 3, 4, 5, 2]),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.findScore(nums=[2, 3, 5, 1, 3, 2]),
        )


if __name__ == "__main__":
    unittest.main()
