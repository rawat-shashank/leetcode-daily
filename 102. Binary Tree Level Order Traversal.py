import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional, List
from collections import deque


class Solution:

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     """dfs - approach"""
    #     res = []
    #
    #     def dfs(curr, depth):
    #         if not curr:
    #             return None
    #         if len(res) == depth:
    #             res.append([])
    #
    #         res[depth].append(curr.val)
    #         dfs(curr.left, depth + 1)
    #         dfs(curr.right, depth + 1)
    #
    #     dfs(root, 0)
    #     return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """bfs - approach"""
        q = deque([])
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([3, 9, 20, None, None, 15, 7])
        self.assertEqual([[3], [9, 20], [15, 7]], self.sol.levelOrder(root))

    def testcase2(self):
        root = listToBinaryTree([1])
        self.assertEqual([[1]], self.sol.levelOrder(root))

    def testcase3(self):
        root = listToBinaryTree([])
        self.assertEqual([], self.sol.levelOrder(root))


if __name__ == "__main__":
    unittest.main()
