def centered_average(nums):
  nums.sort()
  nums.pop([-1])
  total = 0
  del nums[0]
  for number in nums:
    total += number
  return total / float(len(nums))

print(centered_average([10, 3, 5, 6]))