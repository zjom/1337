# Products of Array Except Self
# https://neetcode.io/problems/products-of-array-discluding-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
            
        return res



if __name__ == "__main__":
    cases = []
    s = Solution()
    cases:list[tuple[list[int],list[int]]] = [
        ([1,2,4,6],[48,24,12,8]),
    ]
    for inp,exp in cases:
        assert s.productExceptSelf(inp) == exp
