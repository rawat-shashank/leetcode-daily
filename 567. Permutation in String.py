import unittest
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """sliding window"""
        freq1 = Counter(s1)
        n = len(s1)
        start, end = 0, n - 1
        while end < len(s2):
            freq2 = Counter(s2[start : end + 1])
            if freq2 == freq1:
                return True
            else:
                start += 1
                end += 1
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.checkInclusion(s1="ab", s2="eidbaooo"),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.checkInclusion(s1="ab", s2="eidboaoo"),
        )

    def testcase3(self):
        self.assertTrue(
            self.sol.checkInclusion(s1="adc", s2="dcda"),
        )


if __name__ == "__main__":
    unittest.main()
