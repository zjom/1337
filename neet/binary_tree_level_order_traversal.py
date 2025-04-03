# https://neetcode.io/problems/level-order-traversal-of-binary-tree
# Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:'TreeNode|None' = left
        self.right:'TreeNode|None' = right

class Solution:
    def levelOrder(self, root: TreeNode|None) -> list[list[int]]:
        res: list[list[int]] = []

        def aux(node:TreeNode|None,i:int)->None:
            if not node:
                return

            if i >= len(res)-1:
                res.append([])

            res[i].append(node.val)
            aux(node.left,i+1)
            aux(node.right,i+1)

        aux(root,0)
        return res
