import unittest
from heapq import heapify, heappop, heappush

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //=3
        return True



class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            True,
            self.sol.checkPowersOfThree(n = 12),
        )

    def testcase2(self):
        self.assertEqual(
            True,
            self.sol.checkPowersOfThree(n = 91),
        )

    def testcase3(self):
        self.assertEqual(
            False,
            self.sol.checkPowersOfThree(n = 21),
        )

if __name__ == "__main__":
    unittest.main()
