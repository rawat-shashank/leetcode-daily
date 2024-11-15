from typing import List
import unittest
import math


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """two pointer approach"""
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.findLengthOfShortestSubarray(arr=[1, 2, 3, 10, 4, 2, 3, 5]),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.findLengthOfShortestSubarray(arr=[5, 4, 3, 2, 1]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.findLengthOfShortestSubarray(arr=[1, 2, 3]),
        )

    def testcase3(self):
        self.assertEqual(
            8,
            self.sol.findLengthOfShortestSubarray(
                arr=[6, 3, 10, 11, 15, 20, 13, 3, 18, 12]
            ),
        )


if __name__ == "__main__":
    unittest.main()
