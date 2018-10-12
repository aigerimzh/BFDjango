def array_front9(nums):
  last = len(nums)
  if last > 4:
    last = 4
  
  for x in range(last):
    if nums[x] == 9:
      return True
  return False
