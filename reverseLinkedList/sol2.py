# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # Edge case: If head is None or left == right, no reversal needed
        if not head or left == right:
            return head

        # Create a dummy node to handle edge cases smoothly
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to one node before the `left` position
        for _ in range(left - 1):
            prev = prev.next

        # `start` is the first node of the reversed segment
        # `then` is the node that will be moved to the beginning of the reversed segment
        start = prev.next
        then = start.next

        # Reverse the sublist from left to right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next
