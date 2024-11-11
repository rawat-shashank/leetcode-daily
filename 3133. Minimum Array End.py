from typing import List
import unittest


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        while n > 1:
            res = (res + 1) | x
            n -= 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            6,
            self.sol.minEnd(n=3, x=4),
        )

    def testcase2(self):
        self.assertEqual(
            15,
            self.sol.minEnd(n=2, x=7),
        )


if __name__ == "__main__":
    unittest.main()
