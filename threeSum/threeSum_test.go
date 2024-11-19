package threesum

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/core"
)

func TestMain(t *testing.T) {
	tests := []core.TC[[]int, [][]int]{{
		Input:    []int{-1, 0, 1, 2, -1, -4},
		Expected: [][]int{{-1, -1, 2}, {-1, 0, 1}},
	}}

	for _, tc := range tests {
		assert.Equal(t, tc.Expected, threeSum(tc.Input))
	}
}
