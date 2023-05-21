#   继承特点： 如果一个类A继承自类B，由类A创建出来的十里对象都能直接使用类B里定义的方法

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(self.name + ' is sleeping')

class Students(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def sleep(self):
        print(self.name + ' is sleeping in the classroom')
    def study(self):
        print(self.name + ' is studying')


s = Students('steve', 28, 'chuntianhuahua')
s.sleep()
s.study()
print(s.school)
