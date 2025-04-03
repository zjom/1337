# https://neetcode.io/problems/merge-k-sorted-linked-lists

from heapq import heappop, heappush
from typing import override
from icecream import ic


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next

    @override
    def __str__(self) -> str:
        return f"ListNode(val={self.val},next={self.next})" 


class Solution:    
    def mergeKLists(self, lists: list[ListNode|None]) -> ListNode|None:
        heap:list[int] = []
        def aux(node:ListNode|None):
            while node:
                heappush(heap,node.val)
                node = node.next

        for node in lists:
            aux(node)

        dummy = cur = ListNode()
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next
        return dummy.next


s = Solution()
def test(lists:list[list[int]], expected:list[int]):
    input:list[ListNode|None] = []
    for lst in lists:
        hd = cur = ListNode()
        for n in lst:
            cur.next = ListNode(n)
            cur = cur.next
        input.append(hd)
    res = s.mergeKLists(input)
    actual:list[int] = []
    while res:
        actual.append(res.val)
        res = res.next

    ic(actual)
    assert actual == expected

lists=[[1,2,4],[1,3,5],[3,6]]
expected = [1,1,2,3,3,4,5,6]
test(lists,expected)
