# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([c for c in s.split(" ") if c != ""]))
