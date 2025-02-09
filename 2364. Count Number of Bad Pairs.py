import unittest
from typing import List


class Solution:
    # def countBadPairs(self, nums: List[int]) -> int:
    #     """brute force - TLE"""
    #     count = 0
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if j - i != nums[j] - nums[i]:
    #                 count += 1
    #     return count

    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_count = {}
        for pos in range(len(nums)):
            diff = pos - nums[pos]
            good_pairs = diff_count.get(diff, 0)
            bad_pairs += pos - good_pairs
            diff_count[diff] = good_pairs + 1
        return bad_pairs


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.countBadPairs(nums=[4, 1, 3, 3]),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.countBadPairs(nums=[1, 2, 3, 4, 5]),
        )


if __name__ == "__main__":
    unittest.main()
