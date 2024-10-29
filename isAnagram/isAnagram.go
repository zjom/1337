package isanagram

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	m := make(map[rune]int, len(s))

	for _, c := range s {
		if _, ok := m[c]; ok {
			m[c] = m[c] + 1
			continue
		}
		m[c] = 1
	}

	for _, c := range t {
		if _, ok := m[c]; !ok {
			return false
		}

		m[c] = m[c] - 1
	}

	for _, v := range m {
		if v != 0 {
			return false
		}
	}

	return true
}
