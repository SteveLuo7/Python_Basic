# 1、区间判断

score = float(input('请输入你的成绩'))

if 60 > score >= 0:
    print('You re Trash')

# 2、 隐式类型转换
if 4: # if后面需要的是一个bool类型的值。如果if后面不是布尔类型，会自动转换成为布尔类型。
    print('hello world')

# 3、 三元表达式
num1 = int(input('请输入一个数字：'))
num2 = int(input('请输入另一个数字： '))

# if num1 > num2:
#     x = num1
# else:
#     x = num2

x = num1 if num1 > num2 else num2
print('两个数字中较大的数字为： ', x)

