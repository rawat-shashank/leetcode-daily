import unittest


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        c = 0
        for n in arr:
            if n % 2:
                c += 1
                if c == 3:
                    return True
            else:
                c = 0
        return False


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertFalse(
            self.sol.threeConsecutiveOdds(arr=[2, 6, 4, 1]),
        )

    def testcase2(self):
        self.assertTrue(
            self.sol.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12]),
        )


if __name__ == "__main__":
    unittest.main()
