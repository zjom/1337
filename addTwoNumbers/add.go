// https://leetcode.com/problems/add-two-numbers/description/
package addtwonumbers

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers() {
	fmt.Printf("Hello %d", 1)
	l1 := &ListNode{
		Next: &ListNode{
			Next: &ListNode{
				Next: &ListNode{
					Next: &ListNode{},
				},
			},
		},
	}
}
