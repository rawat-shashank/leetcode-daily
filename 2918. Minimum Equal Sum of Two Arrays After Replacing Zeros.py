import unittest


class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        sum1 = sum2 = 0
        zero1 = zero2 = 0
        for n in nums1:
            sum1 += n
            if n == 0:
                zero1 += 1
                sum1 += 1

        for n in nums2:
            sum2 += n
            if n == 0:
                zero2 += 1
                sum2 += 1

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            12,
            self.sol.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4]),
        )


if __name__ == "__main__":
    unittest.main()
