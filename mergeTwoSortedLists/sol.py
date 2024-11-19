# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int=0, next:None=None):
        self.val:int = val
        self.next: ListNode | None = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1

        hd = ListNode()
        curr = hd
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1

        if list2:
            curr.next = list2
        return hd.next
