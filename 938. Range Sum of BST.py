# 938. Range Sum of BST
import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            ans = 0
            if low <= node.val <= high:
                ans = node.val
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            ans += left_sum + right_sum
            return ans

        return dfs(root)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(32, self.sol.rangeSumBST(root=root, low=7, high=15))

    def testcase2(self):
        root = listToBinaryTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(
            23,
            self.sol.rangeSumBST(root=root, low=6, high=10),
        )


if __name__ == "__main__":
    unittest.main()
