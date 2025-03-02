import unittest


class Solution:
    # def applyOperations(self, nums: list[int]) -> list[int]:
    #     res: list[int] = []
    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1] and nums[i]:
    #             nums[i] *= 2
    #             nums[i+1] = 0
    #     for i in range(len(nums)):
    #         if nums[i]:
    #             res.append(nums[i])
    #     while len(res) < len(nums):
    #         res.append(0)
    #
    #     return res

    def applyOperations(self, nums: list[int]) -> list[int]:
        """optimized for in place"""
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        left: int = 0
        for num in nums:
            if num:
                nums[left] = num
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1
        return nums

class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        self.assertEqual(
            first=[1,4,2,0,0,0],
            second=Solution().applyOperations(nums = [1,2,2,1,1,0]),
        )

    def testcase2(self) -> None:
        self.assertEqual(
            first=[1,0],
            second=Solution().applyOperations(nums = [0,1]),
        )


if __name__ == "__main__":
    unittest.main()
