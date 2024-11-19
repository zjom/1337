from typing import List, Optional


class Node:
    def __init__(self, v: int):
        self.value = v
        self.next: Optional[Node] = None


def walk(n: Optional[Node], i: int) -> Optional[Node]:
    if i == 0 or not n:
        return n
    return walk(n.next, i - 1)


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.length = 0

    def get(self, index: int) -> int:
        n = walk(self.head, index)
        return n.value if n else -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
            return

        tail = walk(self.head, self.length - 1)
        if tail:
            tail.next = Node(val)
            self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next if self.head else None
            self.length -= 1
            return True

        prev = walk(self.head, index - 1)
        if prev and prev.next:
            prev.next = prev.next.next
            self.length -= 1
            return True

        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.value)
            curr = curr.next
        return vals
