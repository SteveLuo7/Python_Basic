class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('zhansan', 18)
p2 = Person('zhansan', 18)

print(p1 is p2)
print(p1 == p2)

if type(p1) == Person:
    print('p1 is Person class object')