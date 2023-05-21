class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + 'is eating')

p1 = Person('zhangsan', 18)
p2 = Person('lisi', 18)

p1.eat()