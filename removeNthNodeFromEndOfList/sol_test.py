from sol import ListNode, Solution


def test_sol():
    ls = ListNode(1,ListNode(2,ListNode(3, ListNode(4,ListNode(5)))))
    expected = ListNode(1,ListNode(2,ListNode(3, ListNode(5))))
    got = Solution().removeNthFromEnd(ls, 2) 
    curr_e = expected
    curr_g = got
    while curr_e:
        assert curr_g is not None
        assert curr_e.val == curr_g.val
        curr_g = curr_g.next
        curr_e = curr_e.next

