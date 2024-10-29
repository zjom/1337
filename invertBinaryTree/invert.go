package invertbinarytree

type node struct {
	val   int
	left  *node
	right *node
}

func invert(root *node) *node {
	if root == nil {
		return nil
	}

	tmp := root.left
	root.left = invert(root.right)
	root.right = invert(tmp)

	return root
}
