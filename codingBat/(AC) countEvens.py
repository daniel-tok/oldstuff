def count_evens(nums):
    evenCount = 0
    for int in nums:
        if int % 2 == 0:
            evenCount += 1
    return evenCount

print(count_evens([2, 1, 2, 3, 4]))