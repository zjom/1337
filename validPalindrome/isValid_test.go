package validpalindrome

import "testing"

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{
			input:    "A man, a plan, a canal: Panama",
			expected: true,
		},
		{
			input:    "race a car",
			expected: false,
		},
		{
			input:    "0P",
			expected: false,
		},
	}

	for i, c := range tests {
		got := isPalindrome(c.input)
		if got != c.expected {
			t.Errorf("test %d failed. got: %t, expected: %t", i, got, c.expected)
		}
	}
}
