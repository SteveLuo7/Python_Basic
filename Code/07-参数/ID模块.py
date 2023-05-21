import uuid

print(uuid.uuid1())
# print(uuid.uuid2())
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'zhangsan'))
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'zhangsan'))

print(uuid.uuid4())
