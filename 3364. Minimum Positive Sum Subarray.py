from typing import List
import unittest


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        pass


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.minimumSumSubarray(nums=[3, -2, 1, 4], l=2, r=3),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minimumSumSubarray(nums=[-2, 2, -3, 1], l=2, r=3),
        )

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.minimumSumSubarray(nums=[1, 2, 3, 4], l=2, r=4),
        )


if __name__ == "__main__":
    unittest.main()
