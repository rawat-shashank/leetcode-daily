import unittest
from typing import Optional
from helpers.listToBinaryTree import listToBinaryTree, TreeNode


class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #
    #     def dfs(root):
    #         if not root:
    #             # if no root we return true, and height=0,
    #             # deapth first bottom up height caculation
    #             return [True, 0]
    #
    #         left, right = dfs(root.left), dfs(root.right)
    #         # check if left, right or diff is less than 2, else return False
    #         balanced = left[0] and right[0] and abs(right[1] - left[1]) < 2
    #         return [balanced, 1 + max(left[1], right[1])]
    #     return dfs(root)[0]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """with height only"""

        def dfs(root):
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return dfs(root) >= 0


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        root = listToBinaryTree([3, 9, 20, None, None, 15, 7])
        self.assertTrue(self.sol.isBalanced(root))

    def testcase2(self):
        root = listToBinaryTree([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(self.sol.isBalanced(root))

    def testcase3(self):
        root = listToBinaryTree([])
        self.assertTrue(self.sol.isBalanced(root))


if __name__ == "__main__":
    unittest.main()
