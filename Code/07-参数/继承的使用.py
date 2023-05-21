class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + 'Sleeping')

class Dog(Animal):
    def bark(self):
        print(self.name + 'barking')

class Students(Animal):
    def study(self):
        print(self.name + 'is studying')

d1 = Dog('keji',18)
print(d1.name)
d1.sleep()

s1 = Students('luoshibin', 28)
s1.study()