from collections import deque
from heapq import heappop, heappush
import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, identicalTrees, listToBinaryTree


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        q = deque([root])  # only because we are garanteed no empty root
        while q:
            cur_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(cur_sum)

        q = deque([root])
        root.val = 0
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                if node.left:
                    node.left.val = level_sum[level + 1] - child_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = level_sum[level + 1] - child_sum
                    q.append(node.right)
            level += 1
        return root


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root1 = listToBinaryTree([5, 4, 9, 1, 10, None, 7])
        root2 = listToBinaryTree([0, 0, 0, 7, 7, None, 11])
        res = self.sol.replaceValueInTree(root=root1)
        self.assertEqual(True, identicalTrees(root2, res))

    def testcase2(self):
        root1 = listToBinaryTree([3, 1, 2])
        root2 = listToBinaryTree([0, 0, 0])
        res = self.sol.replaceValueInTree(root=root1)
        self.assertEqual(True, identicalTrees(root2, res))


if __name__ == "__main__":
    unittest.main()
