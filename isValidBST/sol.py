# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        def aux(node: TreeNode|None, min_val:float,max_val:float) -> bool:
            if not node:
                return True

            if min_val < node.val and node.val < max_val:
                return aux(node.left,min_val,node.val) and aux(node.right,node.val,max_val)
            return False
        return aux(root, float('-inf'), float('inf'))
