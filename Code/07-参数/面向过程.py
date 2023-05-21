def add_user():
    pass

def del_user():
    pass

def modify_user():
    pass

def query_user():
    pass

def show_all():
    pass

def add_user():
    pass



while True:
    print('----------------------------------')
    operator = input('Please press the button')
    if operator == '1':
        add_user()
    elif operator == '2':
        del_user()
    elif operator == '3':
        modify_user()
    elif operator == '4':
        query_user()
    elif operator == '5':
        show_all()
    else:
        print('Wrong Submit, Please Repress')

