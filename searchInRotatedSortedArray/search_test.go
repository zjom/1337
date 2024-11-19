package searchinrotatedsortedarray

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMain(t *testing.T) {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	target := 0
	expected := 4
	assert.Equal(t, expected, search(nums, target))

	nums = []int{4, 5, 6, 7, 8, 1, 2, 3}
	target = 8
	expected = 4
	assert.Equal(t, expected, search(nums, target))
}
