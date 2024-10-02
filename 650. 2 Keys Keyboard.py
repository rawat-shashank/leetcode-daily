import unittest
from typing import List

class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}

        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000
            if (count, paste) in dp:
                return dp[(count, paste)]
            
            #paste
            res1 = 1 + helper(count + paste, paste)
            #copy and paste
            res2 = 2 + helper(count + count, count)
            dp[(count, paste)] = min(res1, res2)
            return dp[((count, paste))]

        if n == 1: return 0
        return 1 + helper(1, 1)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def testcase1(self):
        self.assertEqual(3, self.sol.minSteps(n = 3))

    def testcase2(self):
        self.assertEqual(0, self.sol.minSteps(n = 1))


if __name__ == "__main__":
    unittest.main()
