# if语句的嵌套
ticket = input('是否购买了火车票？ Y/N')
if ticket == 'Y':
    print('你可以进入火车站')
    safe = input('案件是否通过？ Y/N')
    if safe == 'Y':
        print('安检通过')
    else:
        print("进站了，但是安检不通过")
else:
        print('没有买票，走走走')

