def closest_numbers(nums:list[int])->None:
    smallest_dif = 2**31
    nums.sort()
    for i in range(1,len(nums)):
        smallest_dif = min(nums[i]-nums[i-1], smallest_dif)
        if nums[i]-nums[i-1] == smallest_dif:
            print(nums[i-1],nums[i])


numbers = [6,2,4,10]
closest_numbers(numbers)


numbers = [4,-2,-1,3]
closest_numbers(numbers)
