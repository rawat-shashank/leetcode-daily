import unittest


class Solution:
    # def countSymmetricIntegers(self, low: int, high: int) -> int:
    #     """brute force"""
    #     res = 0
    #     for idx in range(low, high + 1):
    #         s = str(idx)
    #         l = len(s)
    #         if l % 2:
    #             continue
    #         j = l // 2
    #         if sum(int(x) for x in s[:j]) == sum(int(x) for x in s[j:]):
    #             res += 1
    #     return res

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """Enumeration"""
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            9,
            self.sol.countSymmetricIntegers(low=1, high=100),
        )

    def testcase2(self):
        self.assertEqual(
            4,
            self.sol.countSymmetricIntegers(low=1200, high=1230),
        )


if __name__ == "__main__":
    unittest.main()
