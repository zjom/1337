# https://leetcode.com/problems/minimum-height-trees/description/
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if not edges:
            return [0]
        adj: dict[int,list[int]] = {i:[] for i in range(n+1)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        leaves:deque[int] = deque()
        edge_cnt = {}
        for src, neighbours in adj.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbours)


        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        return [0]
