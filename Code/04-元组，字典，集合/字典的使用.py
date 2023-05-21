#   列表可以存储任意数据类型，但是一般情况下，我们都存储单一数据类型
scores = [100, 98, 99, 61]
names = ['zhangsan', 'lisi', 'wangwu']

#   列表只能存储值，但是无法对值进行描述
# person = ['zhangsan', 'lisi', 13, 15, 567, 67, 34]

#   字典不仅可以保存值，还能对值进行描述
#   使用打括号来表示一个字典，不仅有值value，还有值的描述key
#   key和value之间使用冒号： 来连接

person = {'name': 'zhangsan',
          'age': 18,
          'math': 98,
          'english': 80,
          'chinese': 87,
          'height': 180,
          'weight': 75,
          'hobbies': ['sing', 'dance', 'rap', 'basketball']
          }
#   字典的缺点
#   字典中的key不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
#   字典里的value可以是任意数据类型，但是key只能使用不可变数据类型，一半是用字符串
