package rottingoranges

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMain(t *testing.T) {
	grid := [][]int{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}
	expected := 4

	assert.Equal(t, expected, orangesRotting(grid))
}
