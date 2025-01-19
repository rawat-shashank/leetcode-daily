import unittest
from typing import List


class Solution:

    def findMin(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = end - 1
        return -1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def testcase2(self):
        self.assertEqual(-1, self.sol.findMin(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def testcase3(self):
        self.assertEqual(
            -1,
            self.sol.findMin(nums=[1], target=0),
        )

    def testcase4(self):
        self.assertEqual(
            0,
            self.sol.findMin(nums=[1], target=1),
        )

    def testcase5(self):
        self.assertEqual(
            1,
            self.sol.findMin(nums=[1, 3], target=3),
        )

    def testcase6(self):
        self.assertEqual(
            0,
            self.sol.findMin(nums=[5, 1, 3], target=5),
        )

    def testcase7(self):
        self.assertEqual(
            1,
            self.sol.findMin(nums=[3, 1], target=1),
        )


if __name__ == "__main__":
    unittest.main()
