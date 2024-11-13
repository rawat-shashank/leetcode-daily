from typing import List
from math import sqrt
import unittest


class Solution:

    # def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    #     """Brute force, time limit exceded"""
    #     nums = sorted([(num, i) for i, num in enumerate(nums)])
    #     left, right = 0, 1
    #     res = []
    #     while left < len(nums) - 1:
    #         num1, i1 = nums[left]
    #         num2, i2 = nums[right]
    #         sum = num1 + num2
    #         if lower > sum:
    #             right += 1
    #         elif upper < sum:
    #             left += 1
    #             right = left + 1
    #         else:
    #             res.append((i1, i2))
    #             right += 1
    #
    #         if right >= len(nums):
    #             left += 1
    #             right = left + 1
    #     return len(res)

    # helper function
    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums: List[int], value: int) -> int:
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            # If sum is less than value, add the size of window to result and move to the
            # next index.
            if sum < value:
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1
        return result

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            6,
            self.sol.countFairPairs(nums=[0, 1, 7, 4, 4, 5], lower=3, upper=6),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.countFairPairs(nums=[1, 7, 9, 2, 5], lower=11, upper=11),
        )


if __name__ == "__main__":
    unittest.main()
