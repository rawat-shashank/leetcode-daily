import unittest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for x in s:
            if x == ")" and len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(x)
        return len(stack)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(1, self.sol.minAddToMakeValid(s="())"))

    def testcase2(self):
        self.assertEqual(3, self.sol.minAddToMakeValid(s="((("))

    def testcase3(self):
        self.assertEqual(4, self.sol.minAddToMakeValid(s="()))(("))


if __name__ == "__main__":
    unittest.main()
