class UF:
    def __init__(self, N:int) -> None:
        self.parents: list[int] = list(range(N))

    def union(self, child: int, parent:int) -> None:
        self.parents[self.find(child)] = self.find(parent)
        pass

    def find(self, x:int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
