import unittest
from collections import defaultdict


class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:

        def atLeastK(k):
            res = 0
            left= 0
            vowel_count = defaultdict(int)
            constant_count = 0
            for right in range(len(word)):
                if word[right] in 'aeiou':
                    vowel_count[word[right]] = vowel_count.get(word[right], 0) + 1
                else:
                    constant_count +=1

                while len(vowel_count) == 5 and constant_count >= k:
                    res += len(word) - right
                    if word[left] in 'aeiou':
                        vowel_count[word[left]] -= 1
                    else:
                        constant_count -=1
                    if vowel_count[word[left]] == 0:
                        vowel_count.pop(word[left])
                    left+=1
            return res

        return atLeastK(k) - atLeastK(k + 1)




class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(0, self.sol.countOfSubstrings(word = "aeioqq", k = 1))

    def testcase2(self):
        self.assertEqual(1, self.sol.countOfSubstrings(word = "aeiou", k = 0))

    def testcase3(self):
        self.assertEqual(
            3,
            self.sol.countOfSubstrings(word = "ieaouqqieaouqq", k = 1),
        )


if __name__ == "__main__":
    unittest.main()
