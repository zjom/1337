# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val:int=0, next:'ListNode | None'=None):
        self.val:int = val
        self.next:ListNode|None = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        def reverse(node: ListNode | None) -> ListNode | None:
            # Base case: if node is None or it's the last node, return it
            if not node or not node.next:
                return node

            # Recursively reverse the rest of the list
            hd = reverse(node.next)

            # Set the next node's next pointer to the current node
            node.next.next = node
            # Set the current node's next pointer to None to prevent cycles
            node.next = None

            return hd

        return reverse(head)
