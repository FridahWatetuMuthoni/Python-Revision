nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(len(nums))
nums.add(8)
nums.add(10)

more_nums = {12, 13, 14, 15}
nums.update(more_nums)
print(nums)