def sum2(nums):
    if len(nums) < 3:
        suml = 0
        for num in nums:
          suml = suml+ num
        return suml
    else:
        suml = 0
        for x in range(2):
          suml = suml + nums[x]
        return suml
