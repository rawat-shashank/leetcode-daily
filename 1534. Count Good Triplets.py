import unittest
from typing import List


class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """brute force - enemuration"""
        res = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            4, self.sol.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3)
        )

    def testcase2(self):
        self.assertEqual(
            0, self.sol.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1)
        )


if __name__ == "__main__":
    unittest.main()
