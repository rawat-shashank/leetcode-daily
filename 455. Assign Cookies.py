# 455. Assign Cookies
import unittest
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0 or len(g) == 0:
            return 0
        g.sort()
        s.sort()
        l, r = 0, 0
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l += 1
                r += 1
            else:
                r += 1
        return l


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1, self.sol.findContentChildren(g=[1, 2, 3], s=[1, 1]))

    def testcase2(self):
        self.assertEqual(
            2, self.sol.findContentChildren(g=[1, 2], s=[1, 2, 3]))

    def testcase3(self):
        self.assertEqual(1, self.sol.findContentChildren(g=[1, 2, 3], s=[3]))


if __name__ == "__main__":
    unittest.main()
