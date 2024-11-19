# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        res = curr = prev = 0
        curr_op = '+'

        i = 0
        while i < len(s):
            curr_char = s[i]
            if curr_char.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1
                match curr_op:
                    case '+':
                        res += curr
                        prev = curr
                    
                    case '-':
                        res -= curr
                        prev = -curr
                    
                    case '*':
                        res -= prev
                        res += prev*curr
                        prev = prev*curr
                    case '/':
                        res -= prev
                        res += int(prev/curr)
                        prev = int(prev/curr)
                    case _:
                        raise ValueError('bruh')
                curr = 0
                
            elif curr_char != ' ':
                curr_op = curr_char

            i += 1

        return res
