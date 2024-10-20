from typing import List
import unittest


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """Recursion DFS - brute force"""
        max_or = 0

        for n in nums:
            max_or |= n

        cache = [[-1] * (max_or + 1) for _ in range(len(nums))]

        def dfs(i, cur_or):
            nonlocal max_or
            if i == len(nums):
                return 1 if cur_or == max_or else 0
            if cache[i][cur_or] != -1:
                return cache[i][cur_or]

            cache[i][cur_or] = dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])

            return cache[i][cur_or]

        return dfs(0, 0)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.countMaxOrSubsets(nums=[3, 1]),
        )

    def testcase2(self):
        self.assertEqual(7, self.sol.countMaxOrSubsets(nums=[2, 2, 2]))

    def testcase3(self):
        self.assertEqual(6, self.sol.countMaxOrSubsets(nums=[3, 2, 1, 5]))


if __name__ == "__main__":
    unittest.main()
