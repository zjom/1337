package coinchange

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/core"
)

func TestMain(t *testing.T) {
	tests := []core.TC[struct {
		coins  []int
		amount int
	}, int]{
		{
			Name: "example 1",
			Input: struct {
				coins  []int
				amount int
			}{
				coins:  []int{1, 2, 5},
				amount: 11,
			},
			Expected: 3,
		},
		{
			Name: "example 2",
			Input: struct {
				coins  []int
				amount int
			}{
				coins:  []int{2},
				amount: 3,
			},
			Expected: -1,
		},
		{
			Name: "example 3",
			Input: struct {
				coins  []int
				amount int
			}{
				coins:  []int{1},
				amount: 0,
			},
			Expected: 0,
		},
		{
			Name: "example 4",
			Input: struct {
				coins  []int
				amount int
			}{
				coins:  []int{186, 419, 83, 408},
				amount: 6249,
			},
			Expected: 20,
		},
	}

	for _, tt := range tests {
		assert.Equal(t, tt.Expected, coinChange(tt.Input.coins, tt.Input.amount))
	}
}
