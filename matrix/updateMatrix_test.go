package matrix

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type tcase struct {
	input    [][]int
	expected [][]int
}

func TestUpdateMatrix(t *testing.T) {
	tests := []tcase{
		{
			input:    [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}},
			expected: [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}},
		},
		{
			input:    [][]int{{0, 0, 0}, {0, 1, 0}, {1, 1, 1}},
			expected: [][]int{{0, 0, 0}, {0, 1, 0}, {1, 2, 1}},
		},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expected, updateMatrix(tc.input))
	}
}
