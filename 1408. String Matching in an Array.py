import unittest
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """brute force - accepted"""
        if not words:
            return []
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    res.add(words[i])
        return [word for word in res]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            ["as", "hero"],
            self.sol.stringMatching(words=["mass", "as", "hero", "superhero"]),
        )

    def testcase2(self):
        self.assertEqual(
            ["et", "code"], self.sol.stringMatching(words=["leetcode", "et", "code"])
        )

    def testcase3(self):
        self.assertEqual([], self.sol.stringMatching(words=["blue", "green", "bu"]))

    def testcase4(self):
        self.assertEqual(
            ["leetcode", "od", "am"],
            self.sol.stringMatching(
                words=["leetcoder", "leetcode", "od", "hamlet", "am"]
            ),
        )


if __name__ == "__main__":
    unittest.main()
