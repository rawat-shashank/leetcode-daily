import unittest


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, cur_set):
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                if substr not in cur_set:
                    cur_set.add(substr)
                    res = max(res, 1 + dfs(j + 1, cur_set))
                    cur_set.remove(substr)
            return res

        return dfs(0, set())


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(5, self.sol.maxUniqueSplit(s="ababccc"))

    def testcase2(self):
        self.assertEqual(2, self.sol.maxUniqueSplit(s="aba"))

    def testcase3(self):
        self.assertEqual(1, self.sol.maxUniqueSplit(s="aa"))


if __name__ == "__main__":
    unittest.main()
