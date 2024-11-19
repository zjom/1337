# https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def partition(self, head: ListNode|None, x: int) -> ListNode|None:
        if not head or not head.next:
            return head
        before = ListNode() # all values before x, to be mutated
        before_head = before # head of result
        after = ListNode() # all values after or equal to x, to be mutated
        after_head = after # head of after
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            tmp = curr
            curr = curr.next
            tmp.next = None

        before.next = after_head.next
        return before_head.next
