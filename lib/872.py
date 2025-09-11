# https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def leafSimilar(self, root1: TreeNode|None, root2: TreeNode|None) -> bool:
        def collect(node: TreeNode|None)->list[int]:
            if not node:
                return []
            if node.left or node.right:
                return collect(node.left)+collect(node.right)
            return [node.val]
        left = collect(root1) 
        right = collect(root2)
        return left == right
