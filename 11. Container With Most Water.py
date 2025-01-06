import unittest
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            49,
            self.sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.maxArea(height=[1, 1]),
        )


if __name__ == "__main__":
    unittest.main()
