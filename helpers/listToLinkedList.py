from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_list(head: Optional[ListNode]) -> List:
    """Helper function to convert a linked list to a list for easy comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def create_linked_list(values: List) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
