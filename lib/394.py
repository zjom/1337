# https://leetcode.com/problems/decode-string/
from icecream import ic

class Solution:
    def decodeString(self, s: str) -> str:
        stack:list[tuple[int,str]] = []
        cur_num:int = 0
        cur_word:str = ''

        for c in s:
            if c.isdigit():
                cur_num = cur_num*10 + int(c)
            elif c == '[':
                stack.append((cur_num,cur_word))
                cur_num = 0
                cur_word = ''
            elif c == ']':
                num, prev_str = stack.pop()
                cur_word = prev_str + cur_word*num
            else:
                cur_word += c

        return cur_word


s = Solution()
assert ic(s.decodeString("3[a]2[bc]")) == "aaabcbc"
assert ic(s.decodeString("3[a2[c]]")) == "accaccacc"
assert ic(s.decodeString("2[abc]3[cd]ef")) == "abcabccdcdcdef"

