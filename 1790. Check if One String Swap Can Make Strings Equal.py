import unittest
from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif Counter(s1) != Counter(s2):
            return False
        else:
            res = 0
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    continue

                res += 1
                if res > 2:
                    return False
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.areAlmostEqual(s1="bank", s2="kanb"),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.areAlmostEqual(s1="kelb", s2="kelb"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.areAlmostEqual(s1="attack", s2="defend"),
        )

    def testcase4(self):
        self.assertFalse(
            self.sol.areAlmostEqual(s1="aa", s2="ac"),
        )


if __name__ == "__main__":
    unittest.main()
