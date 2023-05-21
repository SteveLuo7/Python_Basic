def say_hello(name, age, city='GuangZhou'):
    print('大家好，我是{}，我今年{}岁了， 我来自{}'.format(name,age,city))

say_hello('luoshibin', 28, 'luoyang')


print('hello', '你好', sep='_________', end='')
print('woshiluoshibin')

say_hello('zhuliping',25) # 没有传递city的参数，自动使用默认的 