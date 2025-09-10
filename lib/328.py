from icecream import ic
# https://leetcode.com/problems/odd-even-linked-list

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
    def oddEvenList(self, head: ListNode|None) -> ListNode|None:
        if not head or not head.next:
            return head

        odd_cur:ListNode|None = head
        even_hd: ListNode|None = head.next
        even_cur: ListNode|None = head.next

        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            odd_cur = odd_cur.next

            even_cur.next = odd_cur.next
            even_cur = even_cur.next

        odd_cur.next = even_hd

        return head


s = Solution()
head = list_to_linked_list([1,2,3,4,5])
print(linked_list_to_list(head))
res = s.oddEvenList(head)
_ = ic(linked_list_to_list(res))
