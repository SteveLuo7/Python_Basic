class Student(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print('Running')

    def eat(self):
        print('Eating')


s1 = Student('luoshibin', 25, 184)
s2 = Student('zhuliping', 23, 170)

s1.run()
s2.eat()



