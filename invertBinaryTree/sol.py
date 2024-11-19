# https://leetcode.com/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def invertTree(self, root: TreeNode|None) -> TreeNode|None:

        def aux(node: TreeNode|None)->TreeNode|None:
            if not node:
                return None

            left = aux(node.right)
            node.right = aux(node.left)
            node.left = left
            return node

        return aux(root)
