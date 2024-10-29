package maximumsubarray

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMain(t *testing.T) {
	input := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	expected := 6

	got := maxSubArray(input)
	assert.Equalf(t, expected, got, "expected: %v, got %v", expected, got)
}
