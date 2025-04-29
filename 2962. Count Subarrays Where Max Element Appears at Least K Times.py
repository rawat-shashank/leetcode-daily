import unittest


class Solution:
    # def countSubarrays(self, nums: list[int], k: int) -> int:
    #     """brute force - TLE"""
    #     N = len(nums)
    #     mx = max(nums)
    #     res = 0
    #     for left in range(N):
    #         cnt = 0
    #         for right in range(left, N):
    #             if nums[right] == mx:
    #                 cnt += 1
    #             if cnt >= k:
    #                 res += 1
    #     return res

    def countSubarrays(self, nums: list[int], k: int) -> int:
        """sliding window"""
        N = len(nums)
        mx = max(nums)
        res = 0
        left = 0
        cnt = 0
        for right in range(N):
            if nums[right] == mx:
                cnt += 1
            while cnt >= k:
                res += N - right
                if nums[left] == mx:
                    cnt -= 1
                left += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            6,
            self.sol.countSubarrays(nums=[1, 3, 2, 3, 3], k=2),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.countSubarrays(nums=[1, 4, 2, 1], k=3),
        )


if __name__ == "__main__":
    unittest.main()
