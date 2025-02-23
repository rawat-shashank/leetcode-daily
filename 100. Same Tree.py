import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional


class Solution:

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
        r1 = listToBinaryTree([1, 2, 3])
        r2 = listToBinaryTree([1, 2, 3])
        self.assertTrue(self.sol.isSameTree(r1, r2))

    def testcase2(self):
        r1 = listToBinaryTree([1, 2])
        r2 = listToBinaryTree([1, None, 2])
        self.assertFalse(self.sol.isSameTree(r1, r2))

    def testcase3(self):
        r1 = listToBinaryTree([1, 2, 1])
        r2 = listToBinaryTree([1, 1, 2])
        self.assertFalse(self.sol.isSameTree(r1, r2))


if __name__ == "__main__":
    unittest.main()
