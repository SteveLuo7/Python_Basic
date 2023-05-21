person = {'name': 'zhangsan',
          'age': 18,
          'height': '180cm'}

for x in person:
    print(x, '=', person[x])

print('---------------------')

for item in person.items():
    print(item[0], '=', item[1])

print('================')

for k, v in person.items():
    print(k, '=', v)