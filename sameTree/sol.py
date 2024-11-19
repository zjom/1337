# https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def isSameTree(self, p: TreeNode|None, q: TreeNode|None) -> bool:
        def aux(p: TreeNode|None, q: TreeNode|None) -> bool:
            if q and p:
                if p.val != q.val:
                    return False
                return aux(p.left,q.left) and aux(p.right,q.right)
            elif (p and not q) or (q and not p): 
                return False
            else:
                return True
        return aux(p,q)
