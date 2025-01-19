import unittest
from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(1, self.sol.findMin(nums=[3, 4, 5, 1, 2]))

    def testcase2(self):
        self.assertEqual(0, self.sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))

    def testcase3(self):
        self.assertEqual(
            11,
            self.sol.findMin(nums=[11, 13, 15, 17]),
        )


if __name__ == "__main__":
    unittest.main()
