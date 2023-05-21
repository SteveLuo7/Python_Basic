# python里的条件判断  if ifelse/ if elif /
# python里不支持switch case

age = input(
    '请输入你的年龄： '
)
new_age = int(age)
if new_age > 18:
    print('You are welcome')
else:
    print('Not Allowed')