# https://neetcode.io/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {str(i):i for i in range (10)}

        def parse_num(s: str)->int:
            res = 0
            for  n in s:
                res *= 10
                res += digit_map[n]
            return res

        return str(parse_num(num1)*parse_num(num2))


s = Solution()
s.multiply("4","3")
s.multiply("222","111")
