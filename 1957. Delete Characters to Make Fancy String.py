import unittest


class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        res.append(s[0])
        count = 1
        for i in range(1, len(s)):
            if s[i] == res[-1]:
                if count > 1:
                    continue
                else:
                    res.append(s[i])
                    count += 1
            else:
                res.append(s[i])
                count = 1

        return "".join(res)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "leetcode",
            self.sol.makeFancyString(s="leeetcode"),
        )

    def testcase2(self):
        self.assertEqual(
            "aabaa",
            self.sol.makeFancyString(s="aaabaaaa"),
        )

    def testcase3(self):
        self.assertEqual(
            "aab",
            self.sol.makeFancyString(s="aab"),
        )


if __name__ == "__main__":
    unittest.main()
