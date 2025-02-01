import unittest
from typing import List, Optional
from helpers.listToLinkedList import create_linked_list, linked_list_to_list, ListNode


class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     """using recursion"""
    #     curr = head
    #     i = 0
    #     while curr and i < k:
    #         curr = curr.next
    #         i += 1
    #
    #     # will only do recursive call if we have k elements
    #     if i == k:
    #         curr = self.reverseKGroup(head=curr, k=k)
    #
    #         while i:
    #             temp = head.next
    #             head.next = curr
    #             curr = head
    #             head = temp
    #             i -= 1
    #         head = curr
    #     return head

    def getKthNode(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(None, head)
        groupPrev = res

        while True:
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break

            # refernce to move forward in the given list
            groupNext = kthNode.next

            prev, curr = kthNode.next, groupPrev.next
            # reverse the list
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # last element reference for next reverse
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp

        return res.next


class TestReverseKGroup(unittest.TestCase):

    def _test_reverse_k_group(self, head_values: List, k: int, expected_values: List):
        head = create_linked_list(head_values)
        result_head = Solution().reverseKGroup(head, k)
        result_values = linked_list_to_list(result_head)
        self.assertEqual(result_values, expected_values)

    def test_reverse_k_group_1(self):
        self._test_reverse_k_group([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])

    def test_reverse_k_group_2(self):
        self._test_reverse_k_group([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])


if __name__ == "__main__":
    unittest.main()
