import unittest
from helpers.listToBinaryTree import TreeNode, listToBinaryTree
from typing import Optional
from collections import deque
# from heapq import heappush, heappop


class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     """using bfs and heap"""
    #     res = []
    #     q = deque([root])
    #     while q:
    #         node = q.popleft()
    #         heappush(res, node.val)
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     ans = 0
    #     while k:
    #         ans = heappop(res)
    #         k -= 1
    #     else:
    #         return ans

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     res = root.val
    #
    #     def dfs(node):
    #         nonlocal k, res
    #         if not node:
    #             return
    #         dfs(node.left)
    #         k -= 1
    #         if not k:
    #             res = node.val
    #             return
    #         dfs(node.right)
    #
    #     dfs(root)
    #     return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """dfs - iterative"""
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                # move as left as possible
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([3, 1, 4, None, 2])
        self.assertEqual(1, self.sol.kthSmallest(root, k=1))

    def testcase2(self):
        root = listToBinaryTree([5, 3, 6, 2, 4, None, None, 1])
        self.assertEqual(3, self.sol.kthSmallest(root, k=3))


if __name__ == "__main__":
    unittest.main()
