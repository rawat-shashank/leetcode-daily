import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional, List
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                # adding only last element to res
                res.append(level[-1])
        return res


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([1, 2, 3, None, 5, None, 4])
        self.assertEqual([1, 3, 4], self.sol.rightSideView(root))

    def testcase2(self):
        root = listToBinaryTree([1, 2, 3, 4, None, None, None, 5])
        self.assertEqual([1, 3, 4, 5], self.sol.rightSideView(root))

    def testcase3(self):
        root = listToBinaryTree([1, None, 3])
        self.assertEqual([1, 3], self.sol.rightSideView(root))

    def testcase4(self):
        root = listToBinaryTree([])
        self.assertEqual([], self.sol.rightSideView(root))


if __name__ == "__main__":
    unittest.main()
