package appendanddelete

import (
	"testing"
)

type input struct {
	s string
	t string
	k int32
}

type testCase struct {
	inp input
	exp string
}

func TestSol(t *testing.T) {
	cases := []testCase{
		{
			inp: input{
				s: "aba",
				t: "aba",
				k: 7,
			},
			exp: "Yes",
		},
		{
			inp: input{
				s: "hackerhappy",
				t: "hackerrank",
				k: 9,
			},
			exp: "Yes",
		},
		{
			inp: input{
				s: "ashley",
				t: "ash",
				k: 2,
			},
			exp: "No",
		},
		{
			inp: input{
				s: "qwerasdf",
				t: "qwerbsdf",
				k: 6,
			},
			exp: "No",
		},
		{
			inp: input{
				s: "y",
				t: "yu",
				k: 2,
			},
			exp: "No",
		},
	}

	for i, c := range cases {
		res := appendAndDelete(c.inp.s, c.inp.t, c.inp.k)
		if res != c.exp {
			t.Errorf("test %d failed: expected %s, got %s", i, c.exp, res)
		}
	}
}
