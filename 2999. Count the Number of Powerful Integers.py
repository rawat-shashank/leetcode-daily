import unittest
from helpers.listToBinaryTree import identicalTrees, listToBinaryTree, TreeNode


class Solution:
    def numterOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = low.zfill(n)  # align digits
        pre_len = n - len(s)  # prefix length

        # TLE without cache
        # @cache
        def dfs(i, limit_low, limit_high):
            # recursive boundary
            if i == n:
                return 1
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            res = 0
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dfs(
                        i + 1,
                        limit_low and digit == lo,
                        limit_high and digit == hi,
                    )
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dfs(
                        i + 1, limit_low and x == lo, limit_high and x == hi
                    )

            return res

        return dfs(0, True, True)

class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            5,
            self.sol.numterOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.numterOfPowerfulInt(
                start = 15, finish = 215, limit = 6, s = "10"
            ),
        )
        
    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.numterOfPowerfulInt(
                start = 1000, finish = 2000, limit = 4, s = "3000"
            ),
        )
if __name__ == "__main__":
    _ = unittest.main()
