import unittest
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum = 0
        count = 0
        for i in range(1, n + 1):
            if sum >= maxSum or sum + i > maxSum:
                break
            elif i not in banned:
                sum += i
                count += 1

        return count


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.maxCount(banned=[1, 6, 5], n=5, maxSum=6),
        )

    def testcase2(self):
        self.assertEqual(
            0,
            self.sol.maxCount(banned=[1, 2, 3, 4, 5, 6, 7], n=8, maxSum=1),
        )

    def testcase3(self):
        self.assertEqual(
            7,
            self.sol.maxCount(banned=[11], n=7, maxSum=50),
        )


if __name__ == "__main__":
    unittest.main()
