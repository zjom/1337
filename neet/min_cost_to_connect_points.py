'''
[Min Cost to Connect Points - NeetCode](https://neetcode.io/problems/min-cost-to-connect-points)

You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:

Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10

Constraints:

    1 <= points.length <= 1000
    -1000 <= xi, yi <= 1000
'''


#+REVIEW
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N,node = len(points),0
        dist = [2**31]*N
        visit = [False]*N
        edges,res = 0,0

        while edges < N-1:
            visit[node] = True
            next_node = -1
            for i in range(N):
                if visit[i]:
                    continue
                cur_dist = abs(points[node][0]-points[i][0])+abs(points[node][1]-points[i][1])
                dist[i]= min(dist[i],cur_dist)
                if next_node == -1 or dist[i]<dist[next_node]:
                    next_node = i
            res+=dist[next_node]
            node = next_node
            edges+=1
        return res
