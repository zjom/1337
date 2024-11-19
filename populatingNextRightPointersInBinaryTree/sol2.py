from collections import deque
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node|None' = None, right: 'Node|None' = None, next: 'Node|None' = None):
        self.val:int = val
        self.left:Node|None = left
        self.right:Node|None = right
        self.next:Node|None = next

class Solution:
    def connect(self, root: Node|None) -> Node|None:
        if root is None:
            return root

        q:deque[Node] = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i < size-1:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
