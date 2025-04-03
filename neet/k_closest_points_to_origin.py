# https://neetcode.io/problems/k-closest-points-to-origin

from math import sqrt

from icecream import ic

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap:list[tuple[float,list[int]]] = [(sqrt(x**2+y**2), [x,y]) for x,y in points]
        heap.sort()
        ic(heap)
        return [x[1] for x in heap[:k+1]]


s = Solution()
points=[[3,3],[5,-1],[-2,4]]
k=2
s.kClosest(points,k)
