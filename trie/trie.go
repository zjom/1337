// https://leetcode.com/problems/implement-trie-prefix-tree/description/
package trie

type Trie struct {
	node *node
}

func Constructor() Trie {
	return Trie{newNode()}
}

func (this *Trie) Insert(word string) {
	insert(this.node, word)
}

func (this *Trie) Search(word string) bool {
	return search(this.node, word)
}

func (this *Trie) StartsWith(prefix string) bool {
	return startsWith(this.node, prefix)
}

type node struct {
	children map[byte]*node
	isWord   bool
}

func newNode() *node {
	return &node{
		children: make(map[byte]*node),
		isWord:   false,
	}
}

func insert(n *node, word string) {
	if len(word) == 0 {
		n.isWord = true
		return
	}

	next, ok := n.children[word[0]]
	if !ok {
		next = newNode()
		n.children[word[0]] = next
	}

	insert(next, word[1:])
}

func search(n *node, word string) bool {
	if len(word) == 0 {
		return n.isWord
	}

	next, ok := n.children[word[0]]
	if !ok {
		return false
	}

	return search(next, word[1:])
}

func startsWith(n *node, prefix string) bool {
	if len(prefix) == 0 {
		return true
	}

	next, ok := n.children[prefix[0]]
	if !ok {
		return false
	}

	return startsWith(next, prefix[1:])
}
