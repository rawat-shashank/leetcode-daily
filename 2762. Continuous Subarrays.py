import unittest
from typing import List


class Solution:
    # def continuousSubarrays(self, nums: List[int]) -> int:
    #     """Brute force - TLE"""
    #     k = len(nums)
    #
    #     def validContinousSubarray(arr):
    #         if abs(max(arr) - min(arr)) <= 2:
    #             return True
    #         return False
    #
    #     count = 0
    #     res = []
    #     while k:
    #         left = 0
    #         right = k
    #         while right <= len(nums):
    #             if validContinousSubarray(nums[left:right]):
    #                 res.append(nums[left:right])
    #                 count += 1
    #             left += 1
    #             right += 1
    #         k -= 1
    #     print(res)
    #     return count

    def continuousSubarrays(self, nums: List[int]) -> int:
        left = right = win_len = count = 0
        cur_min = cur_max = nums[0]

        for right in range(len(nums)):
            cur_min = min(cur_min, nums[right])
            cur_max = max(cur_max, nums[right])

            if cur_max - cur_min > 2:
                win_len = right - left
                count += win_len * (win_len + 1) // 2

                # adjust left to new position
                left = right
                cur_min = cur_max = nums[right]

                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    cur_min = min(cur_min, nums[left])
                    cur_max = max(cur_max, nums[left])

                if left < right:
                    win_len = right - left
                    count -= win_len * (win_len + 1) // 2
        win_len = right - left + 1
        count += win_len * (win_len + 1) // 2

        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8,
            self.sol.continuousSubarrays(nums=[5, 4, 2, 4]),
        )

    def testcase2(self):
        self.assertEqual(
            6,
            self.sol.continuousSubarrays(nums=[1, 2, 3]),
        )

    def testcase3(self):
        self.assertEqual(
            28,
            self.sol.continuousSubarrays(nums=[42, 41, 42, 41, 41, 40, 39, 38]),
        )


if __name__ == "__main__":
    unittest.main()
