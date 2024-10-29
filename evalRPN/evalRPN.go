// https://leetcode.com/problems/evaluate-reverse-polish-notation/
package evalrpn

import "strconv"

func pop(stack []int) ([]int, int) {
	return stack[:len(stack)-1], stack[len(stack)-1]
}

func evalRPN(tokens []string) int {
	operations := map[string]func(a, b int) int{
		"*": func(a, b int) int { return a * b },
		"/": func(a, b int) int { return a / b },
		"-": func(a, b int) int { return a - b },
		"+": func(a, b int) int { return a + b },
	}

	stack := make([]int, 0)
	for _, tok := range tokens {
		n, err := strconv.Atoi(tok)
		if err != nil {
			// we have a operand
			op := operations[tok]
			var a, b int
			stack, b = pop(stack)
			stack, a = pop(stack)
			stack = append(stack, op(a, b))
			continue
		}

		stack = append(stack, n)
	}

	return stack[0]
}
