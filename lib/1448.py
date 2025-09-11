# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node:TreeNode|None, max_so_far:int)->int:
            if not node:
                return 0
            max_so_far = max(max_so_far, node.val)
            goods = count(node.left, max_so_far)+count(node.right, max_so_far)
            goods += 1 if node.val >= max_so_far else 0
            return goods

        return count(root, root.val)
