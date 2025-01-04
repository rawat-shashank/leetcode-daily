import unittest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        ans = []
        for num in nums:
            ans.append(mul)
            mul *= num
        mul = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= mul
            mul *= nums[i]
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [24, 12, 8, 6],
            self.sol.productExceptSelf(nums=[1, 2, 3, 4]),
        )

    def testcase2(self):
        self.assertEqual(
            [0, 0, 9, 0, 0],
            self.sol.productExceptSelf(nums=[-1, 1, 0, -3, 3]),
        )


if __name__ == "__main__":
    unittest.main()
