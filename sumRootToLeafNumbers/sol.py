# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def sumNumbers(self, root: TreeNode|None) -> int:
        def aux(node: TreeNode|None, acc: int)->list[int]:
            if not node:
                return []
            curr = acc * 10 + node.val
            nums = [curr] if not node.left and not node.right else []
            nums.extend(aux(node.left, curr))
            nums.extend(aux(node.right,curr))
            return nums

        return sum(aux(root, 0))
