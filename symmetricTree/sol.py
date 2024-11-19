# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        def aux(left: TreeNode | None, right: TreeNode| None) -> bool:
            if not left and not right:
                return True

            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            return aux(left.left, right.right) and aux(left.right, right.left)

        if not root:
            return True

        return aux(root.left,root.right)
