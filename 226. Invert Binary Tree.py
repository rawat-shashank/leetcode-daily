import unittest
from typing import Optional
from helpers.listToBinaryTree import listToBinaryTree, binaryTreeToList, TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class Testcases(unittest.TestCase):

    def testcase1(self):
        root = listToBinaryTree([4, 2, 7, 1, 3, 6, 9])
        expected = [4, 7, 2, 9, 6, 3, 1]
        actual_root = Solution().invertTree(root)
        actual = binaryTreeToList(actual_root)
        self.assertEqual(actual, expected)

    def testcase2(self):
        root = listToBinaryTree([2, 1, 3])
        expected = [2, 3, 1]
        actual_root = Solution().invertTree(root)
        actual = binaryTreeToList(actual_root)
        self.assertEqual(actual, expected)

    def testcase3(self):
        root = listToBinaryTree([])
        expected = []
        actual_root = Solution().invertTree(root)
        actual = binaryTreeToList(actual_root)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
