#pyright:basic
from icecream import ic
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m1,m2 = {},{}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in m1:
                m1[pattern[i]] = words[i]
            if words[i] not in m2:
                m2[words[i]] = pattern[i]

            ic(m1,m2)

            if m1[pattern[i]] != words[i] or m2[words[i]] != pattern[i]:
                return False

        return True

