# https://neetcode.io/problems/course-schedule

from icecream import ic
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree = [0]*numCourses
        adj_list:list[list[int]] = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            in_degree[dst]+=1
            adj_list[src].append(dst)

        q:deque[int] = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)

        finish = 0
        while q:
            cur = q.popleft()
            finish+=1
            for n in adj_list[cur]:
                in_degree[n]-=1
                if in_degree[n]==0:
                    q.append(n)

        return finish == numCourses

s = Solution()
assert True == ic(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
assert True == ic(s.canFinish(numCourses = 2, prerequisites = [[0,1]]))
assert False == ic(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))


