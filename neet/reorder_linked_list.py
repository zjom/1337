'''
https://neetcode.io/problems/reorder-linked-list
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]

Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]

Constraints:
    1 <= Length of the list <= 1000.
    1 <= Node.val <= 1000



0 -> N -> 1 -> N-1

0 -> 1 -> 2 -> ... N // 2
N -> N-1 -> N-2 -> ... N//2+1

left = 0,1
right = N,N-1

next_right = right.next
next_left = 1,2

left.next = right
right.next = next_left

left = next_left
right = next_right
'''

# Definition for singly-linked list.
from typing import Callable, override

class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

    @override
    def __str__(self) -> str:
        return f"ListNode<val: {self.val}, next: {self.next}>"

    @override
    def __repr__(self) -> str:
        return self.__str__()

    def traverse(self, callback: Callable[['ListNode'], None])->None:
        callback(self)
        if self.next:
            self.next.traverse(callback)

def from_list(xs: list[int])->ListNode|None:
    if not xs:
        return None
    dummy = cur = ListNode()
    for x in xs:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def collect(node: ListNode|None)->list[int]:
    if not node:
        return []

    xs:list[int] = []
    node.traverse(lambda n : xs.append(n.val))

    return xs


def reverse(head: ListNode|None)->ListNode|None:
    if not head:
        return None
    dummy = ListNode()
    def aux(node:ListNode)->ListNode:
        if not node.next:
            dummy.next = node
            return node
        nxt = aux(node.next)
        nxt.next = node
        node.next = None
        return node
    aux(head)
    return dummy.next

class Solution:
    def reorderList(self, head: ListNode|None) -> None:
        dummy_right:ListNode = ListNode()

        def reverse_second_half(node:ListNode, n: int) -> tuple[ListNode, int]:
            if node.next is None:
                dummy_right.next = node
                return node,n

            nxt, length = reverse_second_half(node.next, n+1)
            if n > length//2:
                nxt.next = node
                node.next = None
                return node, length
            if n == length//2:
                node.next = None
            return nxt, length

        if not head:
            return
        reverse_second_half(head,0)

        left:ListNode|None = head
        right:ListNode|None = dummy_right.next
        while left is not None and right is not None:
            left_nxt = left.next
            right_nxt = right.next

            left.next = right
            right.next = left_nxt

            left = left_nxt
            right = right_nxt



s = Solution()
head = from_list([2,4,6,8])
s.reorderList(head)
assert collect(head) == [2,8,4,6]


head = from_list([2,4,6,8,10])
s.reorderList(head)
assert collect(head) == [2,10,4,8,6]
