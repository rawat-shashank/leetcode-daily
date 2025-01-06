import unittest
from typing import List


class Solution:

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     """brute force - TLE"""
    #
    #     def twoSum(nums: List[int], t: int) -> List[int]:
    #         dp = {}
    #         res = []
    #         for num in nums:
    #             if dp.get(t - num) == None:
    #                 dp[num] = num
    #             else:
    #                 res.append([t - num, num])
    #         return res
    #
    #     if all(x == 0 for x in nums):
    #         return [[0, 0, 0]]
    #     ans = set()
    #     for i in range(len(nums)):
    #         res = twoSum(nums[:i] + nums[i + 1 :], t=-nums[i])
    #         for x in res:
    #             x.append(nums[i])
    #             ans.add(tuple(sorted(x)))
    #     return [list(x) for x in ans]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """two pointer - two sum"""
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp_sum = nums[left] + num + nums[right]
                if tmp_sum == 0:
                    res.append([nums[left], num, nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertCountEqual(
            [[-1, -1, 2], [-1, 0, 1]],
            self.sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]),
        )

    def testcase2(self):
        self.assertCountEqual(
            [],
            self.sol.threeSum(nums=[0, 1, 1]),
        )

    def testcase3(self):
        self.assertCountEqual(
            [[0, 0, 0]],
            self.sol.threeSum(nums=[0, 0, 0]),
        )


if __name__ == "__main__":
    unittest.main()
