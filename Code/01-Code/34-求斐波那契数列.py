# 求斐波那契数列中第n个数值， n为正整数
# 1,1,2,3,5,8,13,21,34,55,89,144


# i = 0
# num1 = 1
# num2 = 1
# while i < 10:
#     numX = num1 + num2
#     num1 = numX
#     numY = num1 + num2
#     num2 = numY
#     i += 2
# print(numX,numY)
num3 = 1
num4 = 1
for i in range(0, 12 -2):
    a = num3
    num3 = num4
    num4 = a + num4
print(num4)