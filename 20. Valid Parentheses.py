import unittest


class Solution:

    # def isValid(self, s: str) -> bool:
    #     """simple stack - accepted"""
    #     res = []
    #     opening = ["(", "[", "{"]
    #     for x in s:
    #         if x in opening:
    #             res.append(x)
    #         elif res:
    #             y = res.pop()
    #             if (
    #                 (x == ")" and y != "(")
    #                 or (x == "]" and y != "[")
    #                 or (x == "}" and y != "{")
    #             ):
    #                 return False
    #         else:
    #             return False
    #     return False if len(res) else True

    def isValid(self, s: str) -> bool:
        """stack with hashmap - faster"""
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for x in s:
            if x in mapping:
                if stack and stack[-1] == mapping[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return not stack


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.isValid(s="()"),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.isValid(s="()[]{}"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.isValid(s="(]"),
        )

    def testcase4(self):
        self.assertTrue(
            self.sol.isValid(s="([])"),
        )

    def testcase5(self):
        self.assertFalse(
            self.sol.isValid(s="["),
        )

    def testcase6(self):
        self.assertFalse(
            self.sol.isValid(s="]"),
        )


if __name__ == "__main__":
    unittest.main()
