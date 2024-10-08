import unittest
from typing import List


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for x in s:
            stack.append(x)
            if len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B")
                or (stack[-2] == "C" and stack[-1] == "D")
            ):
                stack.pop()
                stack.pop()
        return len(stack)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minLength(s="ABFCACDB"),
        )

    def testcase2(self):
        self.assertEqual(
            5,
            self.sol.minLength(s="ACBBD"),
        )


if __name__ == "__main__":
    unittest.main()
