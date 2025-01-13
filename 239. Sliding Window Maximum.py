import unittest
from typing import List
from collections import deque


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     """brute force - TLE"""
    #     ans = []
    #     for i in range(0, len(nums) - k + 1):
    #         ans.append(max(nums[i : i + k]))
    #     return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """monotonic decreasing queue"""
        q = deque()
        ans = []
        left, right = 0, 0
        while right < len(nums):
            # check if q and have number greater than current
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # check and shrink if window is getting bigger
            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                # add greatest number in q to ans
                ans.append(nums[q[0]])
                left += 1
            right += 1
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [3, 3, 5, 5, 6, 7],
            self.sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3),
        )

    def testcase2(self):
        self.assertEqual(
            [1],
            self.sol.maxSlidingWindow(nums=[1], k=1),
        )


if __name__ == "__main__":
    unittest.main()
