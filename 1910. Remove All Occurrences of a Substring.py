import unittest


class Solution:

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     """stack - like"""
    #     stack = []
    #     part = list(part)
    #     n = len(part)
    #     for i in range(len(s)):
    #         stack.append(s[i])
    #         while stack and len(stack) >= n and stack[-n:] == part:
    #             for _ in range(n):
    #                 stack.pop()
    #     return "".join(stack)

    def removeOccurrences(self, s: str, part: str) -> str:
        """using inbuilt library"""
        while part in s:
            # replace one occurance per loop, to check for newly form strin
            s = s.replace(part, "", 1)
        return s


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "dab",
            self.sol.removeOccurrences(s="daabcbaabcbc", part="abc"),
        )

    def testcase2(self):
        self.assertEqual(
            "ab",
            self.sol.removeOccurrences(s="axxxxyyyyb", part="xy"),
        )


if __name__ == "__main__":
    unittest.main()
