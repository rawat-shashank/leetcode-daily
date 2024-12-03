from typing import List
import unittest


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """two pointer, one for string, another for space"""
        ans = []
        space_idx = 0
        for idx, chr in enumerate(s):
            if space_idx < len(spaces) and idx == spaces[space_idx]:
                ans.append(" ")
                space_idx += 1
            ans.append(chr)
        return "".join(ans)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            "Leetcode Helps Me Learn",
            self.sol.addSpaces(s="LeetcodeHelpsMeLearn", spaces=[8, 13, 15]),
        )

    def testcase2(self):
        self.assertEqual(
            "i code in py thon",
            self.sol.addSpaces(s="icodeinpython", spaces=[1, 5, 7, 9]),
        )

    def testcase3(self):
        self.assertEqual(
            " s p a c i n g",
            self.sol.addSpaces(s="spacing", spaces=[0, 1, 2, 3, 4, 5, 6]),
        )


if __name__ == "__main__":
    unittest.main()
