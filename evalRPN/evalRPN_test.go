package evalrpn

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/core"
)

func TestMain(t *testing.T) {
	tests := []core.TestCase[[]string, int]{
		{
			Input:    []string{"2", "1", "+", "3", "*"},
			Expected: 9,
		},
		{
			Input:    []string{"4", "13", "5", "/", "+"},
			Expected: 6,
		},
		{
			Input:    []string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"},
			Expected: 22,
		},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.Expected, evalRPN(tc.Input))
	}
}
