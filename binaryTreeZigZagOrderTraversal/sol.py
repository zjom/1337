# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode|None) -> list[list[int]]:
        if not root:
            return []

        res: list[list[int]] = []
        q: deque[TreeNode] = deque([root])
        left = True
        while q:
            length = len(q)
            tree = [0]*length
            for i in range(length):
                curr = q.popleft()
                if left:
                    tree[i] = curr.val
                else:
                    tree[length-1-i] = curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            left = not left
            res.append(tree)

        return res
