// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
package longestsubstringwithoutrepeat

func lengthOfLongestSubstring(s string) int {
	l, res := 0, 0
	seen := make(map[byte]struct{})

	for r := 0; r < len(s); r++ {
		for _, ok := seen[s[r]]; ok; _, ok = seen[s[r]] {
			delete(seen, s[l])
			l++
		}
		seen[s[r]] = struct{}{}
		if res < r-l+1 {
			res = r - l + 1
		}
	}

	return res
}
