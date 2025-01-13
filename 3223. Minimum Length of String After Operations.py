import unittest
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        freq_counter = Counter(s)
        count = 0
        for freq in freq_counter.values():
            if freq % 2 == 1:
                count += freq - 1
            else:
                count += freq - 2
        return len(s) - count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(5, self.sol.minimumLength(s="abaacbcbb"))

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.minimumLength(s="aa"),
        )


if __name__ == "__main__":
    unittest.main()
