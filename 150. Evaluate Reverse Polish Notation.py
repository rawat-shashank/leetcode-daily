import unittest
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        """simple stack operation"""
        stack = []
        for x in tokens:
            if x in ["+", "*", "-", "/"]:
                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    stack.append(a + b)
                elif x == "-":
                    stack.append(a - b)
                elif x == "*":
                    stack.append(a * b)
                elif x == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(x))

        return stack.pop()


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(9, self.sol.evalRPN(tokens=["2", "1", "+", "3", "*"]))

    def testcase2(self):
        self.assertEqual(6, self.sol.evalRPN(tokens=["4", "13", "5", "/", "+"]))

    def testcase3(self):
        self.assertEqual(
            22,
            self.sol.evalRPN(
                tokens=[
                    "10",
                    "6",
                    "9",
                    "3",
                    "+",
                    "-11",
                    "*",
                    "/",
                    "*",
                    "17",
                    "+",
                    "5",
                    "+",
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
