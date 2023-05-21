#   python里使用open内置函数打开并操作一个文件

#   open 参数介绍
#   file：用来指定打开的文件 指的是文件的路径
#   mode：打开文件的模式，默认是r 表示只读
#   encoding：打开文件时的编码方式
#   open会有一个返回值，打开的文件对象

file = open('123.txt')
print(file.read())
