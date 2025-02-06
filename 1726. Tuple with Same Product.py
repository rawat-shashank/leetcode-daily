import unittest
from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pairs = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                pairs[product] += 1

        res = 0
        for cnt in pairs.values():
            total_pairs = cnt * (cnt - 1) // 2
            res += 8 * total_pairs
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.tupleSameProduct(nums=[2, 3, 4, 6]),
        )

    def testcase2(self):
        self.assertEqual(
            16,
            self.sol.tupleSameProduct(nums=[1, 2, 4, 5, 10]),
        )


if __name__ == "__main__":
    unittest.main()
