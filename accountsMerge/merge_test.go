package accountsmerge

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/core"
)

func TestMerge(t *testing.T) {
	tests := []core.TC[[][]string, [][]string]{
		{
			Name: "base 1",
			Input: [][]string{
				{"John", "johnsmith@mail.com", "john_newyork@mail.com"},
				{"John", "johnsmith@mail.com", "john00@mail.com"},
				{"Mary", "mary@mail.com"},
				{"John", "johnnybravo@mail.com"},
			},
			Expected: [][]string{
				{"John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"},
				{"Mary", "mary@mail.com"},
				{"John", "johnnybravo@mail.com"},
			},
		},
		{
			Name: "base 2",

			Input: [][]string{
				{"Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"},
				{"Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"},
				{"Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"},
				{"Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"},
				{"Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"},
			},

			Expected: [][]string{
				{"Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"},
				{"Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"},
				{"Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"},
				{"Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"},
				{"Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"},
			},
		},
		{
			Name: "merge all into one",
			Input: [][]string{
				{"David", "David0@m.co", "David1@m.co"},
				{"David", "David3@m.co", "David4@m.co"},
				{"David", "David4@m.co", "David5@m.co"},
				{"David", "David2@m.co", "David3@m.co"},
				{"David", "David1@m.co", "David2@m.co"},
			},
			Expected: [][]string{
				{
					"David",
					"David0@m.co",
					"David1@m.co",
					"David2@m.co",
					"David3@m.co",
					"David4@m.co",
					"David5@m.co",
				},
			},
		},
	}

	for _, tc := range tests {
		assert.EqualValues(t, tc.Expected, accountsMerge(tc.Input))
	}

}
