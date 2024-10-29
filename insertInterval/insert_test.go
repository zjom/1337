package insertinterval

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type input struct {
	intvs   [][]int
	newIntv []int
}
type tcase struct {
	input    input
	expected [][]int
}

func TestMain(t *testing.T) {
	tests := []tcase{
		{
			input: input{
				intvs:   [][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}},
				newIntv: []int{4, 8},
			},
			expected: [][]int{{1, 2}, {3, 10}, {12, 16}},
		},
		{
			input: input{
				intvs:   [][]int{{1, 3}, {6, 9}},
				newIntv: []int{2, 5},
			},
			expected: [][]int{{1, 5}, {6, 9}},
		},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expected, insert(tc.input.intvs, tc.input.newIntv))
	}
}
