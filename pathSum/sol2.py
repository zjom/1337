# https://leetcode.com/problems/path-sum-ii/description/

# Definition for a binary tree node.
from typing import final
@final
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode|None, targetSum: int) -> list[list[int]]:
        def aux(node:TreeNode|None, acc: int, res: list[int]) -> list[list[int]]:
            if not node:
                return []
            
            res.append(node.val)
            acc += node.val

            if not node.left and not node.right and acc == targetSum:
                return [res]
            
            left = aux(node.left, acc, [n for n in res])
            right = aux(node.right, acc, [n for n in res])
            left.extend(right)
            return left

        return aux(root, 0, [])
