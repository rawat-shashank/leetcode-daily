from heapq import heappop, heappush
import unittest


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        odd_counts = 0
        for count in freq:
            if count % 2 == 1:
                odd_counts += 1
        return odd_counts <= k


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canConstruct(s="annabelle", k=2),
        )

    def testcase2(self):
        self.assertFalse(self.sol.canConstruct(s="leetcode", k=3))

    def testcase3(self):
        self.assertTrue(self.sol.canConstruct(s="true", k=4))


if __name__ == "__main__":
    unittest.main()
