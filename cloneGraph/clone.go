package clonegraph

type Node struct {
	Val       int
	Neighbors []*Node
}

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}

	var clone func(*Node, map[*Node]*Node) *Node
	clone = func(orig *Node, v map[*Node]*Node) *Node {
		if n, found := v[orig]; found {
			return n
		}

		cloned := &Node{Val: orig.Val}
		v[orig] = cloned

		for _, neighbor := range orig.Neighbors {
			cloned.Neighbors = append(cloned.Neighbors, clone(neighbor, v))
		}

		return cloned
	}

	return clone(node, make(map[*Node]*Node))
}
