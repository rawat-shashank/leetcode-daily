from typing import List
import unittest


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """sliding window, with hashmap for unique items"""
        window_sum = 0
        ans = 0
        begin = end = 0
        num_index = {}
        while end < len(nums):
            curr_num = nums[end]
            last_occurance = num_index.get(curr_num, -1)
            while begin <= last_occurance or end - begin + 1 > k:
                window_sum -= nums[begin]
                begin += 1
            num_index[curr_num] = end
            window_sum += nums[end]

            if end - begin + 1 == k:
                ans = max(ans, window_sum)
            end += 1

        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            15,
            self.sol.maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.maximumSubarraySum(nums=[4, 4, 4], k=3),
        )


if __name__ == "__main__":
    unittest.main()
