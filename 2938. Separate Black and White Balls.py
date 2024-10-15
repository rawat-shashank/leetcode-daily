import unittest
from typing import List


class Solution:
    def minimumSteps(self, s: str) -> int:
        left, res = 0, 0
        for right in range(len(s)):
            if s[right] == "0":
                res += right - left
                left += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.minimumSteps(s="101"),
        )

    def testcase2(self):
        self.assertEqual(2, self.sol.minimumSteps(s="100"))

    def testcase3(self):
        self.assertEqual(0, self.sol.minimumSteps(s="0111"))

    def testcase4(self):
        self.assertEqual(0, self.sol.minimumSteps(s="0001"))


if __name__ == "__main__":
    unittest.main()
