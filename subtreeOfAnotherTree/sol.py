# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode|None, subRoot: TreeNode|None) -> bool:
        def isMatch(node:TreeNode|None, sub:TreeNode|None)->bool:
            if not(node and sub):
                return node is sub
            return (node.val == sub.val and 
                isMatch(node.left,sub.left) and 
                isMatch(node.right,sub.right))

        def solve(node:TreeNode|None,sub:TreeNode|None)->bool:
            if isMatch(node,sub):
                return True
            if not node:
                return False
            return solve(node.left, sub) or solve(node.right, sub)

        return solve(root,subRoot)
