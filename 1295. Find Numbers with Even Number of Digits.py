import unittest
from typing import List


class Solution:
    # def findNumbers(self, nums: list[int]) -> int:
    #     res = 0
    #     for num in nums:
    #         if not len(str(num)) % 2:
    #             res += 1
    #     return res

    def findNumbers(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            if 10 <= num <= 99 or (1000 <= num <= 9999) or num == 100000:
                res += 1
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            2,
            self.sol.findNumbers(nums=[12, 345, 2, 6, 7896]),
        )

    def testcase2(self):
        self.assertEqual(
            1,
            self.sol.findNumbers(nums=[555, 901, 482, 1771]),
        )


if __name__ == "__main__":
    unittest.main()
