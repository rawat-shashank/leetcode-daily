from typing import List
import unittest


class Solution:
    # def resultsArray(self, nums: List[int], k: int) -> List[int]:
    #     """ brute force accepted"""
    #     length = len(nums)
    #     ans = [0] * (length - k + 1)
    #
    #     for i in range(length - k + 1):
    #         is_consicutive = True
    #
    #         for j in range(i, i + k - 1):
    #             if nums[j + 1] != nums[j] + 1:
    #                 is_consicutive = False
    #                 break
    #         if is_consicutive:
    #             ans[i] = nums[i + k - 1]
    #         else:
    #             ans[i] = -1
    #     return ans

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # optimized to o(n)
        # using consicutive_sum
        # base case, no changes required
        if k == 1:
            return nums

        length = len(nums)
        ans = [-1] * (length - k + 1)
        consicutive_sum = 1
        for i in range(length - 1):
            if nums[i] + 1 == nums[i + 1]:
                consicutive_sum += 1
            else:
                consicutive_sum = 1
            if consicutive_sum >= k:
                ans[i - k + 2] = nums[i + 1]
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [3, 4, -1, -1, -1],
            self.sol.resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3),
        )

    def testcase2(self):
        self.assertEqual(
            [-1, 3, -1, 3, -1],
            self.sol.resultsArray(nums=[3, 2, 3, 2, 3, 2], k=2),
        )


if __name__ == "__main__":
    unittest.main()
