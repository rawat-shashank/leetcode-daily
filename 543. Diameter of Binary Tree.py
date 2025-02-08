import unittest
from typing import Optional
from helpers.listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res


class Testcases(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(
            3, Solution().diameterOfBinaryTree(listToBinaryTree([1, 2, 3, 4, 5]))
        )

    def testcase2(self):
        self.assertEqual(1, Solution().diameterOfBinaryTree(listToBinaryTree([1, 2])))


if __name__ == "__main__":
    unittest.main()
