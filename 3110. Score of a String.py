import unittest


class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = ord(s[0])
        for i in range(1, len(s)):
            next = ord(s[i])
            res += abs(next - prev)
            prev = next
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            13,
            self.sol.scoreOfString(s="hello"),
        )

    def testcase2(self):
        self.assertEqual(
            50,
            self.sol.scoreOfString(s="zaz"),
        )


if __name__ == "__main__":
    unittest.main()
