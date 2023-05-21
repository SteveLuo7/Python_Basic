masters = ['wangzhaojun', 'zhenji', 'diaochan', 'xiaoqiao', 'daqiao', 'daji']

# 删除 pop remove clear

# pop 默认删除最后一个元素 还可以传入下标参数 删除指定数据

masters.pop(3)
print(masters)

# remove

masters.remove('zhenji')
print(masters)


# del
del masters[0]
print(masters)

# clear 清零
masters.clear()
print(masters)



tanks = ['亚瑟', '程咬金', '盾山', '张飞', '廉颇']
# 查询相关的方法
print(tanks.index('盾山'))
# print(tanks.index('庄周'))
print(tanks.count('程咬金'))

print('张飞' in tanks)
print('罗仕斌' in tanks)

# modified
tanks[4] = '凯'
print(tanks)


