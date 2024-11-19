# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parens = {'(': ')', '{': '}', '[':']'}
        seen:list[str] = []

        for c in s:
            if c in parens:
                seen.append(parens[c])
            else:
                if len(seen)==0 or seen.pop() != c:
                    return False

        return len(seen) == 0
