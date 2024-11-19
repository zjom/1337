# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150

class Node:
    def __init__(self, x: int, next: 'Node | None' = None, random: 'Node | None' = None):
        self.val: int = int(x)
        self.next: Node | None = next
        self.random: Node | None = random

class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        seen: dict[Node, Node] = {}

        def copy(node: Node | None) -> Node | None:
            if not node:
                return None
            if node in seen:
                return seen[node]

            n = Node(node.val)
            seen[node] = n
            n.next = copy(node.next)
            n.random = copy(node.random)
            return n

        return copy(head)
