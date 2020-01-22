
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

#Solution

def common_end(a, b):
  len_a = len(a)
  len_b = len(b)
  
  if (len_a >= 1 and len_b >= 1) and (a[0] == b[0] or a[len_a - 1] == b[len_b - 1]):
    return True
  else:
    return False
