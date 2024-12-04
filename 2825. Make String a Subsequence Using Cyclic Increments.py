import unittest


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """Two pointer, simple  check with ord"""
        l1, l2 = len(str1), len(str2)
        l2_idx = 0
        for l1_idx in range(l1):
            if l2_idx < l2 and (
                str1[l1_idx] == str2[l2_idx]
                or ord(str1[l1_idx]) + 1 == ord(str2[l2_idx])
                or ord(str1[l1_idx]) - 25 == ord(str2[l2_idx])
            ):
                l2_idx += 1
        return l2_idx == l2


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canMakeSubsequence(str1="abc", str2="ad"),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.canMakeSubsequence(str1="zc", str2="ad"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.canMakeSubsequence(str1="ab", str2="d"),
        )


if __name__ == "__main__":
    unittest.main()
