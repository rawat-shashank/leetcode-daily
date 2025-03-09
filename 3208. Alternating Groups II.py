import unittest
from typing import List


class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        l = 0
        res = 0
        for r in range(1, N + k -1):
            if colors[r%N] == colors[ (r-1) % N]:
                l = r
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                res += 1
        return res

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            3,
            self.sol.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4),
        )

if __name__ == "__main__":
    unittest.main()
