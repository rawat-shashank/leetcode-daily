import unittest
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """slow, fast pointer - fast eventually will caught up with slow in cycle"""
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """slow, fast pointer - same approach faster runtime"""
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def make_linked_list(self, nums: List, pos: int) -> ListNode:
        if not len(nums):
            return
        head = ListNode(nums[0])
        i = 1
        current = head
        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            current.next = new_node
            current = new_node
            if i == pos:
                temp = new_node
        if pos != -1 and temp:
            current.next = temp
        return head


class Testcases(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testcase1(self):
        list1 = self.sol.make_linked_list(nums=[3, 2, 0, -4], pos=1)
        self.assertTrue(self.sol.hasCycle(list1))

    def testcase2(self):
        list1 = self.sol.make_linked_list(nums=[1, 2], pos=0)
        self.assertTrue(self.sol.hasCycle(list1))

    def testcase3(self):
        list1 = self.sol.make_linked_list(nums=[1], post=-1)
        self.assertFalse(self.sol.hasCycle(list1))

    def testcase4(self):
        list1 = self.sol.make_linked_list(
            nums=[
                -21,
                10,
                17,
                8,
                4,
                26,
                5,
                35,
                33,
                -7,
                -16,
                27,
                -12,
                6,
                29,
                -12,
                5,
                9,
                20,
                14,
                14,
                2,
                13,
                -24,
                21,
                23,
                -21,
                5,
            ],
            pos=-1,
        )
        self.assertFalse(self.sol.hasCycle(list1))


if __name__ == "__main__":
    unittest.main()
