import unittest
from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """using inbuilt min heap"""
        heapify(nums)
        res = 0
        while nums[0] < k:
            num1 = heappop(nums)
            num2 = heappop(nums)
            heappush(nums, num1 * 2 + num2)
            res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minOperations(nums=[2, 11, 10, 1, 3], k=10),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.minOperations(nums=[1, 1, 2, 4, 9], k=20),
        )


if __name__ == "__main__":
    unittest.main()
