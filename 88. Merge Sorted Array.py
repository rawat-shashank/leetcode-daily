import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m and n:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

        return nums1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 2, 2, 3, 5, 6],
            self.sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3),
        )

    def testcase2(self):
        self.assertEqual(
            [1],
            self.sol.merge(nums1=[1], m=1, nums2=[], n=0),
        )

    def testcase3(self):
        self.assertEqual(
            [1],
            self.sol.merge(nums1=[0], m=0, nums2=[1], n=1),
        )


if __name__ == "__main__":
    unittest.main()
