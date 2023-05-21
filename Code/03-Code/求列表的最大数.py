nums = [12,345,65,23,3,5,6563,543,23,5465,2,435435,4,7,8]
nums.sort()
print(nums[-1])
print(nums)

x = nums[0]
index = 0
i= 0
#
# for num in nums:
#     if num > x:
#         x = num

while i < len(nums):
    if nums[i] > x:
        x = nums[i]
        index = i
    i += 1

print('发现的最大数字为%d,他的下标是%d' % (x,))