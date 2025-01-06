import unittest
from typing import List


class Solution:
    # def minOperations(self, boxes: str) -> List[int]:
    #     """brute force - accepted"""
    #     res = [0] * len(boxes)
    #     for i in range(len(boxes)):
    #         for j in range(len(boxes)):
    #             if i == j:
    #                 res[i] == 0
    #
    #             if boxes[j] == "1":
    #                 res[i] += abs(j - i)
    #     return res

    def minOperations(self, boxes: str) -> List[int]:
        """prefix"""
        left = [0] * len(boxes)
        right = [0] * len(boxes)
        ones = 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == "1":
                ones += 1
            left[i] = left[i - 1] + ones

        ones = 0
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == "1":
                ones += 1
            right[i] = right[i + 1] + ones
            left[i] += right[i]
        return left


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 1, 3],
            self.sol.minOperations(boxes="110"),
        )

    def testcase2(self):
        self.assertEqual(
            [11, 8, 5, 4, 3, 4],
            self.sol.minOperations(boxes="001011"),
        )


if __name__ == "__main__":
    unittest.main()
