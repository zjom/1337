'''
https://neetcode.io/problems/sliding-window-maximum

You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

Constraints:
    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    1 <= k <= nums.length

  0-2    1-3
[(2,1), (2,1), ()]

maxHeap (max, idx)
if idx < left -> pop
'''


import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_heap:list[tuple[int,int]] = []
        res:list[int] = []
        left,right = 0,0
        while right < len(nums):
            while right < len(nums) and right-left < k:
                heapq.heappush(max_heap, (-1*nums[right],right))
                right+=1

            while max_heap[0][1] < left:
                heapq.heappop(max_heap)
            res.append(-1*max_heap[0][0])
            left+=1

        return res

s = Solution()
nums = [1,2,1,0,4,2,6]
k = 3
s.maxSlidingWindow(nums,k)
