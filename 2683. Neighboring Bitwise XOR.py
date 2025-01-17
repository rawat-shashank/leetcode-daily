import unittest
from typing import List


class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """calculative XOR and sum parity"""
        return sum(derived) % 2 == 0


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertTrue(
            self.sol.doesValidArrayExist(derived=[1, 1, 0]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.doesValidArrayExist(derived=[1, 1]),
        )

    def testcase3(self):
        self.assertFalse(
            self.sol.doesValidArrayExist(derived=[1, 0]),
        )


if __name__ == "__main__":
    unittest.main()
