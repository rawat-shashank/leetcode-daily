import unittest
from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, close):
            print(stack)
            # check if stack is twice of n
            if len(stack) == 2 * n:
                # add valid brackets to res array
                res.append("".join(stack))
                return
            # if opening brackets are less than n, we backtrack by adding open
            # bracket to stack
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            # since we are adding closing brack only when we
            # have opening brackets we will only be creating
            # valid brackets
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            ["()"],
            self.sol.generateParenthesis(n=1),
        )

    def testcase2(self):
        self.assertEqual(
            ["(())", "()()"],
            self.sol.generateParenthesis(n=2),
        )

    def testcase3(self):
        self.assertEqual(
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
            self.sol.generateParenthesis(n=3),
        )


if __name__ == "__main__":
    unittest.main()
