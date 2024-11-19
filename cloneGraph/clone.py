# https://leetcode.com/problems/clone-graph/description/
from typing import Dict, List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: List[Optional[Node]] = neighbors if \
            neighbors is not None else []


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    seen: Dict[int, Optional[Node]] = {}

    def dfs(node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        cloned = Node(node.val)
        seen[node.val] = cloned
        for n in node.neighbors:
            if n in seen:
                node.neighbors.append(seen[node.val])
                continue
            node.neighbors.append(dfs(n))

        return cloned

    return dfs(node)
