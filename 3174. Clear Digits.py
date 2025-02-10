import unittest
from typing import List


class Solution:

    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit() and stack:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "abc",
            self.sol.clearDigits(s="abc"),
        )

    def testcase2(self):
        self.assertEqual(
            "",
            self.sol.clearDigits(s="cb34"),
        )


if __name__ == "__main__":
    unittest.main()
