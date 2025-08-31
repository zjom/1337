# https://leetcode.com/problems/removing-stars-from-a-string
class Solution:
    def removeStars(self, s: str) -> str:
        acc:list[str] = []
        for c in s:
            if c == "*":
                _ = acc.pop()
            else:
                acc.append(c)
        return "".join(acc)

s = Solution()
assert s.removeStars("leet**cod*e") == "lecoe"
assert s.removeStars("erase*****") == ""
