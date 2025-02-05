import unittest
from typing import Optional
from helpers.listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class Testcases(unittest.TestCase):

    def testcase1(self):
        root = listToBinaryTree([3, 9, 20, None, None, 15, 7])
        expected = 3
        self.assertEqual(expected, Solution().maxDepth(root))

    def testcase2(self):
        root = listToBinaryTree([1, None, 2])
        expected = 2
        self.assertEqual(expected, Solution().maxDepth(root))


if __name__ == "__main__":
    unittest.main()
