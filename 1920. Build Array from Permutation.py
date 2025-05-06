import unittest


class Solution:

    def buildArray(self, nums: list[int]) -> list[int]:
        res = [-1] * len(nums)
        for idx, num in enumerate(nums):
            res[idx] = nums[num]
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [0, 1, 2, 4, 5, 3],
            self.sol.buildArray(nums=[0, 2, 1, 5, 3, 4]),
        )

    def testcase2(self):
        self.assertEqual(
            [4, 5, 0, 1, 2, 3],
            self.sol.buildArray(nums=[5, 0, 1, 2, 3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
