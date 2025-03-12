# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, x:int):
        self.val = x
        self.left:TreeNode|None = None
        self.right:TreeNode|None = None

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode|None:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
