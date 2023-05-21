class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def demo(self):
        print('Name: ', self.name)

    @staticmethod
    def foo():
        print(p.name)

p = Person('zhangsan', 19)
print('ox%X,0x%X' % (id(Person), id(p)))

p.foo()
Person.foo()
Person.demo(p)
p.demo()
