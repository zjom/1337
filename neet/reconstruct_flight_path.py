# https://neetcode.io/problems/reconstruct-flight-path

from icecream import ic
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph: defaultdict[str,list[str]] = defaultdict(list)
        for src,dst in sorted(tickets)[::-1]:
            graph[src].append(dst)

        res:list[str] = []
        def dfs(src:str):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)
            res.append(src)
        dfs("JFK")

        return res[::-1]

s = Solution()
tickets = [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
res = s.findItinerary(tickets)
ic(res)
assert res == ["JFK","BUF","HOU","SEA"]

tickets = [["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]
res = s.findItinerary(tickets)
ic(res)
assert res == ["JFK","HOU","JFK","SEA","JFK"]

tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
res = s.findItinerary(tickets)
ic(res)
assert res == ["JFK","NRT","JFK","KUL"]

