# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.stack:list[int] = []
        self.helper:list[int] = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            return

        while self.stack:
            self.helper.append(self.stack.pop())
        self.stack.append(x)
        while self.helper:
            self.stack.append(self.helper.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        x = self.stack.pop()
        self.stack.append(x)
        return x

    def empty(self) -> bool:
        return self.stack == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
