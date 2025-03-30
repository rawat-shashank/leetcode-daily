import unittest


class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        # step1 is to find the last occ of all chars
        dp = {}
        for idx, ch in enumerate(s):
            dp[ch] = idx

        left = 0
        right = 0
        res = []

        # step two is a two-pointer to create partiation till
        # right pointer matches with current index
        for idx, ch in enumerate(s):
            right = max(right, dp[ch])
            if idx == right:
                res.append(right - left + 1)
                left = right + 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [9, 7, 8],
            self.sol.partitionLabels(s="ababcbacadefegdehijhklij"),
        )

    def testcase2(self):
        self.assertEqual([10], self.sol.partitionLabels(s="eccbbbbdec"))


if __name__ == "__main__":
    unittest.main()
