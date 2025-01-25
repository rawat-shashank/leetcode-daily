import unittest
from typing import List
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # making nums in group who's different are equal or less than limit
        # to make them continous
        groups = []
        # hashmap to check which group number belongs to
        num_in_group = {}

        # sort nums to get continous num within limit
        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_in_group[n] = len(groups) - 1

        res = []
        # get the num in which group, and get the smallest number
        # from that group append it to res
        for n in nums:
            j = num_in_group[n]
            res.append(groups[j].popleft())
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 3, 5, 8, 9],
            self.sol.lexicographicallySmallestArray(nums=[1, 5, 3, 9, 8], limit=2),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 6, 7, 18, 1, 2],
            self.sol.lexicographicallySmallestArray(nums=[1, 7, 6, 18, 2, 1], limit=3),
        )

    def testcase3(self):
        self.assertEqual(
            [1, 7, 28, 19, 10],
            self.sol.lexicographicallySmallestArray(nums=[1, 7, 28, 19, 10], limit=3),
        )


if __name__ == "__main__":
    unittest.main()
