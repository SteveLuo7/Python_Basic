# 列表是用来保存多个数据的
# 操作列表，一般都包含增删改查
# 增删改查 CRUD

heros = ['Ake', 'yinzheng', 'hanxin', 'houyi', 'yase', 'liyuanba', 'liyuanfang']
# 添加元素的方法
heros.append('huangzhong')
print(heros)
print(len(heros))

# 在指定位置插入数据
heros.insert(3, '李白')
print(heros)

x = ['马可波罗', '米莱狄', '狄仁杰']
heros.extend(x)
print(heros)
