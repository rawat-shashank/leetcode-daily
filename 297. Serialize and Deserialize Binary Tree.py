import unittest
from helpers.listToBinaryTree import identicalTrees, listToBinaryTree, TreeNode


class Solution:
    def serialize(self, root: TreeNode | None) -> str:
        res: list[str] = []
        def dfs(node:TreeNode | None) -> None:
            if not node:
                res.append('N')
                return None
            res.append(str(node.val))
            dfs(node=node.left)
            dfs(node=node.right)

        dfs(node=root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode | None:
        vals: list[str] = data.split(sep=",")
        index = 0

        def innerDFS() -> TreeNode | None:
            nonlocal index
            if vals[index] == 'N':
                index += 1
                return None
            node: TreeNode = TreeNode(val=int(vals[index]))
            index += 1
            node.left = innerDFS()
            node.right = innerDFS()
            return node

        return innerDFS()

class Testcases(unittest.TestCase):

    def testcase1(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[1,2,3,None,None,4,5])
        self.assertEqual(
            first="1,2,N,N,3,4,N,N,5,N,N",
            second=Solution().serialize(root=root)
        )

        self.assertTrue(
            identicalTrees(
                a=root,
                b=Solution().deserialize(data="1,2,N,N,3,4,N,N,5,N,N")
            )
        )

    def testcase2(self) -> None:
        root: TreeNode | None = listToBinaryTree(items=[])
        self.assertEqual(
            first="N",
            second=Solution().serialize(root=root)
        )

        self.assertTrue(
            identicalTrees(
                a=root,
                b=Solution().deserialize(data="N")
            )
        )

if __name__ == "__main__":
    _ = unittest.main()
