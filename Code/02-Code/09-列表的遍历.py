# 遍历：将所有的数据都访问一次，遍历的对象是可迭代对象
# while循环遍历： / for... in
killers = ['libai', 'lanlingwang', 'hanxin', 'ake', 'sunwukong', 'buzhihuowu', 'zhaoyun', 'machao']
for k in killers:
    print(k)

print('-----------------------------')

i = 0
while i < len(killers):
    print(killers[i])
    i += 1
