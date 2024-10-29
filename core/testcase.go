package core

type TestCase[I any, E any] struct {
	Name     string
	Input    I
	Expected E
}
