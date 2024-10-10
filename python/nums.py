import math
# Given a list of ints
nums = [25, 10, 47, 36, 89, 74, 53, 61, 42, 98]

# Add them
# Quick way
print(f"tot: {sum(nums)}")

# Long way
total = 0
for i in nums:
    total = total + i
print(f"tot: {total}")

total = sum(nums)
# Get average
average = total / len(nums)

print(f"ave: {average}")

print(sorted(nums))

print(sorted(nums, reverse=True))