package core

type TC[I any, E any] struct {
	Name     string
	Input    I
	Expected E
}
