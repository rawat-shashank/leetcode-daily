import unittest
from helpers.listToBinaryTree import TreeNode


class Solution:
    # def lowestCommonAncestor(
    #     self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    # ) -> "TreeNode":
    #     """binary tree recursive"""
    #     if not root or not p or not q:
    #         return None
    #     if max(p.val, q.val) < root.val:
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     if min(p.val, q.val) > root.val:
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     else:
    #         return root

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """binary tree - iterativily"""
        while root:
            # if both val is smaller, we move towards left
            if max(p.val, q.val) < root.val:
                root = root.left
            # if both val is bigger, we move towards right
            elif min(p.val, q.val) > root.val:
                root = root.right
            # one is smaller and another is bigger, we got the answer
            else:
                return root


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        p = root.left
        q = root.right
        self.assertEqual(root, self.sol.lowestCommonAncestor(root, p, q))

    def testcase2(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left
        q = root.left.right

        expected = root.left
        self.assertEqual(expected, self.sol.lowestCommonAncestor(root, p, q))

    def testcase3(self):
        root = TreeNode(2)
        root.left = TreeNode(1)

        p = root
        q = root.left

        expected = root
        self.assertEqual(expected, self.sol.lowestCommonAncestor(root, p, q))


if __name__ == "__main__":
    unittest.main()
