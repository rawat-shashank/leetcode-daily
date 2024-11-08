from typing import List
import unittest


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        ans = []
        mask = (1 << maximumBit) - 1
        for n in nums[-1::-1]:
            ans.append(xor ^ mask)
            xor ^= n
        return ans


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            [0, 3, 2, 3],
            self.sol.getMaximumXor(nums=[0, 1, 1, 3], maximumBit=2),
        )

    def testcase2(self):
        self.assertEqual(
            [5, 2, 6, 5],
            self.sol.getMaximumXor(nums=[2, 3, 4, 7], maximumBit=3),
        )

    def testcase3(self):
        self.assertEqual(
            [4, 3, 6, 4, 6, 7],
            self.sol.getMaximumXor(nums=[0, 1, 2, 2, 5, 7], maximumBit=3),
        )


if __name__ == "__main__":
    unittest.main()
