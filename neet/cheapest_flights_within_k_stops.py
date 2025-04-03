# https://neetcode.io/problems/cheapest-flight-path

from collections import defaultdict
from heapq import heappush
from icecream import ic

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges:defaultdict[int,list[list[int]]] = defaultdict(list)
        for frm,to,cost in flights:
            heappush(edges[frm],[cost,to])

        def dfs(cur:int,cost:int,stops:int)->int:
            if stops > k:
                return -1
            if cur == dst:
                return cost
            min_cost = 2**31-1
            for cst,to in edges[cur]:
                sum_cost = dfs(to,cost+cst,stops+1)
                if sum_cost == -1:
                    continue
                min_cost = min(min_cost,sum_cost)

            return min_cost

        min_cost = 2**31-1
        for cost,to in edges[src]:
            sum_cost = dfs(to,cost,0)
            if sum_cost == -1:
                continue
            min_cost = min(min_cost,sum_cost)

        return min_cost if min_cost != 2**31-1 else -1


s = Solution()
assert ic(s.findCheapestPrice(n=4,flights=[[0,1,200],[1,2,100],[1,3,300],[2,3,100]],src=0,dst=3,k=1)) == 500

assert ic(s.findCheapestPrice(n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1)) == 200

n=3
flights=[[0,1,100],[1,2,100],[0,2,500]]
src=0
dst=2
k=1

ic(s.findCheapestPrice(n,flights,src,dst,k))
