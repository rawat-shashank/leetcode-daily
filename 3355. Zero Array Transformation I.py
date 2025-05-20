import unittest


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """differnce array - range update in O(1)"""
        diffArray = [0] * (len(nums) + 1)
        for l, r in queries:
            diffArray[l] += 1
            diffArray[r + 1] -= 1
        diffSum = 0
        for idx, val in enumerate(nums):
            diffSum += diffArray[idx]
            if diffSum < val:
                return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.isZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3], [0, 2]]),
        )


if __name__ == "__main__":
    unittest.main()
