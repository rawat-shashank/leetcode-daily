import unittest


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        i = 0

        def helper():
            nonlocal i
            c = expression[i]
            i += 1
            if c == "t":
                return True
            if c == "f":
                return False
            if c == "!":
                i += 1
                res = not helper()
                i += 1
                return res

            children = []
            i += 1
            while expression[i] != ")":
                if expression[i] == ",":
                    i += 1
                else:
                    children.append(helper())
            i += 1
            if c == "&":
                return all(children)
            if c == "|":
                return any(children)

        return helper()


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            False,
            self.sol.parseBoolExpr(expression="&(|(f))"),
        )

    def testcase2(self):
        self.assertEqual(True, self.sol.parseBoolExpr(expression="|(f,f,f,t)"))

    def testcase3(self):
        self.assertEqual(True, self.sol.parseBoolExpr(expression="!(&(f,t))"))


if __name__ == "__main__":
    unittest.main()
