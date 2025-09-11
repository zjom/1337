# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
class ListNode:
    def __init__(self, val:int=0, next:'ListNode|None'=None):
        self.val:int = val
        self.next:ListNode|None = next
class Solution:
    def pairSum(self, head: ListNode|None) -> int:
        if not head:
            return 0

        stack:list[int] = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next


        maximum = -2**31+1
        for i in range(len(stack)//2):
            maximum = max(maximum,stack[i]+stack[len(stack)-1-i])

        return maximum
