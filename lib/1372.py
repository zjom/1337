# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right
class Solution:
    def longestZigZag(self, root: TreeNode|None) -> int:
        seen:dict[tuple[TreeNode|None,int],int] = {}
        # dir of 1 means that right is valid
        # dir of -1 means that left is valid
        def longest(node: TreeNode|None, dir: int)->int:
            if not node:
                return 0
            if (node, dir) in seen:
                return seen[(node,dir)]
            longest_cur = 0
            if dir == -1 and node.left:
                longest_cur = 1 + longest(node.left, 1)
            if dir == 1 and node.right:
                longest_cur = 1 + longest(node.right, -1)
            seen[(node,dir)] = longest_cur
            return longest_cur

        def dfs(node: TreeNode|None)->int:
            if not node:
                return 0

            longest_cur = max(longest(node,-1),longest(node,1), dfs(node.left), dfs(node.right))

            return longest_cur

        return dfs(root)
