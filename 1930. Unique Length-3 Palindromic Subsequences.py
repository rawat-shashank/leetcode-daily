import unittest
from collections import Counter


class Solution:
    # def countPalindromicSubsequence(self, s: str) -> int:
    #     left = set()
    #     res = set()
    #     hashmap = Counter(s)
    #     for ch in s:
    #         hashmap[ch] -= 1
    #         for x in left:
    #             if hashmap[x] > 0:
    #                 res.add((ch, x))
    #         left.add(ch)
    #
    #     return len(res)

    def countPalindromicSubsequence(self, s: str) -> int:
        # create two starting and ending pos list of each ch
        start, last = [-1] * 26, [-1] * 26
        # find there first and last position of each ch
        for idx, ch in enumerate(s):
            curr = ord(ch) - ord("a")
            if start[curr] == -1:
                start[curr] = idx
            last[curr] = idx

        res = 0
        for i in range(26):
            if start[i] == -1:
                continue
            # create an empty set for unique ch between
            # starting and ending position
            between = set()
            for j in range(start[i] + 1, last[i]):
                between.add(s[j])
            # each unique ch is palindrome
            res += len(between)
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(3, self.sol.countPalindromicSubsequence(s="aabca"))

    def testcase2(self):
        self.assertEqual(0, self.sol.countPalindromicSubsequence(s="adc"))

    def testcase3(self):
        self.assertEqual(4, self.sol.countPalindromicSubsequence(s="bbcbaba"))


if __name__ == "__main__":
    unittest.main()
