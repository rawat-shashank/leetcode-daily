from typing import Optional, List


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.data
        right = None if self.right is None else self.right.data
        return "(D:{}, L:{}, R:{})".format(self.val, left, right)

    def __str__(self) -> str:
        return str(self.val)

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val, self.left, self.right)
        if self.right:
            self.right.printTree()


def listToBinaryTree(items: list) -> Optional[TreeNode]:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


def binaryTreeToList(root: Optional[TreeNode]) -> List:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def identicalTrees(a, b):
    # 1. Both empty
    if a is None and b is None:
        return True

    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return (
            (a.val == b.val)
            and identicalTrees(a.left, b.left)
            and identicalTrees(a.right, b.right)
        )

    # 3. one empty, one not -- false
    return False
