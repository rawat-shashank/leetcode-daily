import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """String representation for easy printing."""
        if not self.head:
            return "Empty LinkedList"

        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_n = None
        while head:
            tmp = head.next
            head.next = prev_n
            prev_n = head
            head = tmp
        return prev_n

    def make_linked_list(self, nums: List) -> ListNode:
        if not len(nums):
            return
        head = ListNode(nums[0])
        current = head
        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            current.next = new_node
            current = new_node
        return head

    def print_linkedlist(self, head):

        current = head
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        head = self.sol.make_linked_list(nums=[1, 2, 3, 4, 5])

        self.assertEqual(
            "5 -> 4 -> 3 -> 2 -> 1",
            self.sol.print_linkedlist(self.sol.reverseList(head)),
        )

    def testcase2(self):
        head = self.sol.make_linked_list(nums=[1, 2])

        self.assertEqual(
            "2 -> 1",
            self.sol.print_linkedlist(self.sol.reverseList(head)),
        )

    def testcase3(self):
        head = self.sol.make_linked_list(nums=[])

        self.assertEqual(
            "",
            self.sol.print_linkedlist(self.sol.reverseList(head)),
        )


if __name__ == "__main__":
    unittest.main()
