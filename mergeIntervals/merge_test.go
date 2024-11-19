package mergeintervals

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/core"
)

func TestMain(t *testing.T) {
	tests := []core.TC[[][]int, [][]int]{
		{
			Name:     "1",
			Input:    [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}},
			Expected: [][]int{{1, 6}, {8, 10}, {15, 18}},
		},

		{
			Name:     "2",
			Input:    [][]int{{1, 4}, {4, 5}},
			Expected: [][]int{{1, 5}},
		},

		{
			Name:     "3",
			Input:    [][]int{{1, 4}, {0, 4}},
			Expected: [][]int{{0, 4}},
		},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.Expected, merge(tc.Input))
	}
}
