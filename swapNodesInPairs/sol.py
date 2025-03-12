# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def swapPairs(self, head: ListNode|None) -> ListNode|None:
        dummy = ListNode(0,head)
        prev,cur = dummy,head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = npn
            prev.next = second

            prev = cur
            cur = npn

        return dummy.next
