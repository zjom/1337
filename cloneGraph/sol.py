# https://leetcode.com/problems/clone-graph/description/

# Definition for a Node.
class Node:
    def __init__(self, val:int = 0, neighbors:'list[Node]|None' = None):
        self.val:int = val
        self.neighbors:list[Node] = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node|None) -> Node|None:
        if not node:
            return None

        seen:dict[Node,Node] = {}

        def clone(node:Node|None) -> Node|None:
            if not node:
                return None
            if node in seen:
                return seen[node]
            
            seen[node] = Node(node.val)
            seen[node].neighbors = [clone(n) for n in node.neighbors]
            return seen[node]

        return clone(node)
