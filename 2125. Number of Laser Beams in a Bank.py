# 2125. Number of Laser Beams in a Bank
import unittest
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, lasers = 0, 0
        for num in bank:
            temp = num.count("1")
            if temp != 0:
                lasers = lasers + prev * temp
                prev = temp
        return lasers


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            8, self.sol.numberOfBeams(
                bank=["011001", "000000", "010100", "001000"])
        )

    def testcase2(self):
        self.assertEqual(0, self.sol.numberOfBeams(bank=["000", "111", "000"]))


if __name__ == "__main__":
    unittest.main()
