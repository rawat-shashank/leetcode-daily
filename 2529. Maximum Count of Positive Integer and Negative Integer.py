import unittest

class Solution:
    # def maximumCount(self, nums: list[int]) -> int:
    #     negative_count = 0
    #     positive_count = 0
    #     res = 0
    #     for num in nums:
    #         if num == 0:
    #             continue
    #         if num < 0:
    #             negative_count += 1
    #         if num > 0:
    #             positive_count += 1
    #     return positive_count if positive_count > negative_count else negative_count

    def maximumCount(self, nums: list[int]) -> int:
        left = 0
        neg = 0
        while nums and nums[left] < 0:
            left += 1
        neg = left
        while nums and nums[left] == 0:
            left += 1
        pos = len(nums) - left
        return max(pos, neg)

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.maximumCount(nums = [-2,-1,-1,1,2,3]),
        )

    def testcase2(self):
        self.assertEqual(3, self.sol.maximumCount(nums = [-3,-2,-1,0,0,1,2]))

    def testcase3(self):
        self.assertEqual(
            4,
            self.sol.maximumCount(nums = [5,20,66,1314]),
        )

if __name__ == "__main__":
    unittest.main()
