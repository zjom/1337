from collections import deque
# https://leetcode.com/problems/course-schedule-ii/?envType=study-plan-v2&envId=top-interview-150

# this works but it sucks
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
#         if len(prerequisites) < 1:
#             return [i for i in range(numCourses)]
#
#         graph:dict[int,list[int]] = {i:[] for i in range(numCourses)}
#         for course, prereq in prerequisites:
#             graph[course].append(prereq)
#         seen:set[int] = set()
#         result:list[int] = []
#
#         def dfs(course:int):
#             if course in seen:
#                 return False
#             if course in result:
#                 return True
#             
#             seen.add(course)
#             for prereq in graph[course]:
#                 if not dfs(prereq):
#                     return False
#
#             result.append(course)
#             seen.remove(course)
#             graph[course] = []
#             return True
#
#         for course in range(numCourses):
#             if not dfs(course):
#                 return []
#         return list(result)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj:list[list[int]] = [[] for _ in range(numCourses)]
        in_degree:list[int] = [0] * numCourses
        for dst, src in prerequisites:
            adj[src].append(dst)
            in_degree[dst] += 1

        queue:deque[int] = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        result:list[int] = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for prereq in adj[course]:
                in_degree[prereq] -= 1
                if in_degree[prereq] == 0:
                    queue.append(prereq)

        return result if len(result)==numCourses else []
