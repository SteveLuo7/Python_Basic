a = '31'

print(int(a) + 20)

x = '1a2c'
y = int(x, 16)
print(y)
# 如果字符串不是一个合法的数字，会直接报错

m = 'abc'
n = int(m, 16)
print(bin(n))


m = float('12')
n = float(12)
print(m != n)