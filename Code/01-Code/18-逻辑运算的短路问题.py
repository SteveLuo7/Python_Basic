# 逻辑与运算 只有所有运算都为True结果才为True 只要一个结果为False结果就为False
#
4 > 3 and print('hello world')
4 < 3 and print('你好世界')  # 逻辑运算的短路问题

# 逻辑or 只有所有结果为False 结果才为False
# 只要有一个运算结果为True 结果就为True
4 > 3 or print('hahaha')  # 4 > 3 验证为True后 or后面的就不会执行 短路了！！！
4 < 3 or print('heiheihei')

# 逻辑运算符的结果一定为布尔值吗
# 不一定
# 所有取最后一个值
print(3 and 5 and 0 and 'hello')

# 取第一个为True的指标 如果都为False 取最后一个值
print(0 or [] or 'lisi' or 'ok')
print(0 or () or [] or {})


