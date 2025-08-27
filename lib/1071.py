# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1),len(str2)
        gcd_str = str2 if str1_len >= str2_len else str1
        gcd_str_len = len(gcd_str)
        while gcd_str:
            if str1_len % gcd_str_len != 0 or str2_len % gcd_str_len != 0:
                gcd_str = gcd_str[:gcd_str_len-1]
                gcd_str_len-=1
                continue

            n_rpts = int(str1_len/gcd_str_len)
            for i in range(n_rpts):
                left, right = i*gcd_str_len, (i+1)*gcd_str_len
                if str1[left: right] != gcd_str or \
                    (right <= str2_len and str2[left:right] != gcd_str):
                    break
                if i == n_rpts-1:
                    return gcd_str
            gcd_str = gcd_str[:gcd_str_len-1]
            gcd_str_len-=1
        return ""
