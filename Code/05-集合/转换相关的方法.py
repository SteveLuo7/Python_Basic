import json

nums = [9,8,4,3,2,1]
x = tuple(nums)

print(x)

y = set(nums)
print(y)

z = list({'name': 'zhangsan', 'age': 18, 'score': 98})
print(z)


#   json的使用、把列表、元组、字典等转换为json字符串

person = {'name': 'zhangsan', 'age': 18, 'gender': 'male'}
m = json.dumps(person)
print(m)
print(person)

n = '{"name": "lisi", "age": 20}'
k = json.loads(n)
print(k)
print(type(k))




