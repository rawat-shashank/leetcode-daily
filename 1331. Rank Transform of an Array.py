# 1235. Maximum Profit in Job Scheduling
import unittest
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tempArray = sorted(arr)
        hm = {}
        rank = 0
        for x in tempArray:
            if x in hm:
                pass
            else:
                rank += 1
                hm[x] = rank
        for idx, x in enumerate(arr):
            tempArray[idx] = hm[x]

        return tempArray
    


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [4, 1, 2, 3], self.sol.arrayRankTransform(arr=[40, 10, 20, 30])
        )

    def testcase2(self):
        self.assertEqual([1, 1, 1], self.sol.arrayRankTransform(arr=[100, 100, 100]))

    def testcase3(self):
        self.assertEqual(
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
            self.sol.arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]),
        )


if __name__ == "__main__":
    unittest.main()
