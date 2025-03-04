from typing import List
import unittest
from heapq import heappop, heapify


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     res = []
    #     for num in nums:
    #         heappush(res, num)
    #     while len(res)> k:
    #         heappop(res)
    #     return res[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        while k>1:
            heappop(nums)
            k-=1
        return -heappop(nums)

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(5, self.sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4),
        )


if __name__ == "__main__":
    unittest.main()

