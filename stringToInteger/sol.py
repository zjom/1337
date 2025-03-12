# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        isNeg = False

        def aux(s:str, acc:int)->int:
            if not s:
                return acc
            hd,tl = s[0],s[1:]
            if not hd.isdigit():
                return acc
            acc = acc * 10 + int(hd)
            return aux(tl, acc)
    
        s = s.strip()
        if not s:
            return 0
        hd,tl = s[0],s[1:]
        if hd == '+':
            isNeg = False
        elif hd == '-':
            isNeg = True
        else:
            tl = s
    
        n = aux(tl, 0)
        n = -1*n if isNeg else n
        if n >= 2**31-1:
            return 2**31-1
        if n <= -(2**31):
            return -(2**31)
        return n
