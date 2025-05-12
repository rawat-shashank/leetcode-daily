import unittest


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        # composition
        res = set()
        N = len(digits)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if 100 <= num and num % 2 == 0:
                        res.add(num)
        return sorted(list(res))


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
            self.sol.findEvenNumbers(digits=[2, 1, 3, 0]),
        )

    def testcase2(self):
        self.assertEqual(
            [222, 228, 282, 288, 822, 828, 882],
            self.sol.findEvenNumbers(digits=[2, 2, 8, 8, 2]),
        )

    def testcase3(self):
        self.assertEqual(
            [],
            self.sol.findEvenNumbers(digits=[3, 7, 5]),
        )


if __name__ == "__main__":
    unittest.main()
