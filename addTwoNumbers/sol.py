# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

class ListNode:
    def __init__(self, val:int=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        hd = ListNode()
        curr = hd
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val > 9:
                val = val - 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val + carry
            if val > 9:
                val = val - 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            val = l2.val + carry
            if val > 9:
                val = val - 10
                carry = 1
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)
        return hd.next
