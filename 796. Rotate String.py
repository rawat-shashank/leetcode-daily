import unittest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ptr = 0
        while ptr < len(s):
            if s[ptr] == goal[0] and goal == s[ptr:] + s[0:ptr]:
                return True
            else:
                ptr += 1
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.rotateString(s="abcde", goal="cdeab"),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.rotateString(s="abcde", goal="abced"),
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.rotateString(s="defdefdefabcabc", goal="defdefabcabcdef"),
        )


if __name__ == "__main__":
    unittest.main()
