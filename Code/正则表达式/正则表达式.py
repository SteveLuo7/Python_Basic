#   用来处理字符串，对字符串进行检索和替换
#   1、查找    2、替换
#   看身份证格式是否正确
# card_id = input('请输入你的身份证号码')
import re
x = 'hello\\world'
print(x)

#   在正则表达式中，如果想要匹配一个\ 需要使用三个\\\

#   第一个参数就是正则匹配规则
#   第二个参数表示需要匹配的字符串

m = re.search('\\\\', x)
print(m)

#   match
#   search
#   finditer
#   findall
#   fullmatch


