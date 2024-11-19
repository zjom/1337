# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val:int = val
        self.left:TreeNode | None = left
        self.right:TreeNode | None = right

class Solution:
    def kthSmallest(self, root: TreeNode|None, k: int) -> int:
        stack:list[TreeNode] = []
        cur = root
        n = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+=1
            if n == k:
                return cur.val
            cur = cur.right
        return -1

    def recursive(self, root:TreeNode|None,k:int) -> int:
        def aux(node:TreeNode|None, counter: int) -> tuple[int,int|None]:
            if not node:
                return counter,None

            counter,result = aux(node.left,counter)
            if result is not None:
                return counter, result

            counter += 1
            if counter == k:
                return counter, node.val

            return aux(node.right, counter)

        _, result = aux(root,0)
        return result if result is not None else -1


    def naive(self, root:TreeNode|None,k:int) -> int:
        def traverse(node:TreeNode|None) -> list[int]:
            if not node:
                return []
            res:list[int] = []
            res.extend(traverse(node.left))
            res.append(node.val)
            res.extend(traverse(node.right))
            return res
        nums = traverse(root)
        return nums[k-1]

