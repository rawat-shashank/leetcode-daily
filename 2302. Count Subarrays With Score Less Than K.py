import unittest


class Solution:

    def countSubarrays(self, nums: list[int], k: int) -> int:
        """sliding window"""
        N = len(nums)
        left = total = n = res = 0
        for right in range(N):
            total += nums[right]
            n += 1
            while left <= right and (total * n) >= k:
                total -= nums[left]
                left += 1
                n -= 1
            res += right - left + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            6,
            self.sol.countSubarrays(nums=[2, 1, 4, 3, 5], k=10),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.countSubarrays(nums=[1, 1, 1], k=5),
        )


if __name__ == "__main__":
    unittest.main()
