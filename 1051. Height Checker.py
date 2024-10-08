import unittest
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = sorted(heights)
        count = 0
        for i in range(len(res)):
            if heights[i] != res[i]:
                count += 1
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.heightChecker(heights=[1, 1, 4, 2, 1, 3]),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.heightChecker(heights=[5, 1, 2, 3, 4]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.heightChecker(heights=[1, 2, 3, 4, 5]),
        )


if __name__ == "__main__":
    unittest.main()
