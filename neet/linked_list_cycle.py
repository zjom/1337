'''
https://neetcode.io/problems/linked-list-cycle-detection
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def hasCycle(self, head: ListNode|None) -> bool:
        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True

        return False
