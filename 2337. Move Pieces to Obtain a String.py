import unittest


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """two pointer"""
        str_len = len(start)
        l1, l2 = 0, 0
        while l1 < str_len or l2 < str_len:
            # skip all empty spaces for both start, target
            while l1 < str_len and start[l1] == "_":
                l1 += 1
            while l2 < str_len and target[l2] == "_":
                l2 += 1

            # if l1, l2 aren't equal at end,
            # theres mismatch on len, or number of L or R
            if l1 == str_len or l2 == str_len:
                return l1 == str_len and l2 == str_len

            # L and R should be in same order
            # irrespective of there pos in string
            if (
                start[l1] != target[l2]
                or (start[l1] == "L" and l1 < l2)
                or (start[l1] == "R" and l1 > l2)
            ):
                return False

            l1 += 1
            l2 += 1
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.canChange(start="_L__R__R_", target="L______RR"),
        )

    def testcase2(self):
        self.assertFalse(
            self.sol.canChange(start="R_L_", target="__LR"),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.canChange(start="_R", target="R_"),
        )


if __name__ == "__main__":
    unittest.main()
