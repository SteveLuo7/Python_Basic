score = int(input('请输入你的成绩： '))


if score == 100:
    print('Wonderful')
elif 80 <= score < 100:
    print('You are perfect')
elif 60 <= score < 80:
    print('you are good ')
elif 0 <= score < 60:
    print('You need to work hard')
elif score < 0 or score > 100:
    print('Stats Wrong')