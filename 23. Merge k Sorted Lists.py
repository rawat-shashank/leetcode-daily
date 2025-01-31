import unittest
from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:

    # def mergeTwoLists(
    #     self, list1: Optional[ListNode], list2: Optional[ListNode]
    # ) -> Optional[ListNode]:
    #     head = curr = ListNode()
    #
    #     while list1 and list2:
    #         if list1.val < list2.val:
    #             curr.next = list1
    #             list1 = list1.next
    #         else:
    #             curr.next = list2
    #             list2 = list2.next
    #         curr = curr.next
    #
    #     if list1:
    #         curr.next = list1
    #     if list2:
    #         curr.next = list2
    #
    #     return head.next
    #
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """using merge two sorted list"""
    #     if len(lists) == 0:
    #         return None
    #
    #     for i in range(1, len(lists)):
    #         lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])
    #     return lists[-1]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """using min heap"""
        values = []
        for list in lists:
            while list:
                heappush(values, list.val)
                list = list.next

        head = curr = ListNode()
        while values:
            val = heappop(values)
            temp = ListNode(val)
            curr.next = temp
            curr = curr.next
        return head.next


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Testcases(unittest.TestCase):
    def testcase1(self):
        solution = Solution()
        list1 = create_linked_list([1, 4, 5])
        list2 = create_linked_list([1, 3, 4])
        list3 = create_linked_list([2, 6])
        merged_list = solution.mergeKLists([list1, list2, list3])
        self.assertEqual(linked_list_to_list(merged_list), [1, 1, 2, 3, 4, 4, 5, 6])

    def testcase2(self):
        solution = Solution()
        self.assertIsNone(solution.mergeKLists([]))

    def testcase3(self):
        solution = Solution()
        self.assertIsNone(solution.mergeKLists([[]]))


if __name__ == "__main__":
    unittest.main()
