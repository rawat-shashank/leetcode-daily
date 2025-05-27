import unittest


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """iteration"""
        n1 = n2 = 0
        for i in range(1, n + 1):
            if i % m == 0:
                n2 += i
            else:
                n1 += i
        print(n1, n2)
        return n1 - n2


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(19, self.sol.differenceOfSums(n=10, m=3))

    def testcase2(self):
        self.assertEqual(15, self.sol.differenceOfSums(n=5, m=6))

    def testcase3(self):
        self.assertEqual(-15, self.sol.differenceOfSums(n=5, m=1))


if __name__ == "__main__":
    unittest.main()
