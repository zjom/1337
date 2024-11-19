# https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def rotateRight(self, head: ListNode|None, k: int) -> ListNode|None:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Get the length of the list and link the tail to the head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Calculate the effective rotations needed
        k %= length
        if k == 0:
            return head

        # Step 3: Find the new tail: (length - k - 1)th node
        # and the new head: (length - k)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next if new_tail else None

        new_head = new_tail.next if new_tail else None

        # Step 4: Break the link to form the new list
        if new_tail:
            new_tail.next = None
        tail.next = head

        return new_head
