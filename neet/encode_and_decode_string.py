# Encode and Decode Strings
# https://neetcode.io/problems/string-encode-and-decode

from icecream import ic


# class Solution:
#     def encode_str(self, s: str)->str:
#         return ','.join([str(ord(c)) for c in s])
#     def encode(self, strs: list[str]) -> str:
#         if len(strs) == 0:
#             return '!'
#         return ';'.join([self.encode_str(s) for s in strs])
#
#     def decode_str(self, s:str)->str:
#         res = ''
#         for p in s.split(','):
#             if p != '':
#                 c = int(p)
#                 res += chr(c)
#         return res
#     def decode(self, s: str) -> list[str]:
#         match s:
#             case '':
#                 return ['']
#             case '!':
#                 return []
#             case _:
#                 return [self.decode_str(st) for st in s.split(';')]

class Solution:
    def encode(self, strs:list[str])->str:
        res = ''
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s:str)->list[str]:
        res:list[str]= []
        i = 0

        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1

            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res


if __name__ == "__main__":
    cases = []
    s = Solution()
    cases:list[tuple[list[str],list[str]]] = [
        ([""], [""]),
        ([], []),
        (["neet","code","love","you"], ["neet","code","love","you"])
    ]
    for inp,exp in cases:
        encoded = s.encode(inp)
        decoded = s.decode(encoded)
        ic(inp,encoded,decoded)
