#  下标我们又称之为索引，表示几个数据

# 可迭代对象： str list tuple dict set range

word = 'zhangsan' # 一个一个的字符 字符串
# 在计算机中，下标都是从0开始

# 可以通过下标来修改或者获取指定位置的数据
print(word[4])
# word[4] = 'x' 字符串是不可变的数据类型 对于字符串的任何操作，都不会改变原有字符串

m = 'sjdfklasjdfioewqnfkdsajfl;a'
print(m[5])
print(m[2:])
print(m[3:9])
print(m[:9])
print(m[3:15:2])
print('============================')
print(m[3:15:-1])

# m[start:end:step] 切片语法

print(m[15:3:-1])

print(len(m))
# print(len(m.find(';')))
print(m.find('s', 0, 5))
print(m.find('s'))
print(m.rfind('j'))


print('=============')
print('hello'.startswith('he'))
print('hello'.endswith('o'))

num = input('请输入一个数字')
if num.isdigit():
    print('GOOGOGO')
else:
    print('你输入的不是一个数字')


xyz = 'hello'
c = xyz.replace('h','x')
print(xyz)
print(c)

xx = 'zhangsan-lisi-wangwu-jerry-steve-kobe'
yy = xx.split('-')
print(xx)
print(yy)

print(xx.rsplit('-', 2))
print(xx.split('-', 2))

