def add(a: int, b: int):
    """
    这个函数用来将两个数字相加
    :param a:  第一个数字
    :param b:  第二个数字
    :return:   两个数字相加的结果

    """
    return a + b

help(add)

x = add(1, 2)
print(x)

y = add('hello', 'luoshibin')
print(y)


def test(a, b):
    x = a // b
    y = a % b
    return x, y


result = test(13, 5)
print('商是{}, 余数是{}'.format(result[0],result[1]))


