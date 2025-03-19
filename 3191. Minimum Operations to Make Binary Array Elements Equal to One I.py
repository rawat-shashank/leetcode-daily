import unittest
from typing import List


class Solution:
    def minOperations(self,  nums: List[int]) -> int:
        res = 0
        for i in range(2, len(nums)):
            if nums[i-2]==0:
                res += 1
                nums[i-2] ^= 1
                nums[i-1] ^= 1
                nums[i] ^= 1
        if sum(nums) == len(nums):
            return res
        return -1

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.minOperations(nums = [0,1,1,1,0,0]),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minOperations(nums = [0,1,1,1]),
        )


if __name__ == "__main__":
    unittest.main()
