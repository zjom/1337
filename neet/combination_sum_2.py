# https://neetcode.io/problems/combination-target-sum-ii

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res:list[list[int]] = []
        candidates.sort()

        def dfs(i:int,buf:list[int],total:int):
            if total == target:
                res.append(buf.copy())
                return

            for j in range(i,len(candidates)):
                if j > i and candidates[j]==candidates[j-1]:
                    continue

                if total+candidates[j]>target:
                    break
                buf.append(candidates[j])
                dfs(j+1, buf,candidates[j]+total)
                buf.pop()

        dfs(0,[],0)
        return res


s = Solution()
s.combinationSum2(candidates = [9,2,2,4,6,1,5], target = 8)
s.combinationSum2(candidates = [1,2,3,4,5], target = 7)
