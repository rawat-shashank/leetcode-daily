import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        self.used = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.used

    def dfs(self, root, x):
        """preprocessing with dfs"""
        if root is None:
            return
        self.used.add(x)
        self.dfs(root.left, 2 * x + 1)
        self.dfs(root.right, 2 * x + 2)


class Testcases(unittest.TestCase):

    def testcase1(self):
        root = listToBinaryTree([-1, None, -1])
        fe = FindElements(root)
        self.assertEqual(fe.find(1), False)
        self.assertEqual(fe.find(2), True)

    def testcase2(self):
        root = listToBinaryTree([-1, -1, -1, -1, -1])
        fe = FindElements(root)
        self.assertEqual(fe.find(1), True)
        self.assertEqual(fe.find(3), True)
        self.assertEqual(fe.find(5), False)

    def testcase3(self):
        root = listToBinaryTree([-1, None, -1, -1, None, -1])
        fe = FindElements(root)
        self.assertEqual(fe.find(2), True)
        self.assertEqual(fe.find(3), False)
        self.assertEqual(fe.find(4), False)
        self.assertEqual(fe.find(5), True)


if __name__ == "__main__":
    unittest.main()
