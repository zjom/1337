# https://leetcode.com/problems/string-compression
class Solution:
    def compress(self, chars: list[str]) -> int:
        chars_len = len(chars)
        cur_len, left, right = 0,0,0

        while right < chars_len:
            while right < chars_len and chars[left] == chars[right]:
                right += 1
            s = chars[left] + (str(right-left) if right-left > 1 else "")
            for c in s:
                chars[cur_len] = c
                cur_len += 1
            left = right

        return cur_len
