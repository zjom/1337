# https://neetcode.io/problems/insert-new-interval

from icecream import ic

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        def merge(intv1: list[int], intv2:list[int])->list[int]:
            return [min(intv1[0],intv2[0]), max(intv1[1],intv2[1])]

        res:list[list[int]] = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] >= newInterval[0]:
                break
            res.append(intervals[i])
            i+=1

        while i < len(intervals) and \
            intervals[i][1] >= newInterval[0] and \
            intervals[i][0] <= newInterval[1]:
            newInterval = merge(intervals[i],newInterval)
            i+=1
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res

s = Solution()
def test(intervals:list[list[int]],newInterval:list[int],expected:list[list[int]]):
    res = s.insert(intervals,newInterval)
    ic(res)
    assert sorted(res) == sorted(expected)

intervals = [[1,3],[4,6]]
newInterval = [2,5]
expected = [[1,6]]
test(intervals,newInterval, expected)


intervals = [[1,2],[3,5],[9,10]]
newInterval = [6,7]
expected = [[1,2],[3,5],[6,7],[9,10]]
test(intervals,newInterval,expected)
