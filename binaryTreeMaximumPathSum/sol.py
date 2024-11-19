# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def maxPathSum(self, root: TreeNode|None) -> int:
        result = float("-inf")

        def aux(node: TreeNode|None)->int:
            nonlocal result
            if not node:
                return 0

            right = max(aux(node.right),0)
            left = max(aux(node.left),0)

            max_so_far = node.val + right + left
            result = max(max_so_far, result)
            return node.val + max(right,left)

        _ = aux(root)
        return int(result)
