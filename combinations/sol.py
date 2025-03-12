# https://leetcode.com/problems/combinations/?envType=study-plan-v2&envId=top-interview-150
class Solution:

    def combine(self, n: int, k: int) -> list[list[int]]:
        res:list[list[int]] = []
        acc:list[int] = []
        def aux(i:int):
            if len(acc) == k:
                res.append(acc[:])
                return
            for j in range(i,n+1):
                acc.append(j)
                aux(j+1)
                _ = acc.pop()
            return

        aux(1)
        return res
