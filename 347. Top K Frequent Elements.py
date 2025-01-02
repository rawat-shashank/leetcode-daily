import unittest
from typing import List
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums:
            dp[num] = dp.get(num, 0) + 1
        res = []
        for key, value in dp.items():
            heappush(res, (-value, key))
        ans = []
        while k:
            k -= 1
            value, key = heappop(res)
            ans.append(key)
        print(ans)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertCountEqual(
            [1, 2], self.sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
        )

    def testcase2(self):
        self.assertCountEqual([1], self.sol.topKFrequent(nums=[1], k=1))

    def testcase3(self):
        self.assertCountEqual([1, 2], self.sol.topKFrequent(nums=[1, 2], k=2))


if __name__ == "__main__":
    unittest.main()
