package longestsubstringwithoutrepeat

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type tcase struct {
	input    string
	expected int
}

func TestMain(t *testing.T) {
	tests := []tcase{
		{
			"abcabcbb",
			3,
		},
		{
			"bbbbb",
			1,
		},
		{
			"pwwkew",
			3,
		},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expected, lengthOfLongestSubstring(tc.input))
	}
}
