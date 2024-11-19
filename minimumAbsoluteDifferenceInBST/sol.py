# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def getMinimumDifference(self, root: TreeNode|None) -> int:
        cur = root
        stack:list[TreeNode|None] = []
        minDiff,prev = 10**5,-10**5
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node:
                minDiff = min(minDiff,node.val-prev)
                prev = node.val
                cur = node.right
        return minDiff


    def recursive(self, root: TreeNode | None) -> int:
        def aux(node: TreeNode | None,prev_val:int)->tuple[int,int]:
            if not node:
                return 10**5, prev_val

            left_min_diff, prev_val = aux(node.left, prev_val)
            curr_diff = abs(node.val-prev_val)

            right_min_diff, prev_val = aux(node.right, node.val)

            return min(left_min_diff,right_min_diff,curr_diff),prev_val

        min_diff,_ = aux(root,-10**5)
        return min_diff
