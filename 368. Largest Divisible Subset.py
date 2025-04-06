import unittest
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        cache = {}

        def dfs(idx, prev):
            if idx == len(nums):
                return []
            if (idx, prev) in cache:
                return cache[(idx, prev)]

            # skip
            res = dfs(idx + 1, prev)
            if nums[idx] % prev == 0:
                choose = [nums[idx]] + dfs(idx + 1, nums[idx])
                res = choose if len(choose) > len(res) else res
            cache[(idx, prev)] = res
            return res

        return dfs(0, 1)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertCountEqual([1, 2], self.sol.largestDivisibleSubset(nums=[1, 2, 3]))

    def testcase2(self):
        self.assertCountEqual(
            [1, 2, 4, 8], self.sol.largestDivisibleSubset(nums=[1, 2, 4, 8])
        )


if __name__ == "__main__":
    unittest.main()
