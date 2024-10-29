package sort

import (
	"slices"
	"testing"
)

func TestSort(t *testing.T) {
	testCases := [][]int{
		{1, 2, 3, 4, 5},
		{5, 4, 2, 12, 4, 5},
		{10, 24, 25, 191919},
		{0},
		{10000, 1},
	}

	for i, c := range testCases {
		got, expected := slices.Clone(c), slices.Clone(c)
		quickSort(got, 0, len(got)-1)
		slices.Sort(expected)

		if slices.Compare(got, expected) != 0 {
			t.Errorf("test %d failed, got: %v, expected: %v", i, got, expected)
		}
	}
}
