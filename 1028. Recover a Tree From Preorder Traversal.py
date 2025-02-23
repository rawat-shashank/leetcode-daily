import unittest
from typing import Optional
from helpers.listToBinaryTree import TreeNode, binaryTreeToList


class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        dashes = 0
        while i < len(traversal):
            # first we count dashes between current and next number
            if traversal[i] == "-":
                dashes += 1
                i += 1
            else:
                j = i
                # getting the current number till either the end of traversal
                # string or till next dash
                while j < len(traversal) and traversal[j] != "-":
                    j += 1
                # make the number int
                num = int(traversal[i:j])
                node = TreeNode(num)

                # get to the node where we will be adding current node
                while len(stack) > dashes:
                    stack.pop()

                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                stack.append(node)
                i = j
                dashes = 0
        return stack[0]


class Testcases(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        actual = [1, 2, 5, 3, 4, 6, 7]
        expected = binaryTreeToList(
            self.sol.recoverFromPreorder(traversal="1-2--3--4-5--6--7")
        )
        self.assertEqual(actual, expected)

    def testcase2(self):
        actual = [1, 2, 5, 3, None, 6, None, 4, None, 7]
        expected = binaryTreeToList(
            self.sol.recoverFromPreorder(traversal="1-2--3---4-5--6---7")
        )
        self.assertEqual(actual, expected)

    def testcase3(self):
        actual = [1, 401, None, 349, 88, 90]
        expected = binaryTreeToList(
            self.sol.recoverFromPreorder(traversal="1-401--349---90--88")
        )
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
