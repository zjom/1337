# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compute(s: str)->str:
            retv:list[str] = []
            for c in s:
                if c == "#":
                    if retv:
                        _=retv.pop()
                else:
                    retv.append(c)
            return ''.join(retv)
        ss = compute(s) 
        tt = compute(t)

        return ss==tt
