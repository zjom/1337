# https://leetcode.com/problems/word-break/description/

class Trie:
    def __init__(self):
        self.isWord:bool = False
        self.data:list[Trie|None] = [None]*26

    def insert(self, word:str)->None:
        if not word:
            self.isWord = True
            return
        c = word[0]
        idx = ord(c) - ord('a')
        if not self.data[idx]:
            self.data[idx] = Trie()
        return self.data[idx].insert(word[1:])


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        seen:dict[int,bool] = dict()
        def dfs(start: int)->bool:
            if start == len(s):
                return True
            
            if start in seen:
                return seen[start]

            node = trie
            for end in range(start, len(s)):
                c = ord(s[end]) - ord('a')
                if not node.data[c]:
                    break
                node = node.data[c]
                if node.isWord and dfs(end+1):
                    seen[start] = True
                    return True

            seen[start] = False
            return False

        return dfs(0)
