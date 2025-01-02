import unittest
from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)  # mapping char count to list of anagrams
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord("a")] += 1
    #         res[tuple(count)].append(s)
    #     return list(res.values())  # type: ignore

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # faster approach with sorted str key
        dp = defaultdict(list)
        for str in strs:
            tmp_str = "".join(sorted(str))
            dp[tmp_str].append(str)
        return list(dp.values())


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertequal(
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            self.sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
        )

    def testcase2(self):
        self.assertEqual([[""]], self.sol.groupAnagrams(strs=[""]))

    def testcase3(self):
        self.assertEqual([["a"]], self.sol.groupAnagrams(strs=["a"]))


if __name__ == "__main__":
    unittest.main()
