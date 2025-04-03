# https://neetcode.io/problems/course-schedule-ii

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indeg = [0]*numCourses
        adj:list[list[int]] = [[] for _ in range(numCourses)]
        for src,dst in prerequisites:
            adj[src].append(dst)
            indeg[dst]+=1

        q:deque[int] = deque()
        for n in range(numCourses):
            if indeg[n]==0:
                q.append(n)

        path:list[int] = []
        while q:
            cur = q.popleft()
            path.append(cur)
            for n in adj[cur]:
                indeg[n]-=1
                if indeg[n] == 0:
                    q.append(n)
        return path[::-1] if len(path)== numCourses else []

