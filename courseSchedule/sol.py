# https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preM:dict[int,list[int]] = {course:[] for course in range(numCourses)}
        for course,preq in prerequisites:
            preM[course].append(preq)

        seen:set[int] = set()
        def dfs(course: int)->bool:
            if course in seen:
                return False
            
            if len(preM[course]) == 0:
                return True

            seen.add(course)
            for pre in preM[course]:
                if not dfs(pre):
                    return False

            seen.remove(course)
            preM[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
