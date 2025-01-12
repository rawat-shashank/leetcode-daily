from typing import List
import unittest


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        if open_brackets:
            return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canBeValid(s="))()))", locked="010100"),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.canBeValid(s="()()", locked="0000"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.canBeValid(s=")", locked="0"),
        )


if __name__ == "__main__":
    unittest.main()
