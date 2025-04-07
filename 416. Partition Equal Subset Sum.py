import unittest


class Solution:
    # def canPartition(self, nums: list[int]) -> bool:
    #     """dp"""
    #
    #     total = sum(nums)
    #     # check for odd sum
    #     if total % 2:
    #         return False
    #
    #     dp = set()
    #     dp.add(0)
    #     target = total // 2
    #     for i in range(len(nums) -1, -1, -1):
    #         nextDP = set()
    #         for t in dp:
    #             if (t + nums[i]) == target:
    #                 return True
    #             nextDP.add(t+nums[i])
    #             nextDP.add(t)
    #         dp = nextDP
    #     return True if target in dp else False

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = 1 << 0
        for num in nums:
            dp |= dp << num
        return (dp & (1 << target)) != 0

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canPartition(nums = [1,5,11,5]),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.canPartition(nums = [1,2,3,5]),
        )


if __name__ == "__main__":
    unittest.main()
