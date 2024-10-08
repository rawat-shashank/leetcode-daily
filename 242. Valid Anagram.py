import unittest
# from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False
        # return Counter(s) == Counter(t)
        if len(s) != len(t): return False
        dp = {}
        for x in s:
            if x in dp:
                dp[x]+=1
            else:
                dp[x] = 1
        for y in t:
            if y in dp:
                if dp[y] > 1:
                    dp[y] -= 1
                else:
                    del dp[y]
            else:
                return False
        if len(dp.keys()) == 0: return True
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(True, self.sol.isAnagram(s="anagram", t="nagaram"))

    def testcase2(self):
        self.assertEqual(False, self.sol.isAnagram(s="rat", t="car"))


if __name__ == "__main__":
    unittest.main()
