from typing import final
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
@final
class TreeNode:
    def __init__(self, x:int):
        self.val = x
        self.left:TreeNode|None = None
        self.right:TreeNode|None = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def aux(node: TreeNode|None)->TreeNode|None:
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node

            left = aux(node.left)
            right = aux(node.right)

            if left and right:
                return node

            return left or right

        res = aux(root)
        return res if res else TreeNode(-1)


    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr:TreeNode|None = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr or TreeNode(-1)
        return curr or TreeNode(-1)
