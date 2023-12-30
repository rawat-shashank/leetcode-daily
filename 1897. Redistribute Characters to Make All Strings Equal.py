# 1897. Redistribute Characters to Make All Strings Equal
import unittest
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        words_len = len(words)
        if words_len == 1:
            return True
        if sum(len(word) for word in words) % words_len != 0:
            return False
        char_map = [0] * 26
        for word in words:
            for char in word:
                char_map[ord(char) - ord("a")] += 1
        for num in char_map:
            if num % words_len != 0:
                return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(True, self.sol.makeEqual(words=["abc", "aabc", "bc"]))

    def testcase2(self):
        self.assertEqual(False, self.sol.makeEqual(words=["ab", "a"]))


if __name__ == "__main__":
    unittest.main()
