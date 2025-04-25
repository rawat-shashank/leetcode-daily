import unittest


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        res = 0
        DISTNCT = len(set(nums))
        N = len(nums)
        right = 0
        dp = {}
        for left in range(N):
            if left > 0:
                # remove the left element from Hashmap
                n = nums[left - 1]
                dp[n] -= 1
                if dp[n] == 0:
                    dp.pop(n)
            while right < N and len(dp) < DISTNCT:
                n = nums[right]
                dp[n] = dp.get(n, 0) + 1
                right += 1
            if len(dp) == DISTNCT:
                res += N - right + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.countCompleteSubarrays(nums=[1, 3, 1, 2, 2]),
        )

    def testcase2(self):
        self.assertEqual(
            10,
            self.sol.countCompleteSubarrays(nums=[5, 5, 5, 5]),
        )


if __name__ == "__main__":
    unittest.main()
