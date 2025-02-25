import unittest
from typing import List


class Solution:

    # def numOfSubarrays(self, arr: List[int]) -> int:
    #     """brute force - TLE"""
    #     count = 0
    #     subArrays = ([arr[i:j] for i in range(len(arr))
    #                   for j in range(i + 1, len(arr) + 1)])
    #     for nums in subArrays:
    #         sum = 0
    #         for x in nums:
    #             sum += x
    #         if sum % 2 == 1:
    #             count += 1
    #     return count

    # def numOfSubarrays(self, arr: List[int]) -> int:
    #     res = 0
    #     odd_cnt, evn_cnt = 0, 1
    #     curr_sum = 0
    #     MOD = 10**9 + 7
    #
    #     for n in arr:
    #         curr_sum += n
    #         # if curr_sum is odd
    #         if curr_sum % 2:
    #             res += evn_cnt
    #             odd_cnt += 1
    #         else:
    #             res += odd_cnt
    #             evn_cnt += 1
    #         res %= MOD
    #     return res

    def numOfSubarrays(self, arr: List[int]) -> int:
        """can be re-written as, faster as less calculation is required"""
        cumSum = odd = even = 0
        for num in arr:
            cumSum += num
            if cumSum % 2:
                odd += 1
            else:
                even += 1
        return odd * (even + 1) % (pow(10, 9) + 7)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.numOfSubarrays(arr=[1, 3, 5]))

    def testcase2(self):
        self.assertEqual(0, self.sol.numOfSubarrays(
            arr=[2, 4, 6]))

    def testcase3(self):
        self.assertEqual(
            16,
            self.sol.numOfSubarrays(arr=[1, 2, 3, 4, 5, 6, 7]),
        )


if __name__ == "__main__":
    unittest.main()
