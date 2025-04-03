# https://neetcode.io/problems/count-connected-components

from icecream import ic
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj:list[list[int]] = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        seen:set[int] = set()
        def dfs(cur:int,prev:int):
            nonlocal count
            if cur in seen:
                return False
            seen.add(cur)
            for nei in adj[cur]:
                if nei == prev:
                    continue
                dfs(nei,cur)
            return True

        for node in range(n):
            if dfs(node,-1):
                count+=1

        return count


s = Solution()
n=3
edges=[[0,1], [0,2]]
ic(s.countComponents(n,edges))


n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
ic(s.countComponents(n,edges))
