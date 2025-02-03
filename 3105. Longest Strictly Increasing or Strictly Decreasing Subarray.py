import unittest
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        res = 0
        sign = 0
        count = 1
        for i in range(1, len(nums)):
            temp = nums[i] - nums[i - 1]
            print(temp, count, sign)
            if sign >= 0 and temp > 0:
                count += 1
                sign = 1
            elif sign <= 0 and temp < 0:
                count += 1
                sign = -1
            elif sign >= 0 and temp < 0:
                count = 2
                sign = -1
            elif sign <= 0 and temp > 0:
                count = 2
                sign = 1
            else:
                count = 1
                sign = 0
            res = max(res, count)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.longestMonotonicSubarray(nums=[3, 3, 3, 3]),
        )

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.longestMonotonicSubarray(nums=[3, 2, 1]),
        )

    def testcase4(self):
        self.assertEqual(
            2,
            self.sol.longestMonotonicSubarray(nums=[1, 1, 5]),
        )

    def testcase5(self):
        self.assertEqual(
            2,
            self.sol.longestMonotonicSubarray(nums=[6, 6, 3]),
        )

    def testcase6(self):
        self.assertEqual(
            3,
            self.sol.longestMonotonicSubarray(nums=[1, 9, 7, 1]),
        )


if __name__ == "__main__":
    unittest.main()
