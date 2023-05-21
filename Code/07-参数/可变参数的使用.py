def add(a, b):
    return a + b

def add_many(iter):
    sum = 0
    for i in iter:
        sum += i
    return sum




nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_many(nums))

nums = []
while True:
    num = input('请输入数字，输入exit退出：')
    if num == 'exit':
        break
    nums.append(int(num))
print(nums)

def get_sum(n):
    if n == 0:
        return 0
    return get_sum(n-1) + n


get_sum(6)