package validpalindrome

import "strings"

func isAlphaNumeric(c byte) bool {
	return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9')
}

func isPalindrome(s string) bool {
	if len(s) == 0 || len(s) == 1 {
		return true
	}

	a, b := s[0], s[len(s)-1]
	if !isAlphaNumeric(a) {
		return isPalindrome(s[1:])
	}

	if !isAlphaNumeric(b) {
		return isPalindrome(s[:len(s)-1])
	}

	if strings.ToLower(string(a)) != strings.ToLower(string(b)) {
		return false
	}

	return isPalindrome(s[1 : len(s)-1])
}
