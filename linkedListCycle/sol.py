# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x:int):
        self.val:int = x
        self.next:ListNode | None = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next if slow else None

            if fast == slow:
                return True

        return False
