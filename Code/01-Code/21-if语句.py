num = int(input('Please input a Integer: '))


if num % 4 == 0 and num % 6 == 0:
    print('能被4和6整除')
else:
    print('不能够被4和6同时整除')


if (num % 3 == 0 or num % 7 == 0) and (num % 21 != 0):
    print('能够被3或者7整除,且不被3和7同时整除')
