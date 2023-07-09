nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []

index = 0
while index < len(nums):
    if nums[index] % 2 == 0:
        even.append(nums[index])

    index += 1

print(even)

for i in nums:
    if i % 2 == 0:
        even.append(i)

print(even)
