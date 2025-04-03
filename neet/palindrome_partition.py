# https://neetcode.io/problems/palindrome-partitioning

'''
smallest palindrome is 1 char
  - all strings > len 1 has at least [c for c in s] as palindromes

palindromes can be:
  - odd:
    have 1 char center
  - even:
    have 2 char center

palindromes:
  - left side == right side

to determine palindrome:
- start at center and move outward


bbabb

'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        return []
