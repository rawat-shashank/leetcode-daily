import unittest
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid
        return -1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.search(nums=[-1, 0, 3, 5, 9, 12], target=2),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.search(nums=[5], target=5),
        )


if __name__ == "__main__":
    unittest.main()
