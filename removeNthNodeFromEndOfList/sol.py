# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        # recursively traverse to end of list
        def aux(node: ListNode | None, i: int) -> tuple[ListNode | None, int]:
            if not node:
                return None, i
            
            next, length = aux(node.next, i+1)
            if length-i == n:
                return next, length
            
            node.next = next
            return node, length
            

        node, _ = aux(head, 0)
        return node
