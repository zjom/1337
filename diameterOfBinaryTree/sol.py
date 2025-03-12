# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode|None) -> int:
        maximum = 0
        
        def aux(node:TreeNode|None)->int:
            nonlocal maximum
            if not node:
                return -1

            left = aux(node.left)
            right = aux(node.right)
            maximum = max(maximum, left+right+2)

            return max(left,right)+1

        _=aux(root)
        return maximum
