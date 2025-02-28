import unittest
from helpers.listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(node:TreeNode | None) -> int:
            nonlocal res
            if not node:
                return 0

            leftMax = max(0, dfs(node=node.left))
            rightMax = max(0, dfs(node=node.right))
            
            res = max(
                res,
                node.val + leftMax + rightMax
            )

            return node.val + max(leftMax, rightMax)


        dfs(node=root)
        return res


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[1,2,3])
        self.assertEqual(
            first=6,
            second=Solution().maxPathSum(root=root)
        )

    def testcase2(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[-10,9,20,None,None,15,7])
        self.assertEqual(
            first=42,
            second=Solution().maxPathSum(root)
        )

if __name__ == "__main__":
    _ = unittest.main()
