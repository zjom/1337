# https://leetcode.com/problems/dota2-senate
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue:deque[int] = deque()
        d_queue:deque[int] = deque()

        for i,c in enumerate(senate):
            if c == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        idx = 0
        while True:
            if not (r_queue and d_queue):
                break
            match senate[idx]:
                case 'R' if r_queue[0] == idx:
                    r = r_queue.popleft()
                    r_queue.append(r)
                    _ = d_queue.popleft()
                case 'D' if d_queue[0] == idx:
                    d = d_queue.popleft()
                    d_queue.append(d)

                    _ = r_queue.popleft()
                case _:
                    assert "bruh"
            
            idx +=1
            if idx == len(senate):
                idx = 0

        return 'Radiant' if r_queue else 'Dire'
