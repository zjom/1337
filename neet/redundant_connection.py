# https://neetcode.io/problems/redundant-connection

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1]*(N+1)

        def find(n: int)->int:
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1:int,n2:int)->bool:
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+= rank[p1]

            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        return []
