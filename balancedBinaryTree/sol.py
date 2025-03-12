# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, x:int):
        self.val = x
        self.left:TreeNode|None = None
        self.right:TreeNode|None = None

class Solution:
    def isBalanced(self, root: TreeNode|None) -> bool:
        if not root:
            return True

        def aux(node: TreeNode|None)->int:
            if not node:
                return 0
            left = aux(node.left)
            right = aux(node.right)
            if left == -1 or right == -1:
                return -1

            if abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        return aux(root) != -1
