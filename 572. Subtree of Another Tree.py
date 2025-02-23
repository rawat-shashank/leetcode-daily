import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """based on leetcode 100 - issameTree"""
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False

        return dfs(p, q)


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        r1 = listToBinaryTree([3, 4, 5, 1, 2])
        r2 = listToBinaryTree([4, 1, 2])
        self.assertTrue(self.sol.isSubtree(r1, r2))

    def testcase2(self):
        r1 = listToBinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0])
        r2 = listToBinaryTree([4, 1, 2])
        self.assertFalse(self.sol.isSameTree(r1, r2))


if __name__ == "__main__":
    unittest.main()
