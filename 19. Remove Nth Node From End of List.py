import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """moving pointer n node ahead"""
        dummy = ListNode(val=0, next=head)

        slow, fast = dummy, head
        # move fast pointer n nodes ahead
        while n:
            fast = fast.next
            n -= 1

        # we will stop the fast pointer
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

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
        list1 = self.sol.make_linked_list([1, 2, 3, 4, 5])

        self.assertEqual(
            "1 -> 2 -> 3 -> 5",
            self.sol.print_linkedlist(self.sol.removeNthFromEnd(head=list1, n=2)),
        )

    def testcase2(self):
        list1 = self.sol.make_linked_list([1])

        self.assertEqual(
            "",
            self.sol.print_linkedlist(self.sol.removeNthFromEnd(head=list1, n=1)),
        )

    def testcase3(self):
        list1 = self.sol.make_linked_list([1, 2])

        self.assertEqual(
            "1",
            self.sol.print_linkedlist(self.sol.removeNthFromEnd(head=list1, n=1)),
        )


if __name__ == "__main__":
    unittest.main()
