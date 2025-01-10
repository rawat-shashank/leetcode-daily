import unittest
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxChCount = [0] * 26
        for word in words2:
            counts1 = [0] * 26
            for ch in word:
                tmpIdx = ord(ch) - ord("a")
                counts1[tmpIdx] += 1
                maxChCount[tmpIdx] = max(maxChCount[tmpIdx], counts1[tmpIdx])
        ans = []
        for word in words1:
            counts2 = [0] * 26
            for ch in word:
                counts2[ord(ch) - ord("a")] += 1
            if all([x >= y for x, y in zip(counts2, maxChCount)]):
                ans.append(word)
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            ["facebook", "google", "leetcode"],
            self.sol.wordSubsets(
                words1=["amazon", "apple", "facebook", "google", "leetcode"],
                words2=["e", "o"],
            ),
        )

    def testcase2(self):
        self.assertEqual(
            ["apple", "google", "leetcode"],
            self.sol.wordSubsets(
                words1=["amazon", "apple", "facebook", "google", "leetcode"],
                words2=["l", "e"],
            ),
        )

    def testcase3(self):
        self.assertEqual(
            ["google", "leetcode"],
            self.sol.wordSubsets(
                words1=["amazon", "apple", "facebook", "google", "leetcode"],
                words2=["lo", "eo"],
            ),
        )


if __name__ == "__main__":
    unittest.main()
