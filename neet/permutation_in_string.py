# Permutation in String
# https://neetcode.io/problems/permutation-string
from icecream import ic

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # count c in s1
        char_count:dict[str,int] = {}
        for c in s1:
            char_count[c] = char_count.get(c,0)+1

        i,j=0,0
        while j-i < len(s1):
            char_count[s2[j]] = char_count.get(s2[j],0)-1
            j+=1

        while j < len(s2):
            ic(char_count)
            for v in char_count.values():
                if v > 0:
                    break
            else:
                return True

            char_count[s2[i]] = char_count.get(s2[i],0)+1
            i+=1
            char_count[s2[j]] = char_count.get(s2[j],0)-1
            j+=1

        for v in char_count.values():
            if v > 0:
                break
        else:
            return True
        return False



if __name__ == "__main__":
    cases = []
    s = Solution()
    cases:list[tuple[str,str,bool]] = [
        ("abc", "lecabee",True),
        ("abc", "lecaabee",False),
        ("adc", "dcda",True),
    ]
    for i,(s1,s2,exp) in enumerate(cases):
        res = s.checkInclusion(s1,s2)
        try:
            assert res == exp
        except AssertionError:
            print(f"test {i} failed")
            ic(s1,s2,res,exp)
