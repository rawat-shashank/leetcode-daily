import unittest


class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for x in s:
            if x == "1":
                ones += 1
        res = 0
        zeros = 0
        for idx in range(len(s) - 1):
            if s[idx] == "0":
                zeros += 1
            if s[idx] == "1":
                ones -= 1
            res = max(res, zeros + ones)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.maxScore(s="011101"),
        )

    def testcase2(self):
        self.assertEqual(5, self.sol.maxScore(s="00111"))

    def testcase3(self):
        self.assertEqual(3, self.sol.maxScore(s="1111"))

    def testcase4(self):
        self.assertEqual(1, self.sol.maxScore(s="00"))


if __name__ == "__main__":
    unittest.main()
