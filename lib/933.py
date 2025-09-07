# https://leetcode.com/problems/number-of-recent-calls
from collections import deque
class RecentCounter:
    def __init__(self):
        self.data:deque[int] = deque()

    def ping(self, t: int) -> int:
        while self.data and self.data[0] < t-3000:
            _ = self.data.popleft()
        self.data.append(t)
        return len(self.data)
