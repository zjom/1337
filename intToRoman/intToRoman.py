# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def intToRoman(self, num: int) -> str:
        val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        roman = ""
        for value, symbol in val_map:
            while num >= value:
                roman += symbol
                num -= value
                print(roman)
        return roman


if __name__ == "__main__":
    print(Solution().intToRoman(1994))
