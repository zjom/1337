from collections import deque
from icecream import ic
# https://neetcode.io/problems/serialize-and-deserialize-binary-tree
# Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode|None'=None, right:'TreeNode|None'=None):
        self.val:int = val
        self.left:'TreeNode|None' = left
        self.right:'TreeNode|None' = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode|None) -> str:
        res:list[str] = []
        q:deque[TreeNode|None] = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                res.append('N')
                continue
            res.append(str(curr.val))
            q.append(curr.left)
            q.append(curr.right)

        return ','.join(res)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode|None:
        if data == 'N':
            return None
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        i = 1
        q:deque[TreeNode] = deque([root])
        while q and i < len(vals):
            curr = q.popleft()
            if vals[i] != 'N':
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i+=1

            if vals[i] != 'N':
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i+=1
        return root

if __name__=="__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    c = Codec()
    ic(c.serialize(root))
