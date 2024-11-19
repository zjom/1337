package maxmovesingrid

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMain(t *testing.T) {
	grid := [][]int{{2, 4, 3, 5}, {5, 4, 9, 3}, {3, 4, 2, 11}, {10, 9, 13, 15}}
	output := 3
	assert.Equal(t, output, maxMoves(grid))

	grid = [][]int{{3, 2, 4}, {2, 1, 9}, {1, 1, 7}}
	output = 0
	assert.Equal(t, output, maxMoves(grid))
}
