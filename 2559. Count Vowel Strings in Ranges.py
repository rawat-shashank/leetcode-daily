import unittest
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        vowels = {"a", "e", "i", "o", "u"}
        sum = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                sum += 1
            prefix_sum.append(sum)
        res = []
        for query in queries:
            res.append(prefix_sum[query[1] + 1] - prefix_sum[query[0]])
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [2, 3, 0],
            self.sol.vowelStrings(
                words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [3, 2, 1],
            self.sol.vowelStrings(
                words=["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]]
            ),
        )

    def testcase3(self):
        self.assertEqual(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            self.sol.vowelStrings(
                words=[
                    "bzmxvzjxfddcuznspdcbwiojiqf",
                    "mwguoaskvramwgiweogzulcinycosovozppl",
                    "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
                    "uivcdsboxnraqpokjzaayedf",
                    "yalc",
                    "bbhlbmpskgxmxosft",
                    "vigplemkoni",
                    "krdrlctodtmprpxwditvcps",
                    "gqjwokkskrb",
                    "bslxxpabivbvzkozzvdaykaatzrpe",
                    "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
                    "siqbezhkohmgbenbkikcxmvz",
                    "ddmaireeouzcvffkcohxus",
                    "kjzguljbwsxlrd",
                    "gqzuqcljvcpmoqlnrxvzqwoyas",
                    "vadguvpsubcwbfbaviedr",
                    "nxnorutztxfnpvmukpwuraen",
                    "imgvujjeygsiymdxp",
                    "rdzkpk",
                    "cuap",
                    "qcojjumwp",
                    "pyqzshwykhtyzdwzakjejqyxbganow",
                    "cvxuskhcloxykcu",
                    "ul",
                    "axzscbjajazvbxffrydajapweci",
                ],
                queries=[
                    [4, 4],
                    [6, 17],
                    [10, 17],
                    [9, 18],
                    [17, 22],
                    [5, 23],
                    [2, 5],
                    [17, 21],
                    [5, 17],
                    [4, 8],
                    [7, 17],
                    [16, 19],
                    [7, 12],
                    [9, 20],
                    [13, 23],
                    [1, 5],
                    [19, 19],
                ],
            ),
        )


if __name__ == "__main__":
    unittest.main()
