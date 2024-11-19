# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def maxDepth(self, root:TreeNode|None) -> int:
        if not root:
            return 0

        def dfs(n: TreeNode|None, level:int)->int:
            if not n:
                return level

            return max(dfs(n.left,level+1),dfs(n.right,level+1))

        return dfs(root,0)
