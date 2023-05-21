import sys

import file_manager

from 学生管理系统.files import model

data = {}

def register():
    while True:
        teacher_name = input('请输入账号（3～6位）:')
        if not 3 <= len(teacher_name) <= 6:
            print('账号不符合要求，清重新输入！')
        else:
            break

    while True:
        password = input('请输入密码（6～12位）:')
        if not 6 <= len(password) <= 12:
            print('密码不符合要求，请重新输入')
        else:
            break

    t = model.Teacher(teacher_name, password)
    data[t.name] = t.password
    file_manager.write_json('teacher.json', data)


def login():
    pass



def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n 请选择（1-3）:')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            sys.exit(0)

        else:
            print('输入有误')


if __name__ == '__main__':
    start()