def same_first_last(nums):
    first = nums[0]
    last = nums[-1]
    if len(nums) >= 1 and first == last:
        return True
    else:
        return False

print(same_first_last([1, 2, 3]))