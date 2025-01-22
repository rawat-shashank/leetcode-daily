import unittest
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1, nums2
        total = len(n1) + len(n2)
        half = total // 2

        # swap the smaller number list to be n1
        if len(n2) < len(n1):
            n1, n2 = n2, n1

        # start with 0 to len(n1) -1 from n1
        left, right = 0, len(n1) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            n1_left = n1[i] if i >= 0 else float("-inf")
            n1_right = n1[i + 1] if i + 1 < len(n1) else float("inf")

            n2_left = n2[j] if j >= 0 else float("-inf")
            n2_right = n2[j + 1] if j + 1 < len(n2) else float("inf")

            if n1_left <= n2_right and n2_left <= n1_right:
                if total % 2:
                    # if total number are odd
                    return min(n1_right, n2_right)
                else:
                    # even numbers in total
                    return (max(n1_left, n2_left) + min(n1_right, n2_right)) / 2
            elif n1_right > n2_right:
                right = i - 1
            else:
                left = i + 1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2.00000,
            self.sol.findMedianSortedArrays(nums1=[1, 3], nums2=[2]),
        )

    def testcase2(self):
        self.assertEqual(
            2.50000,
            self.sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
