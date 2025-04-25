import unittest
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        cnt = Counter([0])
        res = 0
        prefix = 0
        for num in nums:
            prefix += 1 if num % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
            print(prefix, res, cnt)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.countInterestingSubarrays(nums=[3, 2, 4], modulo=2, k=1),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.countInterestingSubarrays(nums=[3, 1, 9, 6], modulo=3, k=0),
        )


if __name__ == "__main__":
    unittest.main()
