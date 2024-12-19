import unittest
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """monotonic stack"""
        stack = []
        for x in arr:
            if not stack or x > stack[-1]:
                stack.append(x)
            else:
                max_el = stack[-1]
                while stack and x < stack[-1]:
                    stack.pop()
                stack.append(max_el)
        return len(stack)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        self.assertEqual(
            1,
            self.sol.maxChunksToSorted(arr=[4, 3, 2, 1, 0]),
        )

    def testcase2(self):
        self.assertEqual(4, self.sol.maxChunksToSorted(arr=[1, 0, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
