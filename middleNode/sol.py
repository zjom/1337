# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
from typing import final
@final
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode|None) -> ListNode|None:
        def aux(node:ListNode|None, i:int) -> tuple[int,ListNode|None]:
            if not node:
                return i,None
            
            length,found = aux(node.next, i+1)
            if found:
                return length, found
            if i == length//2:
                return length, node
            
            return length, None

        _, found = aux(head,0)
        return found

