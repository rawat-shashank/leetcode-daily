import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = prev = ListNode()
        val, rem = 0, 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2
            if rem:
                val += rem
                rem = 0
            if val > 9:
                rem = val // 10
                val %= 10
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            new_node = ListNode(val)
            prev.next = new_node
            prev = new_node
        if rem:
            new_node = ListNode(rem)
            prev.next = new_node
            prev = new_node

        print(self.print_linkedlist(dummy.next))
        return dummy.next

    def addTwoNumbers(self, nums: List) -> ListNode:
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
        list1 = self.sol.addTwoNumbers([2, 4, 3])
        list2 = self.sol.addTwoNumbers([5, 6, 4])

        self.assertEqual(
            "7 -> 0 -> 8",
            self.sol.print_linkedlist(self.sol.mergeTwoLists(list1, list2)),
        )

    def testcase2(self):
        list1 = self.sol.addTwoNumbers([9, 9, 9, 9, 9, 9, 9])
        list2 = self.sol.addTwoNumbers([9, 9, 9, 9])

        self.assertEqual(
            "8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1",
            self.sol.print_linkedlist(self.sol.mergeTwoLists(list1, list2)),
        )


if __name__ == "__main__":
    unittest.main()
