import unittest
from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        """strictly increasing monotonic stack"""

        # adding extra zero height at the end to stop ever increasing heights
        heights.append(0)
        # adding -1 in stack for extra zero height pos
        stack = [-1]
        ans = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # width calculation from current ele to the pop up ele
                # to make sure all permutation of heights are calculated
                # while pop elements from stack
                w = i - stack[-1] - 1
                ans = max(ans, w * h)
            stack.append(i)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            10,
            self.sol.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.largestRectangleArea(heights=[2, 4]),
        )

    def testcase3(self):
        self.assertEqual(
            6,
            self.sol.largestRectangleArea(heights=[2, 1, 2, 1, 2, 1]),
        )

    def testcase4(self):
        self.assertEqual(
            2,
            self.sol.largestRectangleArea(heights=[2, 0, 2]),
        )

    def testcase5(self):
        self.assertEqual(
            3,
            self.sol.largestRectangleArea(heights=[2, 1, 2]),
        )

    def testcase6(self):
        self.assertEqual(
            4,
            self.sol.largestRectangleArea(heights=[1, 2, 2]),
        )

    def testcase7(self):
        self.assertEqual(
            9,
            self.sol.largestRectangleArea(heights=[1, 2, 3, 4, 5]),
        )


if __name__ == "__main__":
    unittest.main()
