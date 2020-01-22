def common_end(a, b):
  len_a = len(a)
  len_b = len(b)
  
  if (len_a >= 1 and len_b >= 1) and (a[0] == b[0] or a[len_a - 1] == b[len_b - 1]):
    return True
  else:
    return False