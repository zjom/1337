from typing import List, Optional


class DynamicArray:

    def __init__(self, capacity: int):
        self.arr: List[Optional[int]] = [None for _ in range(capacity)]
        self.length = 0

    def get(self, i: int) -> int | None:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        if i >= self.length:
            self.length = self.length+1

    def pushback(self, n: int) -> None:
        if len(self.arr) == self.length:
            self.resize()
        self.arr[self.length] = n
        self.length = self.length+1

    def popback(self) -> int | None:
        v = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length = self.length - 1
        return v

    def resize(self) -> None:
        next: List[Optional[int]] = [None for _ in range(self.length*2)]
        for i, n in enumerate(self.arr):
            next[i] = n
        self.arr = next

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return len(self.arr)
