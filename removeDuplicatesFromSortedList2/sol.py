# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

class Solution:
    def deleteDuplicates(self, head: ListNode|None) -> ListNode|None:

        def aux(node: ListNode|None, prev_val:int) -> ListNode|None:
            # Base case: if the list is empty, return None
            if not node:
                return None
            # If current node is a duplicate (matches previous or next value), skip it
            if (node.next and node.val == node.next.val) or node.val == prev_val:
                # Skip the current node and continue with the next one
                return aux(node.next, node.val)
            else:
                # Current node is unique so far, include it in the result
                node.next = aux(node.next, node.val)
                return node
        return aux(head, -1001)
