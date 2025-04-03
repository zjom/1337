# Remove Node From End of Linked List
# https://neetcode.io/problems/remove-node-from-end-of-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:'ListNode|None' = next

class Solution:
    def removeNthFromEnd(self, head: ListNode|None, n: int) -> ListNode|None:
        def aux(node: ListNode|None,acc:int)->tuple[ListNode|None,int]:
            if not node:
                return None,acc
            next,length = aux(node.next,acc+1)
            if length-acc==n:
                return next,length

            node.next = next
            return node,length
        node, _ = aux(head,0)
        return node
