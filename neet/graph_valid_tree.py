# https://neetcode.io/problems/valid-tree

from icecream import ic
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # what is a valid tree?
        # no cycles, no isolated nodes
        # how to detect cycles?
        # build graph
        # try visit every node in graph once
        # if a node is not visited or is visited more than once, it is not valid

        if len(edges)>(n-1):
            return False

        adj:list[list[int]] = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen:set[int] = set()
        def dfs(node:int,parent:int):
            if node in seen:
                return False
            seen.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei,node)

        dfs(0,-1)
        return len(seen)==n

s = Solution()
assert ic(s.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))
assert not ic(s.validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
assert ic(s.validTree(5,[[0,1],[2,0],[3,0],[1,4]]))
assert ic(s.validTree(5,[[0,1],[1,3],[3,2],[1,4]]))

