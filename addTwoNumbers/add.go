// https://leetcode.com/problems/add-two-numbers/description/
package addtwonumbers

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	cur := dummy

	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		var (
			v1 int
			v2 int
		)
		if l1 != nil {
			v1 = l1.Val
		}
		if l2 != nil {
			v2 = l2.Val
		}

		val := v1 + v2 + carry

		carry = val / 10
		val = val % 10

		cur.Next = &ListNode{Val: val}
		cur = cur.Next
		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	return dummy.Next
}
