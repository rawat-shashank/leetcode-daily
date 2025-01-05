import unittest
from typing import List


class Solution:
    # def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    #     """brute force 97, 122"""
    #     ans = [ord(ch) for ch in s]
    #     for [start, end, dir] in shifts:
    #         for i in range(start, end + 1):
    #             tmp = ans[i] + (1 if dir else -1)
    #             ans[i] = (tmp - 97) % 26 + 97
    #     return "".join([chr(i) for i in ans])

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # use a array for prefix cumaltive shifts
        diff_shifts = [0] * (len(s) + 1)

        # calculate cumlative shift starting and ending pos with dir
        for [start, end, d] in shifts:
            diff_shifts[end + 1] += 1 if d else -1
            diff_shifts[start] -= 1 if d else -1

        diff = 0
        # conver to list since str are immutable
        res = [ord(c) - ord("a") for c in s]
        for i in range(len(s), -1, -1):
            diff += diff_shifts[i]
            res[i - 1] += diff
        return "".join([chr((tmp % 26) + 97) for tmp in res])


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "ace",
            self.sol.shiftingLetters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]]),
        )

    def testcase2(self):
        self.assertEqual(
            "catz",
            self.sol.shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]]),
        )


if __name__ == "__main__":
    unittest.main()
