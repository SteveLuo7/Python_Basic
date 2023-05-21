import time


def cal_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时：', end - start)
    return inner


@cal_time
def demo():
    x = 0
    for i in range(1, 1000000):
        x += i
    print(x)

@cal_time
def foo():
    print('hello')
    time.sleep(3)
    print('world')


demo()
foo()