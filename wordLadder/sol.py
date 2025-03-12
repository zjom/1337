# https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque([beginWord])
        visited = set([beginWord])
        moves = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return moves
                
                word_arr = list(word)
                for idx,orig in enumerate(word_arr):
                    for c in ascii_lowercase:
                        word_arr[idx] = c
                        word_str = ''.join(word_arr)
                        if word_str in word_set and word_str not in visited:
                            q.append(word_str)
                            visited.add(word_str)

                    word_arr[idx] = orig
            moves += 1

        return 0
