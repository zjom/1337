package trie_test

import (
	"github.com/stretchr/testify/assert"
	"github.com/zjom/1337/trie"
	"testing"
)

func TestTrie_InsertAndSearch(t *testing.T) {
	tests := []struct {
		name     string
		words    []string
		search   string
		expected bool
	}{
		{"Search existing word", []string{"apple"}, "apple", true},
		{"Search non-existing word", []string{"apple"}, "app", false},
		{"Search after inserting prefix", []string{"apple", "app"}, "app", true},
		{"Search different word", []string{"banana"}, "banana", true},
		{"Search partial prefix", []string{"banana"}, "ba", false},
		{"Empty Trie search", []string{}, "a", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tr := trie.Constructor()
			for _, word := range tt.words {
				tr.Insert(word)
			}
			assert.Equal(t, tt.expected, tr.Search(tt.search))
		})
	}
}

func TestTrie_StartsWith(t *testing.T) {
	tests := []struct {
		name     string
		words    []string
		prefix   string
		expected bool
	}{
		{"Prefix exists", []string{"apple"}, "app", true},
		{"Prefix does not exist", []string{"banana"}, "ba", true},
		{"Non-existing prefix", []string{"apple"}, "ban", false},
		{"Exact word as prefix", []string{"banana"}, "banana", true},
		{"Prefix with no insertions", []string{}, "a", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tr := trie.Constructor()
			for _, word := range tt.words {
				tr.Insert(word)
			}
			assert.Equal(t, tt.expected, tr.StartsWith(tt.prefix))
		})
	}
}

func TestTrie_ComplexCases(t *testing.T) {
	tr := trie.Constructor()
	words := []string{"app", "apple", "beer", "add", "jam", "rental"}
	for _, word := range words {
		tr.Insert(word)
	}

	searchTests := []struct {
		search   string
		expected bool
	}{
		{"apps", false},
		{"app", true},
		{"ad", false},
		{"applepie", false},
		{"rest", false},
		{"jan", false},
		{"rent", false},
		{"beer", true},
		{"jam", true},
	}

	for _, tt := range searchTests {
		assert.Equal(t, tt.expected, tr.Search(tt.search), "Search test failed for: %s", tt.search)
	}

	startsWithTests := []struct {
		prefix   string
		expected bool
	}{
		{"app", true},
		{"ad", true},
		{"applepie", false},
		{"rest", false},
		{"jan", false},
		{"rent", true},
		{"beer", true},
		{"jam", true},
	}

	for _, tt := range startsWithTests {
		assert.Equal(t, tt.expected, tr.StartsWith(tt.prefix), "StartsWith test failed for: %s", tt.prefix)
	}
}
