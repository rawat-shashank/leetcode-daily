import unittest


class Solution:

    def smallestNumber(self, pattern: str) -> str:
        """simple stacks"""
        res, stack = [], []
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(stack.pop())
        return "".join(res)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "123549876",
            self.sol.smallestNumber(pattern="IIIDIDDD"),
        )

    def testcase2(self):
        self.assertEqual(
            "4321",
            self.sol.smallestNumber(pattern="DDD"),
        )


if __name__ == "__main__":
    unittest.main()
