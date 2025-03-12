# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        freqS,freqP = [0]*26,[0]*26
        res:list[int] = []

        for i in range(len(p)):
            freqS[ord(s[i])-ord('a')] += 1
            freqP[ord(p[i])-ord('a')] += 1

        if freqS == freqP:
            res.append(0)

        start,end = 0,len(p)
        while end < len(s):
            freqS[ord(s[start])-ord('a')] -= 1
            freqS[ord(s[end])-ord('a')] += 1

            if freqS == freqP:
                res.append(start + 1)

            end += 1
            start += 1
        return res
