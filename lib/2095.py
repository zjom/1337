
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def deleteMiddle(self, head: ListNode|None) -> ListNode|None:
        def aux(node: ListNode | None, idx: int=0) -> tuple[ListNode | None, int]:
            if not node:
                return None, idx
            next_node, length = aux(node.next, idx+1)
            if idx == int(length/2):
                return next_node, length
            node.next = next_node
            return node, length

        node, _ = aux(head)

        return node
