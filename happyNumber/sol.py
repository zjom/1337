# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isHappy(self, n: int) -> bool:
        seen: dict[int,int] = {}

        def aux(n: int) -> bool:
            if n == 1:
                return True
            if n == 2:
                return False
            
            if n in seen:
                return False

            next = 0
            for c in str(n):
                next += int(c)**2
            seen[n] = next
            return aux(next)
        
        return aux(n)
