# https://neetcode.io/problems/merge-triplets-to-form-target

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        for i in range(3):
            triplets = [triplets[j] for j in range(len(triplets)) if triplets[j][i] <= target[i]]

        for i in range(3):
            if target[i] not in [triplets[j][i] for j in range(len(triplets))]:
                return False
        return True



s = Solution()

triplets = [[1,2,3],[7,1,1]]
target = [7,2,3]
assert s.mergeTriplets(triplets,target)

triplets = [[2,5,6],[1,4,4],[5,7,5]]
target = [5,4,6]
assert not s.mergeTriplets(triplets,target)
