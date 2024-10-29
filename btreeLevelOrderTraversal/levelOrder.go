package btreelevelordertraversal

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	acc := make([][]int, 0)
	var recurse func(n *TreeNode, level int)
	recurse = func(n *TreeNode, level int) {
		if n == nil {
			return
		}

		if level > len(acc) {
			acc = append(acc, []int{})
		}
		acc[level-1] = append(acc[level-1], n.Val)
		recurse(n.Left, level+1)
		recurse(n.Right, level+1)
	}
	recurse(root, 1)
	return acc
}
