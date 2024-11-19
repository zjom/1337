# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150
# pyright: basic
from collections import defaultdict, Counter


# == too slow ==
# class Solution:
#     def findSubstring(self, s: str, words: list[str]) -> list[int]:
#         wordLen = len(words[0])
#         wordDict = defaultdict[str,int](int)
#         for word in words:
#             wordDict[word] += 1
#
#         res: list[int] = []
#
#         for i in range(len(s)):
#             seen = defaultdict[str,int](int)
#             offset = 0
#             r = i+offset+wordLen
#             word = s[i+offset:r]
#             ic(word)
#             while r <= len(s) and \
#                 word in wordDict and \
#                 (word not in seen or \
#                 seen[word] < wordDict[word]):
#                 seen[word] += 1
#                 offset += wordLen
#                 r = i+offset+wordLen
#                 word = s[i+offset:r]
#
#                 ic(seen)
#
#                 if seen == wordDict:
#                     res.append(i)
#
#         return res



class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)
        wordDict = Counter(words)  # Counter for the frequency of words
        res = []

        # Iterate over each possible starting index within the word length range
        for i in range(wordLen):
            left = i
            seen = defaultdict(int)
            count = 0  # Number of valid words matched in current window

            for right in range(i, len(s) - wordLen + 1, wordLen):
                word = s[right:right + wordLen]

                if word in wordDict:
                    seen[word] += 1
                    count += 1

                    # If we have more occurrences than needed, slide the window
                    while seen[word] > wordDict[word]:
                        seen[s[left:left + wordLen]] -= 1
                        count -= 1
                        left += wordLen

                    # If the current window matches all words, record the starting index
                    if count == wordCount:
                        res.append(left)

                else:
                    # Reset the window if the word is not in wordDict
                    seen.clear()
                    count = 0
                    left = right + wordLen

        return res
