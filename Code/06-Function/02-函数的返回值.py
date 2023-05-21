#   函数的返回值就是函数执行的结果，并不是所有的函数都必须有返回值

def add(a, b):
    c = a + b #     变量c在外部是不可见的，只能在函数内部使用
    return c  #     return表示一个函数的执行结果


result = add(1, 2)
print(result ** 4)

x = print('hello')
print(x)

age = int(input('please input'))
print(age)
