class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        retv = ["" for _ in range(numRows)]
        idx, dir = 0, 1
        for c in s:
            retv[idx] += c
            if idx == numRows-1:
                dir = -1
            if idx == 0:
                dir = 1
            idx += dir

        return ''.join(retv)
