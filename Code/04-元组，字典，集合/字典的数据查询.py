#   查找数据（字典的数据在保存时，是无序的，不能通过下标来获取）
#   字典的数据是以键值对存在的

person = {'name': 'zhangsan',
          'age': 18
          }

print(person['name'])

x = 'age'
print(person[x])

#   通过key可以找value，不能通过value找key
