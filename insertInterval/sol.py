# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res:list[list[int]] = []
        i = 0

        # intervals before new
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # intervals overlapping
        while i < len(intervals) and intervals[i][1] >= newInterval[0] and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), 
                        max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)

        # intervals after
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":
    print(Solution().insert([[1,3],[6,9]], [2,5]))
