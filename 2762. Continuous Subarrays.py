import unittest
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """Brute force - TLE"""
        k = len(nums)

        def validContinousSubarray(arr):
            if abs(max(arr) - min(arr)) <= 2:
                return True
            return False

        count = 0
        res = []
        while k:
            left = 0
            right = k
            while right <= len(nums):
                if validContinousSubarray(nums[left: right]):
                    res.append(nums[left:right])
                    count += 1
                left += 1
                right += 1
            k -= 1
        print(res)
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.continuousSubarrays(nums = [5,4,2,4]),
        )

    def testcase2(self):
        self.assertEqual(
            6,
            self.sol.continuousSubarrays(nums = [1,2,3]),
        )


if __name__ == "__main__":
    unittest.main()
