import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        while list1 and list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

        if not list1:
            while list2:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
        if not list2:
            while list1:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
        return res.next

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
        list1 = self.sol.make_linked_list([1, 2, 4])
        list2 = self.sol.make_linked_list([1, 3, 4])

        self.assertEqual(
            "1 -> 1 -> 2 -> 3 -> 4 -> 4",
            self.sol.print_linkedlist(self.sol.mergeTwoLists(list1, list2)),
        )

    def testcase2(self):
        list1 = self.sol.make_linked_list([])
        list2 = self.sol.make_linked_list([])

        self.assertEqual(
            "",
            self.sol.print_linkedlist(self.sol.mergeTwoLists(list1, list2)),
        )

    def testcase3(self):
        list1 = self.sol.make_linked_list([])
        list2 = self.sol.make_linked_list([0])

        self.assertEqual(
            "0",
            self.sol.print_linkedlist(self.sol.mergeTwoLists(list1, list2)),
        )


if __name__ == "__main__":
    unittest.main()
