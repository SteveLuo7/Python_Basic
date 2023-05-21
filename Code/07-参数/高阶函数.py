def foo():
    print('我是foo， 我被调用了')
    return 'foo'

def bar():
    print('我是bar， 我被调用了')
    return foo()

x = bar()
print('x的值为{}'.format(x))



y = bar()()

