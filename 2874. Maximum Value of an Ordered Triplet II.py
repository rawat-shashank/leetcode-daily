import unittest
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """greedy - imax, differenceMax"""
        highestSeen = 0
        highestDiff = 0
        ans = 0
        for num in nums:
            if highestDiff*num > ans:
                ans = highestDiff*num
            if highestSeen-num > highestDiff:
                highestDiff = highestSeen-num
            if num > highestSeen:
                highestSeen = num
        return ans

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
