# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digitToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res:list[str] = []
        def aux(idx:int, acc:str):
            if idx == len(digits):
                res.append(acc[:])
                return

            for letter in digitToLetters[digits[idx]]:
                aux(idx+1,acc+letter)

        aux(0, "")

        return res
