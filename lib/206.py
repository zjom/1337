# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

def list_to_linked_list(els: list[int])->ListNode|None:
    if not els:
        return None
    dummy = ListNode()
    cur = dummy
    for el in els:
        cur.next = ListNode(el)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head: ListNode|None)->list[int]:
    acc:list[int] = []
    cur = head
    while cur:
        acc.append(cur.val)
        cur = cur.next

    return acc

class Solution:
    def reverseList(self, head: ListNode|None) -> ListNode|None:
        if not head:
            return None
        prev = None
        cur = head
        next = cur.next

        while next:
            cur.next = prev
            prev = cur
            cur = next
            next = cur.next
        cur.next = prev
        return cur



s = Solution()
print(linked_list_to_list(s.reverseList(list_to_linked_list([1,2,3,4,5]))))
