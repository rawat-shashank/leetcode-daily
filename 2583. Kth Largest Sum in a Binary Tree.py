from collections import deque
from heapq import heappop, heappush
import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, listToBinaryTree


class Solution:
    def KthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        min_heap = []

        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heappop(min_heap)
        return -1 if len(min_heap) < k else min_heap[0]


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([5, 8, 9, 2, 1, 3, 7, 4, 6])
        self.assertEqual(13, self.sol.KthLargestLevelSum(root=root, k=2))

    def testcase2(self):
        root = listToBinaryTree([1, 2, None, 3])
        self.assertEqual(3, self.sol.KthLargestLevelSum(root=root, k=1))


if __name__ == "__main__":
    unittest.main()
