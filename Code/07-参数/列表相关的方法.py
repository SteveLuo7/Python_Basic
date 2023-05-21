#   有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]
# nums.sort()
# print(nums)


#   sorted内置函数，不会改变原有的数据，而是生成一个新的结果
sorted(nums)
x = sorted(nums)
print(nums)
print(x)

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98, 'height': 185},
    {'name': 'lisi', 'age': 18, 'score': 95, 'height': 178},
    {'name': 'jack', 'age': 19, 'score': 99, 'height': 183},
    {'name': 'Kobe', 'age': 40, 'score': 100, 'height': 198},
    {'name': 'LeBron', 'age': 38, 'score': 93, 'height': 203},

]

#   字典和字典之间不能使用比较运算
#   缺少比较规则
#   key= 需要的是一个函数 参数类型是函数


students.sort(key=lambda ele: ele['score'])
print(students)