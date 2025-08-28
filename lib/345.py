# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:
        # 2 pointers, left and right
        # inc/dec pointers until both are on a vowel
        # swap
        # rpt until left > right

        s_arr = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left,right = 0,len(s)-1
        while left < right:
            if s_arr[left] in vowels and s_arr[right] in vowels:
                tmp = s_arr[left]
                s_arr[left] = s_arr[right]
                s_arr[right] = tmp
                left+=1
                right-=1

            while left < right and s_arr[left] not in vowels:
                left+=1
            while left < right and s_arr[right] not in vowels:
                right -= 1

        return "".join(s_arr)



s = Solution()
ans = s.reverseVowels("leetcode")
print(ans)
