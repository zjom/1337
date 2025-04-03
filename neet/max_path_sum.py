# https://neetcode.io/problems/binary-tree-maximum-path-sum
from icecream import ic

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:TreeNode|None = left
        self.right:TreeNode|None = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val
        def aux(node: TreeNode|None)->int:
            nonlocal res
            if node is None:
                return 0
            left = max(aux(node.left),0)
            right = max(aux(node.right),0)
            res = max(res,node.val+left+right)
            return node.val+max(left,right)

        aux(root)
        return res




s = Solution()
root = TreeNode(1,TreeNode(2), TreeNode(3))
ic(s.maxPathSum(root))

# root = [-15,10,20,null,null,15,5,-5]
root = TreeNode(-15,
                TreeNode(10),
                TreeNode(20,
                         TreeNode(15,
                                  TreeNode(-5)),
                         TreeNode(5)))
ic(s.maxPathSum(root))
