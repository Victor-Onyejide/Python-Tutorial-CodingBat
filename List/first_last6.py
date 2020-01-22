# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

#Solution
def first_last6(nums):
  if nums[0] == 6:
    return True
  if nums[len(nums) - 1] == 6:
    return True
  else:
    return False
