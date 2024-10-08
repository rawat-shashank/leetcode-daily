# 872. Leaf-Similar Trees
import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leafs):
            if not node:
                return
            if not node.left and not node.right:
                leafs.append(node.val)
                return
            dfs(node.left, leafs)
            dfs(node.right, leafs)

        leaf1, leaf2 = [], []
        dfs(root1, leaf1)
        dfs(root2, leaf2)
        return leaf1 == leaf2


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root1 = listToBinaryTree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = listToBinaryTree(
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
        )
        self.assertEqual(True, self.sol.leafSimilar(root1, root2))

    def testcase2(self):
        root1 = listToBinaryTree([1, 2, 3])
        root2 = listToBinaryTree([1, 3, 2])
        self.assertEqual(False, self.sol.leafSimilar(root1, root2))


if __name__ == "__main__":
    unittest.main()
