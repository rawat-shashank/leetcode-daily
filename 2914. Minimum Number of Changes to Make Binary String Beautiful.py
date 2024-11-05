import unittest


class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0, len(s), 2):
            print("here", i)
            if s[i] != s[i + 1]:
                res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.minChanges(s="1001"),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.minChanges(s="10"),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.minChanges(s="0000"),
        )


if __name__ == "__main__":
    unittest.main()
