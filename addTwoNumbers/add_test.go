package addtwonumbers

import (
	"testing"

	"github.com/zjom/1337/core"
)

func TestAdd(t *testing.T) {
	tests := []core.TC[[]*ListNode, *ListNode]{
		{Name: "1",
			Input: []*ListNode{
				{
					Val: 2,
					Next: &ListNode{
						Val: 4,
						Next: &ListNode{
							Val:  3,
							Next: &ListNode{},
						},
					},
				},
				{
					Val: 5,
					Next: &ListNode{
						Val: 6,
						Next: &ListNode{
							Val:  4,
							Next: &ListNode{},
						},
					},
				},
			},
			Expected: &ListNode{
				Val: 7,
				Next: &ListNode{
					Val: 0,
					Next: &ListNode{
						Val:  8,
						Next: &ListNode{},
					},
				},
			}},
	}

	for _, tc := range tests {
		t.Log(addTwoNumbers(tc.Input[0], tc.Input[1]))
	}
}
