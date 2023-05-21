def calc(a, b, fn):     #   加参数
    return fn(a, b)

def add(x, y):
    return x + y
def minus(x, y):
    return x - y



print(calc(1, 2, minus))



