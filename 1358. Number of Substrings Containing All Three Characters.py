import unittest
from collections import defaultdict


class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        res = 0
        counts = defaultdict(int)
        for right in range(len(s)):
            counts[s[right]] += 1

            while len(counts) == 3:
                res += len(s) - right
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    counts.pop(s[left])
                left += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            10,
            self.sol.numberOfSubstrings(s = "abcabc"),
        )

    def testcase2(self):
        self.assertEqual(
            3,
            self.sol.numberOfSubstrings(s = "aaacb"),
        )

    def testcase3(self):
        self.assertEqual(
            1,
            self.sol.numberOfSubstrings(s = "abc"),
        )

if __name__ == "__main__":
    unittest.main()
