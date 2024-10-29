package validparentheses

func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}
	pairs := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}

	stack := make([]rune, 0)
	for _, c := range s {
		p, ok := pairs[c]
		if ok {
			stack = append(stack, p)
			continue
		}

		if len(stack) == 0 {
			return false
		}

		last := stack[len(stack)-1]
		if last == c {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}

	}

	return len(stack) == 0
}
