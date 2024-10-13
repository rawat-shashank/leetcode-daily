import unittest
from typing import List
from heapq import heappush, heappop


class Solution:
    def smallerRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):
            left = min(left, nums[i][0])
            right = max(right, nums[i][0])
            heappush(min_heap, (nums[i][0], i, 0))

        res = [left, right]
        while True:
            _, i, idx = heappop(min_heap)
            idx += 1
            if idx == len(nums[i]):
                break

            next_val = nums[i][idx]
            heappush(min_heap, (next_val, i, idx))
            right = max(right, next_val)
            left = min_heap[0][0]
            if right - left < res[1] - res[0]:
                res = [left, right]

        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [20, 24],
            self.sol.smallerRange(
                nums=[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 1], self.sol.smallerRange(nums=[[1, 2, 3], [1, 2, 3], [1, 2, 3]])
        )


if __name__ == "__main__":
    unittest.main()
