import unittest
from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            self.sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 1, 1, 0],
            self.sol.dailyTemperatures(temperatures=[30, 40, 50, 60]),
        )

    def testcase3(self):
        self.assertEqual(
            [1, 1, 0],
            self.sol.dailyTemperatures(temperatures=[30, 60, 90]),
        )


if __name__ == "__main__":
    unittest.main()
