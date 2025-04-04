import unittest
from typing import Optional
from helpers.listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """depth first search"""
        def dfs(root):
            if not root:
                return 0, None
            left = dfs(root.left)
            right = dfs(root.right)
            # if left depth is more
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if right[0] > left[0]:
                return right[0] + 1, right[1]
            # if both level are same
            return left[0] + 1, root
        return dfs(root)[1]


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([3,5,1,6,2,0,8,None,None,7,4])
        self.assertEqual(
            str(listToBinaryTree([2,7,4])),
            str(self.sol.lcaDeepestLeaves(root))
        )

    def testcase2(self):
        root = listToBinaryTree([1])
        self.assertEqual(
            str(listToBinaryTree([1])),
            str(self.sol.lcaDeepestLeaves(root))
        )

    def testcase3(self):
        root = listToBinaryTree([0,1,3,None,2])
        self.assertEqual(
            str(listToBinaryTree([2])), 
            str(self.sol.lcaDeepestLeaves(root))
        )

if __name__ == "__main__":
    unittest.main()
