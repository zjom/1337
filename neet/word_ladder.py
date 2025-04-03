# https://neetcode.io/problems/word-ladder

from icecream import ic
from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        nei:defaultdict[str,list[str]] = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        seen = set([beginWord])
        queue = deque([beginWord])
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for w in nei[pattern]:
                        if w not in seen:
                            queue.append(w)
                            seen.add(w)
            res+=1

        return 0



beginWord = "cat"
endWord = "sag"
wordList = ["bat",
            "bag",
            "sag",
            "dag",
            "dot"]
s = Solution()
res = s.ladderLength(beginWord,endWord,wordList)
ic(res)
