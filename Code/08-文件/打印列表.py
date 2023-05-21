class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'hello'

    def __repr__(self):
        return 'Name: {}, Age: {}'.format(self.name, self.age)
p1 = Person('zhangsan', 18)
p2 = Person('lisi', 18)

print(p1)

print([p1, p2])