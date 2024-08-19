import unittest
from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        i2,i3,i5 = 0, 0,0
        for i in range(1, n):
            next_num = min(
                ans[i2]*2, ans[i3]*3,ans[i5]*5
            )
            ans.append(next_num)
            if next_num == ans[i2] * 2:
                i2 += 1
            if next_num == ans[i3] * 3:
                i3 += 1
            if next_num == ans[i5] * 5:
                i5 += 1
        return ans[n-1]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def testcase1(self):
        self.assertEqual(12, self.sol.nthUglyNumber(n = 10))

    def testcase2(self):
        self.assertEqual(1, self.sol.nthUglyNumber(n = 1))


if __name__ == "__main__":
    unittest.main()
