import unittest
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        if head in self.hashmap:
            return self.hashmap[head]

        copy = Node(head.val)
        self.hashmap[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.hashmap.get(head.random)
        return copy


class TestCases(unittest.TestCase):
    def list_to_linked_list(self, lst: list) -> Optional[Node]:
        if not lst:
            return None

        nodes = []  # Store created nodes for easy random pointer assignment
        head = Node(lst[0][0])
        curr = head
        nodes.append(head)

        for i in range(1, len(lst)):
            new_node = Node(lst[i][0])
            curr.next = new_node
            curr = new_node
            nodes.append(curr)

        # Assign random pointers
        for i, node_info in enumerate(lst):
            if node_info[1] is not None:
                nodes[i].random = nodes[node_info[1]]

        return head

    def _compare_lists(self, head1, head2):
        """Helper function to compare two linked lists"""
        while head1 and head2:
            self.assertEqual(head1.val, head2.val)
            if head1.random and head2.random:
                if head1.random.val != head2.random.val:
                    return False
            elif head1.random != head2.random:
                return False
            head1 = head1.next
            head2 = head2.next
        return head1 is None and head2 is None

    def testcase1(self):
        head = self.list_to_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        copiedList = Solution().copyRandomList(head)
        self.assertTrue(self._compare_lists(head, copiedList))

    def testcase2(self):
        head = self.list_to_linked_list([[1, 1], [2, 1]])
        copiedList = Solution().copyRandomList(head)
        self.assertTrue(self._compare_lists(head, copiedList))

    def testcase3(self):
        head = self.list_to_linked_list([[3, None], [3, 0], [3, None]])
        copiedList = Solution().copyRandomList(head)
        self.assertTrue(self._compare_lists(head, copiedList))


if __name__ == "__main__":
    unittest.main()
