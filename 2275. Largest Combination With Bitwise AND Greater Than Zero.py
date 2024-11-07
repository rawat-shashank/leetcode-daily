from typing import List
import unittest


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 24
        for n in candidates:
            i = 0
            while n > 0:
                count[i] += 1 & n
                i += 1
                n = n >> 1
        return max(count)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4,
            self.sol.largestCombination(candidates=[16, 17, 71, 62, 12, 24, 14]),
        )

    def testcase2(self):
        self.assertEqual(
            2,
            self.sol.largestCombination(candidates=[8, 8]),
        )


if __name__ == "__main__":
    unittest.main()
