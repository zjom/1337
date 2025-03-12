# https://leetcode.com/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150

class WordDictionary:
    def __init__(self):
        self.data:list[WordDictionary|None] = [None]*26
        self.isWord:bool = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.isWord = True
            return
        idx = ord(word[0]) - ord('a')
        if not self.data[idx]:
            self.data[idx] = WordDictionary()
        self.data[idx].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.isWord
        c = word[0]
        if c == ".":
            for data in self.data:
                if data and data.search(word[1:]):
                    return True
            return False

        idx = ord(c) - ord('a')
        if not self.data[idx]:
            return False
        return self.data[idx].search(word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
