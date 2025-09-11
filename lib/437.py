# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def pathSum(self, root: TreeNode|None, targetSum: int) -> int:
        def dfs(node: TreeNode|None, target:int)->int:
            if not node:
                return 0

            count = 0
            if target-node.val == 0:
                count += 1
            count += dfs(node.left, target-node.val)
            count += dfs(node.right, target-node.val)
            return count

        if not root:
            return 0

        from_root = dfs(root, targetSum)
        from_left = self.pathSum(root.left, targetSum)
        from_right = self.pathSum(root.right, targetSum)

        return from_root+from_left+from_right
