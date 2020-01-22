def same_first_last(nums):
  length = len(nums)
  # last = nums[len(nums)-1]
  
  if (length >= 1) and (nums[0] == nums[len(nums)-1]):
    return True
  else:
    return False