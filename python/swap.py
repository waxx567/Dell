a, b = 35, 75
x, y, z = 45, 65, 85
a, b = b, a
x, y, z = y, x, z
print(a, b)
print(x, y, z)

nums = [25, 10, 47, 36, 89, 74, 53, 61, 42, 98]
new = []
count = (len(nums) - 1)
while count > -1:
    new.append(nums[count])
    count -= 1
print(nums)
print(new)