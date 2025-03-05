import unittest

class Solution:

    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        self.assertEqual(
            first=1,
            second=Solution().coloredCells(n=1),
        )

    def testcase2(self) -> None:
        self.assertEqual(
            first=5,
            second=Solution().coloredCells(n=2),
        )

    def testcase3(self) -> None:
        self.assertEqual(
            first=13,
            second=Solution().coloredCells(n=3),
        )

    def testcase4(self) -> None:
        self.assertEqual(
            first=25,
            second=Solution().coloredCells(n=4),
        )
if __name__ == "__main__":
    unittest.main()
