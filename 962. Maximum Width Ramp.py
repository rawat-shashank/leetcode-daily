from typing import List
import unittest


class Solution:
    def maxWidthTamp(self, nums: List[int]) -> int:
        nums_len = len(nums)
        right_max = [0] * nums_len
        right_max[nums_len - 1] = nums[nums_len - 1]
        for idx in range(nums_len - 2, -1, -1):
            right_max[idx] = max(nums[idx], right_max[idx + 1])

        left, max_width = 0, 0
        # while right < nums_len:
        #     while left < right and nums[left] > right_max[right]:
        #         left += 1
        #     max_width = max(max_width, right - left)
        #     right += 1
        for right in range(nums_len):
            while nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)

        return max_width


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(4, self.sol.maxWidthTamp(nums=[6, 0, 8, 2, 1, 5]))

    def testcase2(self):
        self.assertEqual(
            7,
            self.sol.maxWidthTamp(nums=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]),
        )


if __name__ == "__main__":
    unittest.main()
