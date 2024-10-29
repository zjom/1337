package appendanddelete

func appendAndDelete(s string, t string, k int32) string {
	if k >= (int32(len(s)) + int32(len(t))) {
		return "Yes"
	}

	same := min(len(s), len(t))
	for i := 0; i < min(len(s), len(t)); i++ {
		if s[i] != t[i] {
			same = i
			break
		}
	}

	k = k - int32(len(s)-same)
	k = k - int32(len(t)-same)

	if k >= 0 && k%2 == 0 {
		return "Yes"
	}

	return "No"
}
