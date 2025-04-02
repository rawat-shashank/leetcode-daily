# 2870. Minimum Number of Operations to Make Array Empty
import unittest
from typing import List


class Solution:
    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     """brute force"""
    #     res=0
    #     N = len(nums)
    #     for i in range(N):
    #         for j in range(i+1, N):
    #             for k in range(j + 1, N):
    #                 res = max(
    #                     res,
    #                     (nums[i] - nums[j]) * nums[k]
    #                 )
    #     return 0 if res <= 0 else res

    def maximumTripletValue(self, nums: List[int]) -> int:
        """greedy - imax, differenceMax"""
        res, imax, dmax = 0 , 0 ,0
        for k in nums:
            res = max(res, dmax*k)
            dmax= max(dmax, imax - k)
            imax = max(imax, k)
        return res

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(77, self.sol.maximumTripletValue(
            nums = [12,6,1,2,7]))

    def testcase2(self):
        self.assertEqual(133, self.sol.maximumTripletValue(nums=[1,10,3,4,19]))

    def testcase3(self):
        self.assertEqual(0, self.sol.maximumTripletValue(nums=[1,2,3]))

if __name__ == "__main__":
    unittest.main()
