import unittest
from typing import List


class Solution:

    # def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    #     """brute force - TLE"""
    #     ans = 0
    #     res = []
    #     for x in nums1:
    #         for y in nums2:
    #             res.append(x ^ y)
    #     for x in res:
    #         ans ^= x
    #     return ans

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """even xor of a number is zero"""
        ans = 0
        if len(nums2) % 2 == 1:
            for x in nums1:
                ans ^= x

        if len(nums1) % 2 == 1:
            for x in nums2:
                ans ^= x
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            13,
            self.sol.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0]),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.xorAllNums(nums1=[1, 2], nums2=[3, 4]),
        )


if __name__ == "__main__":
    unittest.main()
