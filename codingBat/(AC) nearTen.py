def near_ten(num):
  rem = num % 10
  if rem <= 2 or rem >= 8:
    return True
  else:
    return False


print(near_ten(158))