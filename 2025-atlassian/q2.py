'''
given string with wildcards, return the alphabetically smallest palindrome that can be formed with the letters.
Return -1 if impossible
can rearrange the letters
must use all letters

palindrome is same forward and backwards
palindrome can have 1 or 2 char center

axxb??

if len(input) % 2 == 0 then must have 2 char center => input must have a c where count(c) % 2 == 0
similarly opposite applies


sort input
count input

iterate input in reverse
build front and middle of palindrome 
middle should be as great as possible
'''

from collections import Counter


def getSmallestPalindrome(s:str)->str|int:
    count = Counter(s)
    sorted_s = sorted(s)
    is_odd = len(s)%2 != 0 
    back:list[str] = []
    middle:list[str] = []
    for c in sorted_s[::-1]:
        if c=="?":
            break
        if count[c]==0:
            continue
        if count[c]%2==0:
            back.extend([c]*(count[c]//2))
            count[c]=0
            continue
        if not is_odd:
            if count["?"]==0:
                return -1
            count["?"]-=1
            back.extend([c]*((count[c]+1)//2))
            count[c]=0
            continue
        if not middle:
            middle = [c]*count[c]
            count[c]=0
            continue
        if middle and count["?"]==0:
            return -1
        count["?"]-=1
        back.extend([c]*((count[c]+1)//2))
        count[c]=0

    if not is_odd and count["?"]%2!=0:
        return -1
    if is_odd and middle and count["?"]%2!=0:
        return -1
    if is_odd and not middle and count["?"]%2==1:
        middle = ["a"]
        count["?"]-=1

    while count["?"]>0:
        back.append("a")
        count["?"]-=2

    res = "".join(back[::-1] + middle + back)
    return res if len(res)==len(s) else -1

getSmallestPalindrome("axxb??")
getSmallestPalindrome("a?rt???")
getSmallestPalindrome("yh??tx")
