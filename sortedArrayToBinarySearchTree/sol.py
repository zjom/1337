# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode|None:
        def aux(nums:list[int],left:int,right:int)->TreeNode|None:
            if left>right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = aux(nums,left,mid-1)
            root.right = aux(nums,mid+1,right)
            return root
        return aux(nums,0,len(nums)-1)
