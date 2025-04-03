# https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left,right = 0,0
        seen:set[str] = set()

        while left<=right and right < len(s):
            while s[right] in seen and left <=right:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            right += 1
            res = max(res,len(seen))
        return res


s = Solution()
cases = [("zxyzxyz", 3), ("xxxx",1)]
for inp,exp in cases:
    assert s.lengthOfLongestSubstring(inp) == exp
