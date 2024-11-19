# https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res: list[str] = []
        i = 0
        while i < len(nums):
            j = i
            currInterval = [nums[i]]
            while j < len(nums)-1 and nums[j]+1 == nums[j+1]:
                currInterval.append(nums[j+1])
                j += 1

            if len(currInterval) == 1:
                res.append(str(currInterval[0]))
            else:
                res.append(f"{currInterval[0]}->{currInterval[-1]}")

            i = j + 1

        return res

if __name__ == "__main__":
    print(Solution().summaryRanges([0,1,2,4,5,7]))
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))

