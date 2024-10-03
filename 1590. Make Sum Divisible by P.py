import unittest
from typing import List


class Solution:
    def minSunarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        remain_to_idx = {0: -1}

        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_idx:
                length = i - remain_to_idx[prefix]
                res = min(res, length)
            remain_to_idx[cur_sum] = i
        return -1 if res == len(nums) else res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.minSunarray(nums=[3, 1, 4, 2], p=6),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.minSunarray(nums=[6, 3, 5, 2], p=9),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.minSunarray(nums=[1, 2, 3], p=3),
        )

    def testcase4(self):
        self.assertEqual(
            1,
            self.sol.minSunarray(nums=[1, 1, 1], p=2),
        )


if __name__ == "__main__":
    unittest.main()
