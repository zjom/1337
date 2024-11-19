# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        m: dict[str,list[str]] = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in m:
                m[sorted_s].append(s)
            else:
                m[sorted_s] = [s]

        return list(m.values())
