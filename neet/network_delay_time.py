# https://neetcode.io/problems/network-delay-time

from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges:defaultdict[int,list[tuple[int,int]]] = defaultdict(list)
        for src,dst,weight in times:
            edges[src].append((dst,weight))
        
        seen:set[int] = set()
        t = 0
        q = [(0,k)] # weight first so sort by weight
        while q:
            w,src = heappop(q)
            if src in seen:
                continue
            seen.add(src)
            t = w
            for dst,weight in edges[src]:
                if dst not in seen:
                    heappush(q, (weight+w,dst))

        return t if len(seen) == n else -1
