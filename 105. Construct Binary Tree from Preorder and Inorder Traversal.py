import unittest
from helpers.listToBinaryTree import listToBinaryTree, TreeNode, identicalTrees


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        root: TreeNode = TreeNode(val=preorder[0])
        mid: int = inorder.index(preorder[0])
        root.left = self.buildTree(preorder=preorder[1:mid+1], inorder=inorder[:mid])
        root.right = self.buildTree(preorder=preorder[mid+1:], inorder=inorder[mid+1:])
        return root


class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[3,9,20,None,None,15,7])
        self.assertTrue(
            identicalTrees(
                root,
                Solution().buildTree(
                        preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
                )
            )
        )

    def testcase2(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[-1])
        self.assertTrue(
            identicalTrees(
                root,
                Solution().buildTree(
                        preorder = [-1], inorder = [-1]
                )
            )
        )

if __name__ == "__main__":
    _ = unittest.main()
