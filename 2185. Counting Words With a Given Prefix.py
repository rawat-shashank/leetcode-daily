import unittest
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.prefixCount(
                words=["pay", "attention", "practice", "attend"], pref="at"
            ),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.prefixCount(
                words=["leetcode", "win", "loops", "success"], pref="code"
            ),
        )


if __name__ == "__main__":
    unittest.main()
