import unittest


class Solution:
    def minSwaps(self, s: str) -> int:
        close, maxClose = 0, 0
        for ch in s:
            if ch == "[":
                close -= 1
            else:
                close += 1
            maxClose = max(close, maxClose)
        return (maxClose + 1) // 2


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(1, self.sol.minSwaps(s="][]["))

    def testcase2(self):
        self.assertEqual(2, self.sol.minSwaps(s="]]][[["))

    def testcase3(self):
        self.assertEqual(0, self.sol.minSwaps(s="[]"))


if __name__ == "__main__":
    unittest.main()
