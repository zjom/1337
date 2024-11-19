# https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def calculate(self, s: str) -> int:
        def apply_op(op: str, res:int, curr:int, prev: int) -> list[int]:
            # Process the current operation with `curr`
            if op == '+':
                res += curr
                prev = curr
            elif op == '-':
                res -= curr
                prev = -curr
            elif op == '*':
                res -= prev
                res += prev * curr
                prev = prev * curr
            elif op == '/':
                res -= prev
                res += int(prev / curr)
                prev = int(prev / curr)
            return [res,curr,prev]

        def eval(i: int) -> tuple[int, int]:
            res = curr = prev = 0
            curr_op = '+'

            while i < len(s) and s[i] != ')':
                curr_char = s[i]
                if curr_char.isdigit():
                    # Building the number if it's more than one digit
                    curr = 0
                    while i < len(s) and s[i].isdigit():
                        curr = curr * 10 + int(s[i])
                        i += 1
                    i -= 1  # Step back as we will increment `i` in the loop
                    res,curr,prev = apply_op(curr_op, res, curr, prev)

                elif curr_char == '(':
                    # Recursive call to handle expressions in parentheses
                    curr, i = eval(i + 1)
                    # Process the current operation with `curr` after returning from recursion
                    res,curr,prev = apply_op(curr_op, res, curr, prev)
                elif curr_char != ' ':
                    curr_op = curr_char
                i += 1

            return res, i

        # Calculate from the start of the string
        res, _ = eval(0)
        return res
