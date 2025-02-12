import unittest
from typing import List


class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r

        dp = {}
        res = -1
        for num in nums:
            sum_digit = sum_digits(num)
            if sum_digit in dp:
                res = max(res, num + dp[sum_digit])
                dp[sum_digit] = num if num > dp[sum_digit] else dp[sum_digit]
            else:
                dp[sum_digit] = num
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            54,
            self.sol.maximumSum(nums=[18, 43, 36, 13, 7]),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.maximumSum(nums=[10, 12, 19, 14]),
        )

    def testcase3(self):
        self.assertEqual(
            835,
            self.sol.maximumSum(
                nums=[
                    368,
                    369,
                    307,
                    304,
                    384,
                    138,
                    90,
                    279,
                    35,
                    396,
                    114,
                    328,
                    251,
                    364,
                    300,
                    191,
                    438,
                    467,
                    183,
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
