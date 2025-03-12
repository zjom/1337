# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
from random import randint

def isBadVersion(version: int) -> bool:
    return version == randint(1,10)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1,n

        while low < high:
            mid = low+(high-low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
