# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def maxDepth(self, root: TreeNode|None) -> int:
        def maximum_depth(node: TreeNode|None) -> int:
            if not node:
                return 0
            
            return max(maximum_depth(node.left), maximum_depth(node.right))+1

        return maximum_depth(root)
