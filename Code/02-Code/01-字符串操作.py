print('hello'.index('h'))

print('hello'.capitalize())

print('hello'.upper())

print('LUOSHIBIN'.lower())

print('LUOSHIBIN'.title())

while True:
    content = input('请输入内容，输入Exit退出: ')
    print('你输入的内容是：', content)
    if content.capitalize() == 'Exit':
        break

print('Monday'.ljust(10, '+'))
print('Monday'.rjust(10, '+'))
print('Monday'.center(10, '+'))


x = 'zhangsan+lisi+wangwu+luoshibin+steve'
names = x.split('+')
print(names)

fruits = ['apple','pear','peach','banana','orange','grape']
print('-'.join(fruits))

