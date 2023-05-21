
def tell_story(place, person1, person2):
    print('从前有座山')
    print('山里有座' + place)
    print(place + '里有个' + person1)
    print('还有一个' + person2)
    print(person1 + '在给' + person2 + '讲故事')
    print('故事的内容是')


#   使用def来声明一个函数
#   def 函数名（）：
#   函数要执行的操作

age = int(input('孩子的年龄是： '))
if 0 <= age < 3:
    for i in range(5):
        tell_story('尼姑庵', '师太', '小尼姑' )
elif 5 > age >= 3:
    tell_story('道观', '老道', '小道童' )
    

