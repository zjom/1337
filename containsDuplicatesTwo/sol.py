# https://leetcode.com/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        m: dict[int,int] = {}
        for i,n in enumerate(nums):
            if n in m and abs(m[n] - i) <= k:
                return True
            m[n] = i

        return False


if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
