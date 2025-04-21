import unittest


class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        min_n = max_n = curr = 0
        for diff in differences:
            curr += diff
            min_n = min(min_n, curr)
            max_n = max(max_n, curr)
            if (max_n - min_n) > upper - lower:
                return 0
        return (upper - lower) - (max_n - min_n) + 1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2, self.sol.numberOfArrays(differences=[1, -3, 4], lower=1, upper=6)
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.numberOfArrays(differences=[3, -4, 5, 1, -2], lower=-4, upper=5),
        )

    def testcase3(self):
        self.assertEqual(
            0,
            self.sol.numberOfArrays(differences=[4, -7, 2], lower=3, upper=6),
        )


if __name__ == "__main__":
    unittest.main()
