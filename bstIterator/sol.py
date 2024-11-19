from collections import deque
# https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class BSTIterator:
    def __init__(self, root: TreeNode|None):
        self.data:deque[int] = deque()

        def traverse(node:TreeNode|None):
            if not node:
                return
            traverse(node.left)
            self.data.append(node.val)
            traverse(node.right)

        traverse(root)

    def next(self) -> int:
        return self.data.popleft()

    def hasNext(self) -> bool:
        return len(self.data) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
