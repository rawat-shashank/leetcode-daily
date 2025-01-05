import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """two pointer approach"""
        left, right = 0, len(numbers) - 1
        while left < right:
            tmp_sum = numbers[left] + numbers[right]
            if tmp_sum == target:
                return [left + 1, right + 1]
            if tmp_sum < target:
                left += 1
            if tmp_sum > target:
                right -= 1


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [1, 2],
            self.sol.twoSum(numbers=[2, 7, 11, 15], target=9),
        )

    def testcase2(self):
        self.assertEqual(
            [1, 3],
            self.sol.twoSum(numbers=[2, 3, 4], target=6),
        )

    def testcase3(self):
        self.assertEqual(
            [1, 2],
            self.sol.twoSum(numbers=[-1, 0], target=-1),
        )

    def testcase4(self):
        self.assertEqual(
            [3, 6],
            self.sol.twoSum(numbers=[3, 24, 50, 79, 88, 150, 345], target=200),
        )


if __name__ == "__main__":
    unittest.main()
