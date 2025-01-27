import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # fast and slow traversal to find the middle node
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next

        # reverse the remaing node after middle
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        slow.next = None

        # start from head and reversed element of remaining half
        # and merge them together
        head1, head2 = head, prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next

        return head

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
        list1 = self.sol.make_linked_list([1, 2, 3, 4])

        self.assertEqual(
            "1 -> 4 -> 2 -> 3",
            self.sol.print_linkedlist(self.sol.reorderList(list1)),
        )

    def testcase2(self):
        list1 = self.sol.make_linked_list([1, 2, 3, 4, 5])

        self.assertEqual(
            "1 -> 5 -> 2 -> 4 -> 3",
            self.sol.print_linkedlist(self.sol.reorderList(list1)),
        )


if __name__ == "__main__":
    unittest.main()
