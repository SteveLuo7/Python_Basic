# break 和continue只能用于循环语句
# break： 用于结束整个循环
# continue：用于结束本轮循环，开启下一轮循环

i = 0
while i < 5:
    if i == 3:
        continue

    print(i)
    i += 1

# username = input('Please input your username')
# password = input('please input your password')
# while not(username == 'zhangsan' and password == '1234'):
#     username = input('Please input your username')
#     password = input('please input your password')
while True:
    username = input('Please input your username: ')
    password = input('please input your password: ')
    if username == 'zhangsan' and password == '1234':
        break
