import unittest
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """brute force"""
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"]),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.countPrefixSuffixPairs(words=["pa", "papa", "ma", "mama"]),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.countPrefixSuffixPairs(words=["abab", "ab"]),
        )


if __name__ == "__main__":
    unittest.main()
