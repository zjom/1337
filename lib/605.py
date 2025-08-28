# https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        padded_flowerbed = [0] + flowerbed + [0]

        count = 0
        for i in range(1, len(padded_flowerbed)-1):
            if padded_flowerbed[i] != 0 or padded_flowerbed[i-1]!=0 or padded_flowerbed[i+1]!=0:
                continue
            padded_flowerbed[i] = 2
            count += 1
        return count >= n

