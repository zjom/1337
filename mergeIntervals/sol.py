# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def shouldMerge(a: list[int], b: list[int]) -> bool:
            return True if a[1] >= b[0] else False

        def mergeTwo(a: list[int], b: list[int]) -> list[int]:
            return [min(a[0],b[0]), max(a[1],b[1])]

        def conns(arr: list[list[int]]) -> tuple[list[int], list[list[int]]]:
            return arr[0], arr[1:]

        def aux(curr: list[int], intervals: list[list[int]]) -> list[list[int]]:
            if len(intervals) == 0:
                return [curr]
            hd,tl = conns(intervals)
            if shouldMerge(curr,hd):
                return aux(mergeTwo(curr,hd), tl)
            res = [curr]
            res.extend(aux(hd,tl))
            return res

        if len(intervals) == 0:
            return []
        intervals.sort()
        hd,tl = conns(intervals)
        return aux(hd,tl)
