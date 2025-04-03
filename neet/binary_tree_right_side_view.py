# https://neetcode.io/problems/binary-tree-right-side-view

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def rightSideView(self, root: TreeNode|None) -> list[int]:
        if not root:
            return []

        res:list[int] = []
        q:deque[TreeNode] = deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if len(res)==level:
                    res.append(cur.val)
                else:
                    res[-1] = cur.val
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            level +=1
        return res

