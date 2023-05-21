# 元组和列表很像，都是用来保存多个数据
# 使用一对小括号（ ） 来表示一个元组
# 元组和列表的区别在于，列表是可变的，而元组是不可变数据类型

words = ['hello', 'yes', 'why', 'good', 'hi']
nums = (9,4,6,2,1,7,5,9,9)
print(nums[3])
# nums[3] = 100 元组是不可变的数据类型
print(nums.index(5)) # 查询元素下标
print(nums.count(9)) # 计数

x = sorted(nums)
print(x)

print(tuple('hello'))
print(tuple(words))
print(list(nums))
print(set(nums))

#   元组的遍历
for i in nums:
    print(i)

print('=================')
j = 0
while j < len(nums):
    print(nums[j])
    j += 1

