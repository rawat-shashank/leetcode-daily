import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        lmax, rmax = height[0], height[-1]
        res = 0
        while left < right:
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                res += lmax - height[left]
            else:
                right -= 1
                rmax = max(rmax, height[right])
                res += rmax - height[right]
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(6, self.sol.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def testcase2(self):
        self.assertEqual(
            9,
            self.sol.trap(height=[4, 2, 0, 3, 2, 5]),
        )


if __name__ == "__main__":
    unittest.main()
