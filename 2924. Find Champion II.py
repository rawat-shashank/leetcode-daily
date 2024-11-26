from typing import List
import unittest


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """in-degree count"""
        arr = [0] * n
        for edge in edges:
            arr[edge[1]] += 1
        champ = -1
        no_of_champ = 0
        for i in range(n):
            if arr[i] == 0:
                champ = i
                no_of_champ += 1
        if no_of_champ > 1:
            return -1
        return champ


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            0,
            self.sol.findChampion(n=3, edges=[[0, 1], [1, 2]]),
        )

    def testcase2(self):
        self.assertEqual(
            -1,
            self.sol.findChampion(n=4, edges=[[0, 2], [1, 3], [1, 2]]),
        )


if __name__ == "__main__":
    unittest.main()
