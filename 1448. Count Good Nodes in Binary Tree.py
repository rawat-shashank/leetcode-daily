import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, parentValue):
            if not node:
                return 0
            res = 1 if node.val >= parentValue else 0
            parentValue = max(parentValue, node.val)
            res += dfs(node.left, parentValue)
            res += dfs(node.right, parentValue)
            return res

        return dfs(root, root.val)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([3, 1, 4, 3, None, 1, 5])
        self.assertEqual(4, self.sol.goodNodes(root))

    def testcase2(self):
        root = listToBinaryTree([3, 3, None, 4, 2])
        self.assertEqual(3, self.sol.goodNodes(root))

    def testcase3(self):
        root = listToBinaryTree([1])
        self.assertEqual(1, self.sol.goodNodes(root))

    def testcase4(self):
        root = listToBinaryTree([2, None, 4, None, None, 10, 8, None, None, 4])
        root.printTree()
        self.assertEqual(4, self.sol.goodNodes(root))


if __name__ == "__main__":
    unittest.main()
