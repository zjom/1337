# https://neetcode.io/problems/search-for-word-ii

from typing import Any

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Trie to optimize word search
        trie: dict[str, Any] = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word
        
        m, n = len(board), len(board[0])
        res: list[str] = []
        
        def dfs(x: int, y: int, node: dict[str, Any]) -> None:
            # Base case: out of board or character not found
            if (x < 0 or x >= m or y < 0 or y >= n or 
                board[x][y] not in node):
                return
            
            # Current character
            char: str = board[x][y]
            curr_node: dict[str, Any] = node[char]
            
            # Check if we found a complete word
            if '#' in curr_node:
                res.append(curr_node['#'])
                del curr_node['#']  # Prevent duplicate
            
            # Mark as visited
            board[x][y] = '#'
            
            # Explore all 4 directions
            directions: list[tuple[int, int]] = [(0,1), (1,0), (-1,0), (0,-1)]
            for dx, dy in directions:
                dfs(x+dx, y+dy, curr_node)
            
            # Restore the original character
            board[x][y] = char
        
        # Start DFS from each cell
        for x in range(m):
            for y in range(n):
                dfs(x, y, trie)
        
        return res

s = Solution()
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
res = s.findWords(board,words)
assert sorted(res) == sorted(["cat","back","backend"])


board = [
  ["x","o"],
  ["x","o"]
]
words = ["xoxo"]

res = s.findWords(board,words)
assert sorted(res) == sorted([])


board=[["o","a","a","n"],
       ["e","t","a","e"],
       ["i","h","k","r"],
       ["i","f","l","v"]]
words=["oath","pea","eat","rain"]
res = s.findWords(board,words)
assert sorted(res) == sorted(["eat","oath"])


board=[["a"]]
words=["a"]
res = s.findWords(board,words)
print(res)
assert sorted(res) == sorted(["a"])
