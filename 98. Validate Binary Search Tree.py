import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional
from collections import deque


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def dfs(node, left, right):
    #         if not node:
    #             return True
    #         if not (left < node.val < right):
    #             return False
    #
    #         # check with left node, smallest left value and current
    #         # node.val as right limit for left side of tree
    #         # nove.val as left limit for right side of tree
    #         return (
    #             dfs(node.left, left, node.val)
    #             and dfs(node.right, node.val, right)
    #         )
    #
    #     return dfs(root, float("-inf"), float("inf"))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """using bfs"""
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))

            if node.right:
                q.append((node.right, node.val, right))
        return True


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([2, 1, 3])
        self.assertTrue(self.sol.isValidBST(root))

    def testcase2(self):
        root = listToBinaryTree([5, 1, 4, None, None, 3, 6])
        self.assertFalse(self.sol.isValidBST(root))

    def testcase3(self):
        root = listToBinaryTree([2, 2, 2])
        self.assertFalse(self.sol.isValidBST(root))

    def testcase4(self):
        root = listToBinaryTree([5, 4, 6, None, None, 3, 7])
        self.assertFalse(self.sol.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
