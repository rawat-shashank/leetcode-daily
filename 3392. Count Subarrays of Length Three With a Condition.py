import unittest


class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        """brute force"""
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == 2 * (nums[i - 1] + nums[i + 1]):
                res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.countSubarrays(nums=[1, 2, 1, 4, 1]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.countSubarrays(nums=[7, 8, -3]),
        )


if __name__ == "__main__":
    unittest.main()
