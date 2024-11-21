import unittest
from typing import List


class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        ans = set(nums)
        for i, idx in enumerate(moveFrom):
            if idx in ans:
                ans.remove(idx)
                ans.add(moveTo[i])
        return list(sorted(ans))


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [5, 6, 8, 9],
            self.sol.relocateMarbles(
                nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]
            ),
        )

    def testcase2(self):
        self.assertEqual(
            [2],
            self.sol.relocateMarbles(nums=[1, 1, 3, 3], moveFrom=[1, 3], moveTo=[2, 2]),
        )

    def testcase3(self):
        self.assertEqual(
            [1, 13, 22, 23, 33],
            self.sol.relocateMarbles(
                nums=[5, 13, 22, 23, 23, 33], moveFrom=[13, 5, 12], moveTo=[1, 12, 13]
            ),
        )


if __name__ == "__main__":
    unittest.main()
